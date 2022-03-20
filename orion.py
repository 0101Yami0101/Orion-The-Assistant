#Orion

import pyttsx3
import datetime
import speech_recognition as sr 
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio) 
    engine.runAndWait() 

def wishme():

   hour = int(datetime.datetime.now().hour)
   
   if hour>=0 and hour<12:
       speak(f"Good Morning, I am Orion. How may I help You? ")
   elif hour>=12 and hour<18:
       speak(f"Good afternoon, I am Orion. How may I help You? ")
   else:
        speak(f"Good Evening, I am Orion. How may I help You? ")

  
def takeCommand():
    # '''Takes input from user using microphone'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising....")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query} " )

    except Exception as e:
        print(e)
        print("Please say that again...")
    return query


if __name__=="__main__":
    wishme()

    #logic
    while True:
        query = takeCommand().lower()
        if "how are you" in query:
            speak("I am fine sir.. How are You today?")
        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com/')
        elif 'On Chrome' in query:
            webbrowser.open(f"google.com {query}")
        elif 'open marketplace'  in query:
            speak(f"Opening Marketplace on Chrome ")
            webbrowser.open('https://marketplace.axieinfinity.com')  
        elif 'open card explorer' in query:
            webbrowser.open('https://www.axieworld.com/en/tools/cards-explorer')
        elif 'time' in query:

            hour = int(datetime.datetime.now().hour)
            minute = int(datetime.datetime.now().minute) 
            if hour>=0 and hour<12:
                speak(f"The time is {hour}AM and {minute} minutes ")
            else:
                speak(f"The time is {hour}PM and {minute} minutes ")
        elif 'open game' in query:
            path = "C:\\Users\\Sonit\\Desktop\\Games\\VALORANT"
            os.startfile(path)
 
        
