import json
import pickle


def load_json(filename, path="data/"):
    with open(path + filename + ".json") as file:
        return json.load(file)


def save_pickle(words, labels, train_X, train_y, filename="data", path="data/"):
    with open(path + filename + ".pickle", "wb") as file:
        pickle.dump((words, labels, train_X, train_y), file)


def load_pickle(filename, path="data/"):
    with open(path + filename + ".pickle", "rb") as file:
        words, labels, train_X, train_y = pickle.load(file)
        return words, labels, train_X, train_y
