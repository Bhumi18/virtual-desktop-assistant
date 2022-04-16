from math import comb
import gtts
import speech_recognition as sr
import playsound
import random
from gtts import gTTS
import webbrowser
import ssl
import certifi
import time
import os
import subprocess
from PIL import Image
import pyautogui
import pyttsx3
import bs4 as bs
import urllib.request
import datetime

r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

class person:
    name = ''
    def setName(self, name):
        self.name = name
    
class assistant:
    name = ''
    def setName(self, name):
        self.name = name

def thereExists(terms):
    for term in terms:
        if term in voice_data:
            return True

def engineSpeak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

def recordAudio(ask=''):
    with sr.Microphone() as source:
        if ask:
            engineSpeak(ask)
        audio = r.listen(source, 5, 5)
        print('done listening')
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            engineSpeak('sorry sir i did not get that')
        except sr.RequestError:
            engineSpeak('sorry the server is down')
        print('>>', voice_data.lower())
        return voice_data.lower()

# def engineSpeak(audio_string):
#     audio_string = str(audio_string)
#     tts = gTTS(text=audio_string, lang='en')
#     r = random.randint(1, 20000000)
#     audio_file = 'audio'+str(r)+'.mp3'
#     tts.save(audio_file)
#     playsound.playsound(audio_file)
#     print(asis_obj.name+':', audio_string)
#     os.remove(audio_file)

def respond(voice_data):
    if thereExists(['hello','hi','hey']):
        # hour = int(datetime.datetime.now().hour)
        # if hour>=0 and hour<=12:
        #  engineSpeak('good morning')
        # elif hour>=12 and hour<=18:
        #     engineSpeak('goog afternoon')
        # else:
        #     engineSpeak('good evening')
        greetings = [person_obj.name+'how can i help you','please tell me how can i help you'+ person_obj.name]
        greet = greetings[random.randint(0 ,len(greetings)-1)]
        engineSpeak(greet)

    if thereExists(['what is your name','tell me your name']):
        if person_obj.name:
            engineSpeak('what is with my name')
        else:
            engineSpeak('i do not know my name , please give my name by saying command your name should be,,,,,,,,what is your name')
    
    if thereExists(['my name is']):
        person_name = voice_data.split('is')[-1].strip()
        engineSpeak('okay i will rembember that your name is '+person_name)
        person_obj.setName(person_name)

    if thereExists(['your name should be']):
        asis_name = voice_data.split('be')[-1].strip()
        engineSpeak('okay i will rembember that my name is '+asis_name)
        asis_obj.setName(asis_name)
    
    if thereExists(['how are you','how rae you doing']):
        engineSpeak('i am very well thanks for asking'+person_obj.name)
    
    if thereExists(['what is the time','tell the time']):
        time = datetime.datetime.now().strftime('%H:%M:%S')
        engineSpeak(f'{person_obj.name} , the time is {time}')
    
    if thereExists(['search for']) and 'youtube' not in voice_data:
        search_term = voice_data.split('for')[-1]
        url = 'https://google.com/search?q='+search_term
        webbrowser.get().open(url)
        engineSpeak('here is what i found for'+search_term+'on goole')
    
    if thereExists(['youtube']):
        search_term = voice_data.split('for')[-1]
        url = 'https://www.youtube.com/results?search_query='+search_term
        webbrowser.get().open(url)
        engineSpeak('here is what i found for '+search_term+'on youtube')

    if thereExists(['price of']):
        search_term = voice_data.split('for')[-1]
        url = 'https://google.com/search?q='+search_term
        webbrowser.get().open(url)
        engineSpeak('here is what i found for'+search_term+'on google')

    if thereExists(['play music']):
        search_term = voice_data.split('for')[-1]
        url = 'https://open.spotify.com/search/'+search_term
        webbrowser.get().open(url)
        engineSpeak('you are listening to'+search_term+'enjoy sir')

    if thereExists(['amazon.com']):
        search_term = voice_data.split('for')[-1]
        url = 'https://www.amazon.in'+search_term
        webbrowser.get().open(url)
        engineSpeak('here is what i found for'+search_term+'on amazon.com')
    
    if thereExists(['make a note']):
        search_term = voice_data.split('for')[-1]
        url = 'https://keep.google.com/#home'
        webbrowser.get().open(url)
        engineSpeak('here you can make notes')
    
    if thereExists(['open instagram','want to have some fun time']):
        search_term = voice_data.split('for')[-1]
        url = 'https://www.instagram.com/'
        webbrowser.get().open(url)
        engineSpeak('opening instagram')
    
    if thereExists(['open twitter']):
        search_term = voice_data.split('for')[-1]
        url = 'https://twitter.com/'
        webbrowser.get().open(url)
        engineSpeak('opening twitter')
    
    if thereExists(['show my time table']):
        image = Image.open(r'timetable.jpg')
        image.show()
    
    if thereExists(['weather','tell me the weather report','what is the condition outside']):
        search_term = voice_data.split('for')[-1]
        url = 'https://www.google.com/search?q=weather+report&rlz=1C1VDKB_enIN979IN979&oq=wea&aqs=chrome.0.69i59l2j0i131i433i512j69i57j0i512j0i131i433i512j0i433i457i512j0i402l2j0i512.2272j0j7&sourceid=chrome&ie=UTF-8'
        webbrowser.get().open(url)
        engineSpeak('here what is i found for on google')
    
    if thereExists(['open my gmail','check my email']):
        search_term = voice_data.split('for')[-1]
        url = 'https://mail.google.com/mail/u/0/#inbox'
        webbrowser.get().open(url)
        engineSpeak('here you can check your gmail')

    if thereExists(['game']):
        voice_data = recordAudio('choose among rock paper scissor')
        moves = ['rock','paper','scissor']
        cmove = random.choice(moves)
        pmove = voice_data
        engineSpeak('the computer choose '+cmove)
        engineSpeak('you choose'+pmove)

        if pmove==cmove:
            engineSpeak('the match is draw')
        elif pmove=='rock' and cmove=='paper':
            engineSpeak('computer wins')
        elif pmove=='rock' and cmove=='scissor':
            engineSpeak('player wins')
        elif pmove=='paper'and cmove=='scissor':
            engineSpeak('computer wins')
        elif pmove=='paper'and cmove=='rock':
            engineSpeak('player wins')
        elif pmove=='scissor' and cmove=='rock':
            engineSpeak('computer wins')
        elif pmove=='scissor' and cmove=='paper':
            engineSpeak('player wins')

    if thereExists(['toss','flip','coin']):
        moves = ['head','tails']
        cmove = random.choice(moves)
        engineSpeak('the computer choose'+cmove)

    if thereExists(['plus','minus','multiply','divide','power','+','-','*','/']):
        operation = voice_data.split()[1]

        if operation =='+':
            engineSpeak(int(voice_data.split()[0])+int(voice_data.split()[2]))
        elif operation =='-':
            engineSpeak(int(voice_data.split()[0])-int(voice_data.split()[2]))
        elif operation =='*':
            engineSpeak(int(voice_data.split()[0])*int(voice_data.split()[2]))
        elif operation =='/':
            engineSpeak(int(voice_data.split()[0])/int(voice_data.split()[2]))
        elif operation =='power':
            engineSpeak(int(voice_data.split()[0])**int(voice_data.split()[2]))
        else:
            engineSpeak('wrong operator')

    if thereExists(['capture','screenshot','my screen']):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('D://Youtube Projects//Desktop Voice Assistant')

    if thereExists(['exit','quit','good bye']):
        engineSpeak('bye ...have a good day')
        exit()

time.sleep(1)

asis_obj = assistant()
person_obj = person()
asis_obj.name = 'Siri'
while (1):
    voice_data = recordAudio('recording')
    print('done')
    print('you said : ', voice_data)
    respond(voice_data)


        

