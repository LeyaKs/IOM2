from keywords import to_key_words
from parsing import parsing
from preproccess import preprocess

parsing_res = parsing("test.xlsx")
prep_res = preprocess(parsing_res)
keywords_res = to_key_words(prep_res)
print(keywords_res)