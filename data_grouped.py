from src.keywords import to_key_words
from src.parsing import parsing
from src.preproccess import preprocess
from src.translator import keywords_translate
from src.groups_parse import parse_groups_file
from src.grouping import group_keywords

def group(filename : str) -> list[dict[str, int]]:
    parsing_res = parsing(filename)
    prep_res = preprocess(parsing_res)
    keywords_res = to_key_words(prep_res)
    groups_parsed = parse_groups_file("./resources/group.txt")
    result = group_keywords(keywords_res, groups_parsed)
    return result