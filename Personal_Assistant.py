import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def WishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good AfterNoon!")
    else:
        speak("Good Evening!")
        
    speak("I am jarvis! What can I help you with?")
 
def takeCommand():
    #takes microphone input from user and returns string output
    r= sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = "en-US")
        #print("you said: -  " + r.recognize_google(audio, language = "en-US"))
        #response = json.dumps(sFinalResult, ensure_ascii=False).encode('utf8')
        print("User said:", query)
    except Exception as e:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return query
    
def sendMail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('poonamvashist1@gmail.com', 'mathematics56')
    server.sendmail('poonamvashist1@gmail.com',to, content)
    server.close()
    
    
    
if __name__=='__main__':
    WishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        if 'open youtube' in query:
            webbrowser.open('https://www.youtube.com')
            #webbrowser.open('nabinkhadka.com.np', new = 2)
        if 'open google' in query:
            webbrowser.open('https://www.google.com')
        if 'mail' in query:
            webbrowser.open('https://www.gmail.com')
        if 'play music' in query:
            speak("playing Music")
            music_dir = 'D:\\Music'
            songs = os.listdir (music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        if 'time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak("The time is, %s!" % str_time)
        if 'send mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sakshijain9510@gmail.com"
                sendMail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Couldn't send the mail !")
        if 'how are you' in query:
            print("I am well. Thank You !")
            speak("I am well. Thank You ! ")
            
        
