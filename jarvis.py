import audioop
from math import trunc
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib  



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak('good morning')
    elif hour>=12 and hour<=18:
        speak('goog afternoon')
    else:
        speak('good evening')
    speak('i am siri please tell me how may i help you')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('recognizing')
        query = r.recognize_google(audio, language="en-IN")
        #print(f'you said : {query} \n')
    except Exception as e:
        print(e)
        print('please say that again')
        return "none"
    return query    

# def sendEmail(to , content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login('youremail@gmail.com', 'password')
#     server.sendmail('youemail@gmail.com', to, content)
#     server.close()

    

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak("according to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            num = random.randint(0,1)
            file_name = music_dir+'\\'+songs[num]
            os.startfile(file_name)
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'bhumi , the time is {time}')
        elif 'open code' in query:
            code_path = "C:\\Users\\Bhumi Sadaria\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        # elif 'email to bhumi' in query:
        #     try:
        #         speak('what should i say')
        #         content = takeCommand()
        #         to = 'bhumiyouremail@gmail.com'
        #         sendEmail(to, content)
        #         speak('email has been sent')
        #     except Exception as e:
        #         print(e)
        #         speak('sorry i am not able to send email')
        elif 'exit' in query:
            speak('by      bhumi i love you please miss me')
            exit()