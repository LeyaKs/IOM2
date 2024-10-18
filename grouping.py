def group_keywords(data_to_group : list[list[str]], grouped_keywords : dict[str, set[str]]) -> dict[str, int]:
    result = dict()
    for question in data_to_group:
        for answer in question:
            for word in answer:
                for group_name in grouped_keywords:
                    if(word == group_name or word in grouped_keywords[group_name]):
                        if(word in result):
                            result[word] += 1
                        else:
                            result[word] = 0
    return result
