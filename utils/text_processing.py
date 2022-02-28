from utils import stemming


def init_data_stemmed(data):
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data['intents']:
        for pattern in intent['patterns']:
            stemmed_words = stemming.lancaster(pattern.lower())
            words.extend(stemmed_words)
            docs_x.append(stemmed_words)
            docs_y.append(intent['tag'])

        if intent['tag'] not in labels:
            labels.append(intent['tag'])

    words = sorted(list(set(words)))
    labels = sorted(labels)

    return words, labels, docs_x, docs_y
