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