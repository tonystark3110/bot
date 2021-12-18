import speech_recognition as sr
import pyttsx3 as p
#from web_auto import *

r1=sr.Recognizer()
engine = p.init()
engine.say("hello")
engine.runAndWait()
with sr.Microphone () as source:
    r1.adjust_for_ambient_noise(source)
    print("hello!")
    audio = r1.listen(source)
    try:
         text = r1.recognize_google(audio)
         print(text)
    except sr.UnknownValueError:
        print("")
    except sr.RequestError as e:
        print("")


engine.say("how may i assist you?")
engine.runAndWait()
print("?")

r2 = sr.Recognizer()
with sr.Microphone() as source:
    r2.adjust_for_ambient_noise(source)
    audio = r2.listen(source)
    try:
        instruction = r2.recognize_google(audio)
        print(instruction)
    except sr.UnknownValueError:
        print("")
    except sr.RequestError as e:
        print("")

r3 = sr.Recognizer()
from web_automation import *
if "information" in instruction:
    engine.say("information about what")
    engine.runAndWait()
    with sr.Microphone() as source1:
        audio2=r3.listen(source1)
        try:
            information = r3.recognize_google(audio2)
            bot = info()
            bot.get_info(information)
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as e:
            print("")


r4 = sr.Recognizer()
from weather import *

if "weather" in instruction:
    engine.say("weather status of what?")
    engine.runAndWait()
    with sr.Microphone() as source1:
        audio3=r4.listen(source1)
        try:
            information1 = r4.recognize_google(audio3)
            bot = weather()
            bot.get_info(information1)
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as e:
            print("")

            
            

