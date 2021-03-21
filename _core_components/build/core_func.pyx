from nltk.stem import WordNetLemmatizer
import nltk
import numpy as np
cimport numpy
import pickle
from tensorflow.keras.models import load_model
import random
import os
import json
from work.work import *
from WebScraping.googledata import google_results
from layla.engine_components import take_command
from _Core_Components_Cpp.cpp_func import *



classes = pickle.load(open('layla/classes.pkl', 'rb'))

words = pickle.load(open('layla/words.pkl', 'rb'))
model = load_model('layla/layla_model.h5')

intents = json.loads(open('layla/basic-comands.json', encoding="utf8").read())

lemmatizer = WordNetLemmatizer()

cpdef list clean_up_sentence(str sentence):
	cdef list sentence_word = nltk.word_tokenize(sentence)
	cdef list sentence_words = [lemmatizer.lemmatize(word) for word in sentence_word]
	return sentence_words

cpdef numpy.ndarray bag_of_words(str sentence):
	cdef list sentence_words = clean_up_sentence(sentence)
	cdef list bag = [0] * len(words)
	for w in sentence_words:
		for i, word in enumerate(words):
			if word == w:
				bag[i] = 1
	return np.array(bag)


cdef lambda_replc(x):
		return x[1]

cpdef list predict_class(str sentence):
	cdef numpy.ndarray bow = bag_of_words(sentence)
	res = model.predict(np.array([bow]))[0]
	cdef float ERROR_THRESHOLD = 0.25
	cdef list results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
	results.sort(key=lambda_replc, reverse=True)
	cdef list return_list = []
	for r in results:
		return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
	return return_list

cpdef str get_response(list intents_list, intents_json):
	cdef str tag = intents_list[0]['intent']
	cdef list list_of_intents = intents_json['intents']
	cdef str result
	for i in list_of_intents:
		if i['tag'] == tag:
			result = random.choice(i['responses'])
			return result

cpdef void layla_run():
	os.system('cls')
	while True:
		query = input("Enter >> ").lower()
		

		ints = predict_class(query)
		res = get_response(ints, intents)

		try:
			eval(res)
		except Exception as e:
			speak(res)
			print(res)
