import speech_recognition as sr
import webbrowser as web
import pyttsx3
import pygame 
import sys
from listoflist import *
from google import genai
import os
import dotenv
import pyautogui as pi
# import openai



# for google api
dotenv.load_dotenv() # to add api key in env to os.env


#for openai 
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

def youtube_search(x:str):
    x = x.replace(" ","+")
    web.open(f"https://www.youtube.com/results?search_query={x}")


def genaibrain(a:str) -> str:
    with genai.Client(api_key=os.environ.get("GEMINI_API_KEY")) as client:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{a} in very short (like 15 words)",
            #writing this to reduce token usage
            config=genai.types.GenerateContentConfig(
                thinking_config=genai.types.ThinkingConfig(thinking_budget=0) # Disables thinking
            ),
        )
        return (response.text)
    
    # ai response with openai api

    # try:
    #     response = client.chat.completions.create(model= "gpt-3.5-turbo",
    #     messages= [{'role':"system","content":"your are a ai system of automated project like jarvis"},{"role":"user","content":"what is the weather"}])
    #     return response

    # except:
    #     print("LIMIT EXCEED")

    
def ytscroller():
    speak("activating youtube scroller")
    while True:
        with sr.Microphone() as mic:

            try:
                print("say command")  #-> FOR DEBBUGING 
                command = recogniser.listen(mic,timeout= 2,phrase_time_limit=2)
                # print("recognizing...") ->  FOR DEBBUGING 
            except sr.exceptions.WaitTimeoutError:
                # print("cant able to understand") ->  FOR DEBBUGING 
                continue
        try:
            print("you say :",a := recogniser.recognize_google(command).lower())# -> FOR DEBBUGING 
            if a == "scroll up":
                # pi.click(1550,458)
                pi.press("up")
            elif a == "scroll down":
                # pi.click(1550, 529) 
                pi.press("down")
            elif a == "video stop" or a == "video resume":
                # pi.press("space")
                pi.click(825,484)
            elif a == "exit":
                break
        except (sr.RequestError,sr.UnknownValueError):
            continue
        

def speak(a):
    tt.say(a)
    tt.runAndWait()

            
speak("initializing shaktimaan")

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
                pygame.mixer.Sound("Projects-Python/shaktimaan/sfx/game-start-317318.mp3").play()
                print("\nshaktiman is listening")
                
                with sr.Microphone() as source:
                    audio = recogniser.listen(source)
                    print("saktimaan is processing the text")
                try:
                    print("\nyou said :",a:= recogniser.recognize_google(audio))


                    # checking any link word are in sentence if yes then opening it
                    if 'open' in a.lower():
                        for b in list(linklist.keys()):
                            if b in a.lower() :
                                web.open(linklist[b])
                                pygame.mixer.Sound("Projects-Python/shaktimaan/sfx/okkk.mp3").play()
                                break
                            # else:
                            #     print("no link founded")
                            #     break


                    elif 'play' in a.lower():
                        for b in list(musiclist.keys()):
                            if b in a.lower() :
                                web.open(musiclist[b])
                                pygame.mixer.Sound("Projects-Python/shaktimaan/sfx/okkk.mp3").play()
                                break
                        
                    
                    #command for exiting while loop
                    elif a.lower() == "system shutdown" :
                        sys.exit()
                    
                    elif a.lower() == "youtube scroller":
                        ytscroller()

                    elif "youtube search" in a.lower():
                        search = a.lower().replace("youtube search","")
                        youtube_search(search)

                    else :
                        print(data :=genaibrain(a))

                        
                except (sr.UnknownValueError , sr.RequestError):
                    print("not able to understand")  

        except (sr.UnknownValueError , sr.RequestError):
            print("not able to understand")
            #when audio recorder not get proper sentence

        except ConnectionResetError:   #making sure system is connected to internet
            print("connect to the internet")
            sys.exit()