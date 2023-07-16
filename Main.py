#from black import main
import pyttsx3
from zmq import device
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
#print(voices[0].id)
engine.setProperty('voices',voices[1].id)
engine.setProperty('rate',165)

def Speak(audio):
    print("    ")
    print(f":  {audio}")
    print("    ")
    engine.say(audio)
    engine.runAndWait()


Speak("Hello Sir, How are you?")
def takecommand():

    r = sr.Recognizer()
    
    with sr.Microphone(device_index=0) as source:
        print("Listening...")
        r.pause_threshold =1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"Your Command: {query}\n") 

    except Exception as e:
       # print(e)    
        print("Say that again please...")  
        return "None" 
    return query