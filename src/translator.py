from deep_translator import GoogleTranslator

def keywords_translate(keywords : list[list[list[str]]]) -> list[list[list[str]]]:
    for question in keywords:
        for answer in question:
            for i in range(len(answer)):
                answer[i] = GoogleTranslator(source='auto', target='en').translate(answer[i])
    return keywords