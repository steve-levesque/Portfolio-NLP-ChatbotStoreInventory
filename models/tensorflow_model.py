import tensorflow as tf
import tflearn


def tf_model_network(train_X, train_y):
    tf.compat.v1.reset_default_graph()

    net = tflearn.input_data(shape=[None, len(train_X[0])])
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, len(train_y[0]), activation="softmax")
    net = tflearn.regression(net)

    model = tflearn.DNN(net)

    return model


def tf_model_save(model, train_X, train_y, n_epoch=200, batch_size=4, verbose=True):
    model.fit(train_X, train_y, n_epoch=n_epoch, batch_size=batch_size, show_metric=verbose)
    model.save("model.tflearn")


def tf_model_load(model):
    model.load("models/model.tflearn")
