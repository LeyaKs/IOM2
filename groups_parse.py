import re

def parse_groups_file(file_path):
    parsed_data = {}
    with open(file_path, "r", encoding="utf-8") as file:
       text = file.read()
       pattern = r"(.+): (.+)"
       for match in re.findall(pattern, text):
          category, words_string = match
          words = words_string.split(", ")
          parsed_data[category] = words
    return parsed_data

def main():
    file_path = "./resources/group-1.txt"
    parsed_data = parse_groups_file(file_path)
    print(parsed_data)

if __name__ == "__main__":
   main()
