import time
import pyautogui
import pyjokes
import pyttsx3
import requests
from bs4 import BeautifulSoup
from time import sleep
from datetime import timedelta
from datetime import datetime
import speech_recognition as sr
from pywikihow import search_wikihow
from whatsapp import get_message
import datetime
import os
import cv2
from Demos.FileSecurityTest import permissions
from flask import request
from numpy.random.mtrand import operator
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import psutil
import speedtest
import PyPDF2
from PyPDF2 import PdfReader
# import json
# from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
        r= sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.....")
            r.pause_threshold = 1
            audio=r.listen(source,timeout=1,phrase_time_limit=5)
        try:
                print("Recongnizing.....")
                query = r.recognize_google(audio, language='en-in')
                print(f"user said:{query}\n")
        except Exception as e:
            print("Say that again please")
            return "none"
        return query

def wish():
    hour = int(datetime.datetime.now().hour)
    tt=time.strftime("%I:%M %p")
    if hour>=0 and hour<=12:
        speak(f"Good Morning ,its {tt}")
    elif hour>12 and hour<16:
        speak(f"Good Afternoon ,its {tt}")
    else:
        speak(f"Good Evening ,its {tt}")

def sendEmail(emai,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('thekingff134@gmail.com','qygn baes zvhn hwyo')
    server.sendmail('thekingff134@gmail.com',emai,content)
    server.close()

# def news():
#     main_url='http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=c2f99a6f612f49d1816557afba233ad6'
#     main_page=requests.get(main_url).json()
#     articles=main_page["articles"]
#     head=[]
#     day=["first","second","third","fourth","fifth","sixth","seventh","eighth","nineth","tenth"]
#     for ar in articles:
#         head.append(ar["title"])
#     for i in range (len(day)):
#         speak(f"today's {day[i]} news is: {head[i]}")

def pdfreader():
    reader = PdfReader("C:\\Users\\Jigar\\Desktop\\py3.pdf")
    number_of_pages = len(reader.pages)
    pg=int(input("Enter number of page i have to read"))
    page = reader.pages[pg]
    text = page.extract_text()
    speak(text)


strftime=int(datetime.datetime.now().strftime("%H"))
update=int((datetime.datetime.now()+timedelta(minutes=4)).strftime("%M"))
def get():
    speak("What message do you want to send")
    message=takecommand().lower()
    phone=input("Enter Receiver Phone number with country code(+91): ")
    kit.sendwhatmsg(phone, message, time_hour=strftime,time_min=update)


def taskexecution():
    wish()
    speak("this is jarvis . sir please tell me how may i help you")
    # takecommand()

    while True:
    # if 1:
        query = takecommand().lower()
        if "open xml" in query:
            npath="C:\\Users\\Jigar\\Desktop\\Exchanger XML Editor 3.3.exe"
            os.startfile(npath)


        elif "open command prompt" in query:
            os.system("start cmd")


        elif "open camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break;
                    cap.release()
                    cv2.destroyAllWindows()


        elif "ip address" in query:
            ip=get('https://api.ipify.org').text
            speak(f"Your ip address is {ip}")

        elif "developed" in query:
            speak("I am developed by Legend Harsh Shah")

        elif "wikipedia" in query:
            speak("Searching wikipedia.....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("accoring to wikipedia")
            speak(results)
            print(results)


        elif "open youtube" in query:
            speak("what should i search on youtube")
            cm=takecommand().lower()
            space=cm.replace(" ","")
            webbrowser.open(f"https://www.youtube.com/@{space}")



        elif "send message on whatsapp" in query:
            get()




        elif "play song on youtube" in query:
            speak("which song you want to listen")
            song=takecommand().lower()
            kit.playonyt(f"{song}")


        elif "send email" in query:
            try:
                speak("what message you want to send")
                content=takecommand().lower()
                speak("to whom you want to send message")
                emai=input("Input Receiver Email: ")
                # res=emai.replace(" ","")
                sendEmail(emai,content)
                speak("Email has been sent")


            except Exception as e:
                print(e)
                speak("sorry sir i am not able to send email")


        elif "you can sleep now" in query:
            speak("okay sir, i am going to sleep now you can call me anytime")
            break


        elif "tell me a joke" in query:
            joke=pyjokes.get_joke()
            speak(joke)


        elif "shutdown" in query:
            os.system("shutdown /s /t 5")
        elif "restart system" in query:
            os.system("shutdown /r /t 5")
        elif "sleep he system" in query:
            os.system("roundll32.exe powrprof.dll,SetSuspendState 0,1,0")


        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        # elif "tell me news" in query:
        #     speak("please wait sir, fetching the latest news")
        #     news()

        elif "how are you" in query or "how r u" in query:
            speak("i am fine sir, what about you")

        elif "i am great" in query or "i am also fine" in query:
            speak("that's great to hear from you")

        elif "reading" in query:
            pdfreader()

        elif "where i am" in query or "where we are" in query:
            speak("wait sir, let me check")
            try:
                ipAdd=requests.get('https://api.ipify.org').text
                print(ipAdd)
                url='https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests=requests.get(url)
                geo_data=geo_requests.json()
                city=geo_data['city']
                country=geo_data['country']
                speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("Sorry sir, Due to network issue i am not able to find where we are")
                pass

        elif "thank you" in query or "no thanks" in query:
            speak("It's my pleasure sir")

        elif "temperature" in query or "weather" in query:
            search = "temperature in ahmedabad"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")

        elif "activate how to do mode" in query:
            speak("how to do mode is activated")
            while True:
                speak("please tell me what you want to know")
                how=takecommand().lower()
                try:
                    if "exit" in how or "close" in how:
                        speak("ok sir, how to do mode is closed")
                        break
                    else:
                        max_results=1
                        how_to=search_wikihow(how,max_results)
                        assert len(how_to)==1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir, i am not able to find this")

        elif "how much power left" in query or "how much battery we have" in query or "battery" in query:
            battery=psutil.sensors_battery()
            percentage=battery.percent
            speak(f"sir our system have {percentage} percentage battery")

        elif "internet speed" in query:
            st=speedtest.Speedtest()
            dl=st.download()/1000000
            ul=st.upload()/1000000
            ds = f"{dl:.2f}"
            us = f"{ul:.2f}"
            speak(f"sir we have {ds} megabyte per second downloading speed and {us} megabyte per second uploading speed")

        elif "hide all files" in query or "hide this folder" in query or "visible this file" in query or "visible this folder" in query:
            speak("sir please tell me you want to hide this folder or make it visible for erveryone")
            condition=takecommand().lower()
            if "hide" in  condition:
                os.system("attrib +h /s /d")
                speak("sir, all the files in this folder are now hidden")
            elif "visible" in condition:
                os.system("attrib -h /s /d")
                speak("sir, all the files in this folder are now visible to everyone")
            elif "leave it" in condition or "leave for now" in condition:
                 speak("ok sir")







            # elif "do some calculation" in query or "can you calculate" in query:
            #     r=sr.Recognizer()
            #     with sr.Microphone() as source:
            #         speak("Say what you want to calculate, for example 3 plus 3")
            #         print("Listening.....")
            #         r.adjust_for_ambient_noise(source)
            #         audio=r.listen(source)
            #     my_string=r.recognize_google(audio)
            #     print(my_string)
            #
            #
            #     def get_operator_fn(op):
            #         return {
            #             '+': operator.add,
            #             '-': operator.sub,
            #             'x': operator.mul,
            #             'divided': operator.__truediv__,
            #         }[op]
            #
            #
            #     def eval_binary_expr(op1, oper, op2):
            #         op1, op2 = int(op1), int(op2)
            #         return get_operator_fn(oper)(op1, op2)
            #
            #
            #     speak("your result is:")
            #     speak(eval_binary_expr(*(my_string.split())))





        speak("sir do you have any other work")

if __name__ == "__main__":
     while True:
         permission=takecommand().lower()
         if "wake up" in permission:
             taskexecution()
         elif "goodbye" in permission or "good bye" in permission:
                speak("thanks for using me sir, and have a good day, and i developed by harsh shah")
                sys.exit()
