import numpy as np


def bag_of_words_compare(stemmed_words, corpus_words):
    bag = [0 for _ in range(len(corpus_words))]

    for se in stemmed_words:
        for i, w in enumerate(corpus_words):
            if w == se:
                bag[i] = 1

    return np.array(bag)


def bag_of_words_Xy(words, labels, docs_x, docs_y):
    train_X = []
    train_y = []

    out_empty = [0 for _ in range(len(labels))]
    for idx, doc in enumerate(docs_x):
        bag = []

        for w in words:
            if w in doc:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[idx])] = 1
        train_X.append(bag)
        train_y.append(output_row)

    train_X = np.array(train_X)
    train_y = np.array(train_y)

    return train_X, train_y
