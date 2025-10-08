
import pyautogui as pi 
import speech_recognition as sr 

recogniser = sr.Recognizer()

#TO GET THE POSITION OF CURSOR
# while True:
#     x,y = pi.position()
#     print(x,y)
#     if x== 1599 and y == 0:
#         exit()
while True:
    with sr.Microphone() as mic:
        try:
            # print("say anything")  -> FOR DEBBUGING 
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

