from sklearn.feature_extraction.text import TfidfVectorizer
import pymorphy3
import re

_g_key_words_amount = 3000
_g_morph = pymorphy3.MorphAnalyzer()

def to_key_words(questions : list[list[str]]) -> list[list[str]]:
    questions = lemmatise_questions(questions)
    all_kwords = get_all_keywords(questions, _g_key_words_amount)
    for question in questions:  # removing all words, except for keywords
        for i in range(len(question)):
            this_answer_kwords = []
            for word in question[i]:
                if word in all_kwords:
                    this_answer_kwords.append(word)
            question[i] = this_answer_kwords
    return questions

def get_all_keywords(questions : list[list[str]], amount) -> set[str]:
    all_answers = []    # geting a list of all words
    for question in questions:
        all_answers.extend(question)
    all_words = []
    for word in all_answers:
        all_words.extend(word)
    vectorizer = TfidfVectorizer()  # finding keywords by frequency
    vector = vectorizer.fit_transform(all_words)
    feature_names = vectorizer.get_feature_names_out()
    keywords = [feature_names[i] for i in vector.toarray().argsort()[0][-amount:]] 
    return set(keywords)

def lemmatize_string(text : str) -> list[str]:
    words = re.findall(r'\w+', text)
    res = list()
    for word in words:
        p = _g_morph.parse(word)[0]
        res.append(p.normal_form)
    return res

def lemmatise_questions(questions : list[list[str]]) -> list[list[str]]:
    for question in questions:
        for i in range(len(question)):
            question[i] = lemmatize_string(question[i])
    return questions