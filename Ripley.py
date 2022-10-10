import speech_recognition as sp
import pyttsx3
import datetime
import wikipedia 
import webbrowser
import pywhatkit

listener=sp.Recognizer()

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("Good Morning sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")
    elif hour>=18 and hour<24:
        speak("Good Evening sir!")
    else:
        speak("Goodnight sir!")
    speak("I am Ripley. Please tell me how can i help you sir")  

def give_command():
    try:
        with sp.Microphone() as source:
            print("listening...")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.replace('Ripley','')
            print(command)
    except:
        print("Unable to listen. Please say again sir.")
    return command

if __name__ == "__main__":
    greet()
    while True:
        query=give_command().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")            
            output = wikipedia.summary(query,2)
            print(output)
            speak(output)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play' in query:
            song=query.replace('play',' ')
            print("Playing" + song)
            speak('Playing' + song)
            pywhatkit.playonyt(song)

        elif 'time' in query:
            Time = datetime.datetime.now().strftime("%I:%M %p")   
            print(Time) 
            speak("Sir, the current time is" + Time)
        


