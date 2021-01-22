import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')

for voice in voices:
	print(voice.name)

