import openpyxl

def parsing(file_name):
    wb = openpyxl.load_workbook(file_name)
    result = []
    index = 0
    for sheet in wb:        #Проход по страницам excel файла
        answers = []        #Список ответов для каждого опрошенного
        check_first_row = 1 #Флаг проверки первой строки 
        for row in sheet.iter_rows(values_only=True):   #Проход по строкам на каждой странице
            if (check_first_row == 1):
                check_first_row = 0
                continue
            answers.append(list(row))   #Добавление ответа в список
        result.append(answers)  #Добавление ответов в результирующий список
    return result


USELESS_SYMBOLS = ['.', ',', '!', '?']
USELESS_ANSWERS = ['нет', 'спасибо']

'''
prepross for user and hr
'''
def preprocess(array_hr, array_user):
    return preprocess_user(array_user) + preprocess_hr(array_hr)


'''

'''
SPECIAL_WORDS = ['тест', '-', 'none']
LEN_ACCESS = 5
QUESTION_STAY = 1       # index
QUESTION_RETURN = 2
def preprocess_user(array):
    array = array_purify(array)
    lines_count = len(array)
    columns_count = len(array[0]) if len(array) > 0 else 0
    for line in range(lines_count):
        # объединение 1 и 1.1 вопросов
        array[line][0] = ' '.join([array[line][0], array[line][1]])
        array[line].pop(1)
        # обработка каждой строки
        array[line] = [user_line_purify(str(string), column, string_dlc) for string, column, string_dlc in string_unite(array[line], range(4))]
    return array

'''

'''
def string_unite(array_questions, array_numbers):
    array_unite = list(zip(array_questions, array_numbers))
    for ques in array_numbers:
        array_unite[ques] = list(array_unite[ques])
        if 'описано выше' not in array_questions[QUESTION_STAY]:
            array_unite[ques].append(array_questions[QUESTION_STAY])
        else:
            array_unite[ques].append(array_questions[QUESTION_RETURN])

    return array_unite

def user_line_purify(string, column, string_dlc = ''):
    if column == QUESTION_STAY or column == QUESTION_RETURN:            # дублирование: номера вопросов, в которых может быть фраза 'описано выше'
        if 'описано выше' in string:
            string = string_dlc
    if len(string) < LEN_ACCESS:
        string = str(string)
        for word in string.split():                                     # проверка на мусор
            if word in SPECIAL_WORDS:
                string = ''
                break
    return string

'''

'''
def preprocess_hr(array):
    array = array_purify(array)
    lines_count = len(array)
    columns_count = len(array[0]) if len(array) > 0 else 0
    for line in range(lines_count):
        # объединение 1 и 1.1 вопросов
        array[line].insert(0, '')
        # обработка каждой строки
        array[line] = [hr_line_purify(str(string), column, string_dlc) for string, column, string_dlc in string_unite(array[line], range(5))]
    return array

def hr_line_purify(string):
    return string
'''
purify array: lower and delete useless symbols
'''
def array_purify(array):
    for line in range(len(array)):
        array[line] = [string_purify(string) for string in array[line]]
    return array


def string_purify(string):
    string = str(string).lower()
    for symbols_delete in USELESS_SYMBOLS:
        string = string.replace(symbols_delete, '')
    return string

array = preprocess_user(parsing('task.xlsx')[0])
for i in range(5):
    print(array[i])
