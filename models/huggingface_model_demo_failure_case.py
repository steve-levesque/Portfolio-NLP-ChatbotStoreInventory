import json
from transformers import pipeline

model_name = "distilbert-base-uncased-distilled-squad"
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

with open("intents.json") as file:
    data = json.load(file)

disable_helper = True
input = "available computer"
current_best_score = 0
current_best_tag = None
current_best_answer = None

print(data['intents'])
for tag in data['intents']:
    print(tag)
    # The question on context model needs help by targeting the right category (tag).
    # Else, it will be biased with a result from a none pertinent tag with higher %.
    # Putting disable_helper to True will allow a check on all tags and the kernel will
    # fail respectively.
    if tag['tag'] == 'available_items' or disable_helper:
        for pattern in tag['responses']:
            QA_input = {
                'question': input,
                'context': pattern
            }
            res = nlp(QA_input)
            print(res)
            score = res['score']
            tag_name = tag['tag']
            print(tag)

            if current_best_score < score:
                current_best_score = score
                current_best_tag = tag_name
                current_best_answer = res['answer']

print(current_best_score)
print(current_best_tag)
print(current_best_answer)
