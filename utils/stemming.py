import nltk
from nltk.stem.lancaster import LancasterStemmer


def lancaster(s):
    stemmer = LancasterStemmer()
    s_words = nltk.word_tokenize(s)
    stemmed_words = [stemmer.stem(w.lower()) for w in s_words if w not in "?"]

    return stemmed_words
