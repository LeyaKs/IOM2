import re

def parse_groups_file(file_path) -> dict[str, set[str]]: # txt keywords data parcer
    parsed_data = {}
    with open(file_path, "r", encoding="utf-8") as file:
       text = file.read()
       pattern = r"(.+): (.+)"
       for match in re.findall(pattern, text):
          category, words_string = match
          words = words_string.split(", ")
          parsed_data[category] = set(words)
    return parsed_data
