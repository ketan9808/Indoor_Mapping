import pyttsx3

class speak:
    def __init__(self, ):
        # one time initialization
        self._engine = pyttsx3.init()
        
    def speak(data):        
        # set the properties
        engine.setProperty('rate', 150) # speed percentalge
        engine.setProperty('volume',0.5) # volume 0-1
        engine.setProperty('voice', )
        #queue up things to say
        engine.say(data)
        
        # flush thesay() queue and play the audio
        engine.runAndWait()
        
    def available_voices():
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        for voice in voices:
            print('id: ', voice.id)
            print('name: ', voice.name)
            print('languages: ', voice.languages)
            print('gender: ', voice.gender)
            print('age: ', voice.age)