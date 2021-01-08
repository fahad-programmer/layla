import pyttsx3
import speech_recognition as sr
import datetime




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

# Below all code is copy pasted so it is going to change

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wish_me():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir !") 

	else:
		speak("Good Evening Sir !") 

	assname =("Jarvis 1 point o")
	speak("I am your Assistant")
	speak(assname)
	


def take_command():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...") 
		query = r.recognize(audio)
		print(f"User said: {query}\n")

	except Exception as e:
		print(e) 
		print("Unable to Recognize your voice.") 
		return "None"
	
	return query


