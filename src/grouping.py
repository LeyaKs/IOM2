def group_keywords(data_to_group : list[list[str]], grouped_keywords : dict[str, set[str]]) -> list[dict[str, int]]:
    result = list()
    for question in data_to_group:      # groups all the keywords using info grom grouped_keywords dictionary, counts each group frequencies
        result_for_question = dict()
        for answer in question:
            for word in answer:
                for group_name in grouped_keywords:
                    if(word == group_name or word in grouped_keywords[group_name]):
                        if(group_name in result_for_question):
                            result_for_question[group_name] += 1
                        else:
                            result_for_question[group_name] = 0
        result.append(result_for_question)
    return result
