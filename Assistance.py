#pyttsx3 library which convert the text  into speech
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import smtplib

#sapi5 is microsoft  speech engine which are inbuilt voices in windows
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<=17:
        speak("Good Afternnon Sir")
    elif hour>=17 and hour<=19:
        speak("Good Evening Sir")
    else:
        speak("Good Night Sir")

    speak("I am zira sir, please tell me how may i help you")


def takeCommand():
    #It takes microphone input from the user and return the string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        r.recognize_google(audio, key=None, language="en-in", show_all=False)
    except Exception as e:
        print("Say again please...")
        return "None"
    return query

def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    #ehlo-Identify yourself to an ESMTP server using EHLO
    server.ehlo()
    #starttls-Put the SMTP connection in TLS (Transport Layer Security) mode.
    # All SMTP commands that follow will be encrypted.
    server.starttls()
    server.login('ag027238@gmail.com','qwerty@123')
    server.sendmail('ag027238@gmail.com', to, content)
    server.close()

if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()

    # Logic for executing tasks based on query
        if 'wikipedia' in query:
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            print(strTime)   
            speak(f"Sir, the time is {strTime}")
        
        elif 'email to ankit' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to="ankitgupta8292@gmail.com"
                sendemail(to,content)
                speak("Congratulation Sir, Email has been sent!")

            except Exception as e:
                speak("Sorry sir, Email does not send to this email ")

        elif 'play music' in query:
            music_dir = 'G:\\Video'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'quit the program' in query:
            speak("Okay sir as you want")
            exit()