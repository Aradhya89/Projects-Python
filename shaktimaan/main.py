import speech_recognition as sr
import webbrowser as web
import pyttsx3
import pygame 
import sys
from listoflist import *
# import openai
# import dotenv
# import os


# dotenv.load_dotenv() # to add api key in env to os.env
# openaiapi = os.environ.get("openai_api")
# client = openai.OpenAI(api_key= openaiapi)

#initializing module

recogniser = sr.Recognizer()
tt = pyttsx3.init()
pygame.mixer.init()

#command for woman voice 0 for man, 1 for woman
def voicechange(x):
    voices = tt.getProperty("voices")
    tt.setProperty('voice',voices[x].id)   


tt.say("initializing shaktimaan")
tt.runAndWait()

if __name__ == "__main__": #writig this so it will not work after importing on other

    while True:
        #code for getting waking sound command
        with sr.Microphone() as source:
            print("\nsay shaktimaan to activate.")

            try:
                entry = recogniser.listen(source,timeout= 2,phrase_time_limit=2)
                print("recognizing...")
            except sr.exceptions.WaitTimeoutError:
                continue

        try:
            #code for waking up saktimaan
            if (recogniser.recognize_google(entry).lower()) == "shaktiman":
                pygame.mixer.Sound("shaktimaan/sfx/game-start-317318.mp3").play()
                print("\nshaktiman is listening")
                
                with sr.Microphone() as source:
                    audio = recogniser.listen(source)
                    print("saktimaan is processing the text")
                try:
                    print("\nyou said :",a:= recogniser.recognize_google(audio))
                    if 'open' in a.lower():
                    # checking any link word are in sentence if yes then opening it
                        for b in list(linklist.keys()):
                            if b in a.lower() :
                                web.open(linklist[b])
                                pygame.mixer.Sound("shaktimaan/sfx/okkk.mp3").play()
                                break
                    if 'play' in a.lower():
                        for b in list(musiclist.keys()):
                            if b in a.lower() :
                                web.open(musiclist[b])
                                pygame.mixer.Sound("shaktimaan/sfx/okkk.mp3").play()
                                break
                        
                    
                    #command for exiting while loop
                    if a.lower() == "system shutdown" :
                        sys.exit()
                    else :...
                        # try:
                        #     client.chat.completions.create(model= "gpt-3.5-turbo",
                        #         messages= [{'role':"system","content":"your are a ai system of automated project like jarvis"},
                        #         {"role":"user","content":"what is the weather"}])
                        # except:
                        #     print("LIMIT EXCEED")
                        
                    

                    
                    
                    
                except (sr.UnknownValueError , sr.RequestError):
                    print("not able to understand")  

        except (sr.UnknownValueError , sr.RequestError):
            print("not able to understand")
            #when audio recorder not get proper sentence

        except ConnectionResetError:   #making sure system is connected to internet
            print("connect to the internet")
            sys.exit()