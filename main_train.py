import models.tensorflow_model as tfm
from utils import vectorization, text_processing, dataset


data = dataset.load_json("intents-store_inventory", path="../data/")

words, labels, docs_x, docs_y = text_processing.init_data_stemmed(data)
train_X, train_y = vectorization.bag_of_words_Xy(words, labels, docs_x, docs_y)

dataset.save_pickle(words, labels, train_X, train_y, filename="data_chatbot", path="../data/")

model = tfm.tf_model_network(train_X, train_y)
tfm.tf_model_save(model, train_X, train_y)
