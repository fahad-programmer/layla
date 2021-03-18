import random
import json
import pickle
import numpy as np
import nltk
import os
from nltk.stem import WordNetLemmatizer
from layla.engine_components import take_command
from tensorflow.keras.models import load_model

from work.work import *
from WebScraping.googledata import google_results

from _Core_Components_Cpp.cpp_func import *

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('layla/basic-comands.json', encoding="utf8").read())

words = pickle.load(open('layla/words.pkl', 'rb'))
classes = pickle.load(open('layla/classes.pkl', 'rb'))
model = load_model('layla/layla_model.h5')


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list


def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            return result


"""
This is a basic code...
everything will be working inside the work folder
we will just import work.py function in this while loop
"""

def layla_run():
    # os.system('cls')

    WAKE = 'hey layla'

    # This Function will clean any
    # command before execution of this python file
    wish_me()
    while True:        # For Test
        # query = take_command().lower()
        query = input("Enter >> ").lower()
        
        if query == WAKE:
            query = input("Enter >> ").lower()

            ints = predict_class(query)
            res = get_response(ints, intents)
            # answer = google_results(query)
            try:
                eval(res)
            except Exception as e:
                speak(res)

        else:
            pass