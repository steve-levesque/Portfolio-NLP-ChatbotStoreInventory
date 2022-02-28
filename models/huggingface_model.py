from transformers import pipeline


def hf_distilbert_model_question_answering():
    model_name = "distilbert-base-uncased-distilled-squad"
    model = pipeline('question-answering', model=model_name, tokenizer=model_name)
    return model
