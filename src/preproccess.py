USELESS_ANSWERS = ['да', 'нет']
def preprocess(array):      # prepross for user and hr
    array_ans = [[],[],[],[],[]]
    array_user = preprocess_user(array[0])
    array_hr = preprocess_hr(array[1])
    for i in range(5):
        if i != 4:
            length_user = len(array_user)
            for j in range(length_user):
                if array_user[j][i] != '' or any(word in array_user[j][i]
                 for word in USELESS_ANSWERS) and i == 0:
                    array_ans[i].append(array_user[j][i])
            
        length_hr = len(array_hr)
        for j in range(length_hr):
            if array_hr[j][i] != '' or any(word in array_hr[j][i] 
            for word in USELESS_ANSWERS) and i == 0:
                array_ans[i].append(array_hr[j][i])
            
    return array_ans


'''

'''
USER_SPECIAL_WORDS = ['тест', '-', 'none']
LEN_ACCESS = 5
QUESTION_STAY = 1       # index
QUESTION_RETURN = 2
def preprocess_user(array):
    array = array_purify(array)
    lines_count = len(array)
    columns_count = len(array[0]) if len(array) > 0 else 0
    for line in range(lines_count):
        array[line][0] = ' '.join([array[line][0], array[line][1]])     # merging 1 and 1.1 questions
        array[line].pop(1)
        array[line] = [user_line_purify(str(string), column, string_dlc)    # processing each line
        for string, column, string_dlc in string_unite(array[line], range(4))]
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
    if column == QUESTION_STAY or column == QUESTION_RETURN:  # duplication: numbers of questions in which the phrase can be described earlier
            string = string_dlc
    if len(string) < LEN_ACCESS:
        string = str(string)
        for word in string.split():                                # checking for trash
            if word in USER_SPECIAL_WORDS:
                string = ''
                break
    return string

'''

'''
HR_SPECIAL_WORDS = ['комментариев нет', 'без комментария', 'комментарий отсутствует']
def preprocess_hr(array):
    array = array_purify(array)
    lines_count = len(array)
    columns_count = len(array[0]) if len(array) > 0 else 0
    for line in range(lines_count):
        if any([word in array[line][3] for word in HR_SPECIAL_WORDS]):  # adding 1 question
            array[line].insert(0, 'желание сменить направление дейстельности')
        else:
            array[line].insert(0, '')
        for column in range(5):
            if any([word in array[line][column] for word in USER_SPECIAL_WORDS]):
                array[line][column] = ''
    return array

'''
purify array: lower and delete useless symbols
'''
def array_purify(array):
    for line in range(len(array)):
        array[line] = [string_purify(string) for string in array[line]]
    return array

USELESS_SYMBOLS = ['!', '@', '"', '#', '№', '$', ';', '%', '^', ':', 
'&', '?', '*', '(', ')', '-', '_', '+', '=', '\\', '|', '/', '\'', '[', ']', '{', '}', '.', '<', '>']
def string_purify(string):
    string = str(string).lower()
    for symbols_delete in USELESS_SYMBOLS:
        string = string.replace(symbols_delete, '')
    return string
