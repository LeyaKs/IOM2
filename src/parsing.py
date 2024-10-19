import openpyxl
def parsing(file_name):
    wb = openpyxl.load_workbook(file_name)
    result = []
    index = 0
    for sheet in wb:        # iterating through pages of the file
        answers = []        # list of answers for each interviewee
        check_first_row = 1 # flag variable
        for row in sheet.iter_rows(values_only=True):   # iteraring through rows on each page
            if (check_first_row == 1):
                check_first_row = 0
                continue
            answers.append(list(row))   # adding an answer to the list
        result.append(answers)  # adding answers to the resulting list
    return result