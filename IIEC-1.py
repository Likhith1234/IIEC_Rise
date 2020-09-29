#! /usr/bin/python3

print("content-type: text/html")
print()

import speech_recognition as sr
import subprocess as sp
import pyttsx3 as p

print("Welcome sir! This is Hero")
p.speak("Welcome sir! This is Hero")
print("How can i help you sir?")
p.speak("How can i help you sir?")
r = sr.Recognizer()
response = True
while response:
    with sr.Microphone() as source:
        print("---Speak Now---")
        r.adjust_for_ambient_noise(source)
        audio = r.record(source, 10)
        print("---Audio Recorded---")

    try:
        data = r.recognize_google(audio)
        print("Your request: ",data)

        if ("what is your name" in data) or ("what's your name" in data) or ("who are you" in data):
            p.speak("This is Hero your voice assisstant")
        elif ("bye" in data) or ("thank" in data):
            print("bye")
            p.speak("It's my pleasure sir! Have a great day")
            response = False
        elif ("how are you" in data):
            p.speak("I am good sir")
        elif ("cal" in data) and (
                ("show" in data) or ("open" in data) or ("run" in data) or ("execute" in data)):
            res = sp.getoutput("cal")
            print(res)
        elif ("date" in data) and (("show" in data) or ("open" in data) or ("run" in data) or ("execute" in data)):
            res = sp.getoutput("date")
            print(res)
        elif ("clock" in data) and (("show" in data) or ("open" in data) or ("run" in data) or ("execute" in data)):
            res = sp.getoutput("while true; do echo -en `date +%T``sleep 1`\"\\b\\b\\b\\b\\b\\b\\b\\b\" ; done &")
            print(res)
        elif ("day" in data) and (("show" in data) or ("open" in data) or ("run" in data) or ("execute" in data)):
            res = sp.getoutput("date +%A")
            print(res)
        elif ("month" in data) and (("show" in data) or ("open" in data) or ("run" in data) or ("execute" in data)):
            res = sp.getoutput("date +%B")
            print(res)
        elif ("time" in data) and (("show" in data) or ("open" in data) or ("run" in data) or ("execute" in data)):
            res = sp.getoutput("date +%T")
            print(res)
        elif ("cal" in data) and ("this year") and (
                ("show" in data) or ("open" in data) or ("run" in data) or ("execute" in data)):
            res = sp.getoutput("cal -y")
            print(res)
        else:
            print("Invalid")
            p.speak("Sorry Sir! I don't understand what you said")
    except Exception:
        p.speak("Sorry Sir! I can't get you")