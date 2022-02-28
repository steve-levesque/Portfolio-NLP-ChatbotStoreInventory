import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import numpy as np
import random

import models.tensorflow_model as tfm
import models.huggingface_model as hfm
from utils import stemming, vectorization, dataset

# ===============================================
#  Global Variables
# ===============================================
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


# ===============================================
#  Flask Website Store CRUD
# ===============================================
def get_db_connection():
    print('DB connection in process...', flush=True)
    conn = sqlite3.connect('data/database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_item(post_id):
    conn = get_db_connection()
    item = conn.execute('SELECT * FROM inventory WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if item is None:
        abort(404)
    return item


@app.route('/')
def index():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM inventory').fetchall()
    conn.close()
    return render_template('index.html', items=items)


@app.route('/<int:item_id>')
def item(item_id):
    item = get_item(item_id)
    return render_template('item.html', item=item)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        item_count = request.form['item_count']
        title = request.form['title']
        description = request.form['description']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO inventory (item_count, title, description) VALUES (?, ?, ?)',
                         (item_count, title, description))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    item = get_item(id)

    if request.method == 'POST':
        item_count = request.form['item_count']
        title = request.form['title']
        description = request.form['description']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE inventory SET item_count = ?, title = ?, description = ?'
                         ' WHERE id = ?',
                         (item_count, title, description, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', item=item)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    item = get_item(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM inventory WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(item['title']))
    return redirect(url_for('index'))


# ===============================================
#  Chatbot and Flask Entry Point
# ===============================================
# Loading Stemming, Vectorization and labeling data created outside of web app.
data = dataset.load_json("intents-store_inventory")
words_stemmed, labels, train_X, train_y = dataset.load_pickle("data_chatbot")

# Tensorflow - model 1
model1 = tfm.tf_model_network(train_X, train_y)
tfm.tf_model_load(model1)

# HuggingFace - model 2
model2 = hfm.hf_distilbert_model_question_answering()


@app.route('/get_chatbot_res')
def get_bot_response():
    tol = 0.6
    message = request.args.get('msg')

    if message:
        # Model 1
        # Stemming -> Vectorization -> Neural Network
        stemmed_message = stemming.lancaster(message.lower())
        vectorized_words = vectorization.bag_of_words_compare(stemmed_message, words_stemmed)
        results = model1.predict([vectorized_words])[0]

        # Resulting tag and accuracy
        result_index = np.argmax(results)
        tag = labels[result_index]
        acc = results[result_index]

        if acc > tol:
            # If the user is asking for the inventory of an item.
            # We will use model 2 to amplify the accuracy.
            if tag == "available_items":
                # All items are fetched from the database and concatenated in a string.
                conn = get_db_connection()
                items = conn.execute('SELECT * FROM inventory').fetchall()
                conn.close()

                full_list = ""
                for item in items:
                    # print(item['item_count'], item['title'])
                    full_list = full_list + str(item['item_count']) + " " + item['title'] + ", "

                # print(full_list)

                # The model 2 will "ask" a question with the message to the full list of items.
                # This list could be a unstructured redacted text from another source.
                QA_input = {
                    'question': message,
                    'context': full_list
                }
                res = model2(QA_input)

                response = "Available item(s) count : " + res['answer'] + " [[" + str(res['score']) + "]]"

            # If the user is not asking for an item or in an imperative tone.
            # The data can be larger and have more generic use-cases.
            else:
                responses = "No response available from data given."

                for tg in data['intents']:
                    if tg['tag'] == tag:
                        responses = tg['responses']

                response = random.choice(responses)

        else:
            response = "I didn't quite get that, please try again. (Below tolerance : " + str(tol) + ")"

        full_res = str(response) + " [" + str(acc) + "]"
        print(full_res)
        return full_res

    return "Missing Data!"


if __name__ == "__main__":
    app.run()
