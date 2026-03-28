import speech_recognition as sr 
import setuptools
import webbrowser
import pyttsx3
import cohere
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("MY_API_KEY")

recognizer = sr.Recognizer()

music = {
    "flight" : "https://youtu.be/RgCZpGwjIUc?si=zCJ7WaQMfv0s7AOI",
    "purple" : "https://youtu.be/6oAbrKhvf7M?si=ilFf66y5P0xwO9zE",
    "companion" : "https://youtu.be/PKIYJAhHY6M?si=bsSifcWHS5HEPSzS",
    "high" : "https://youtu.be/gI1Z4UHg9o0?si=j-QU5NiQnMu_GcDd",
    "again" : "https://youtu.be/ulsnTa0gu4Q?si=xqpe8VRQ4GtahnSv",
    "mirror" : "https://youtu.be/QFMtWOwn670?si=P9W_wuuNl3h2kfYD",
    "four" : "https://youtu.be/UcU-yRIZ5DE?si=OH5Q3KV_OJAvWgfB",
    "minutes" : "https://youtu.be/shgTmiWAuHI?si=PMaa2lFZkr0pZZBw",
    "you" : "https://youtu.be/shgTmiWAuHI?si=PMaa2lFZkr0pZZBw",
    "lock" : "https://youtu.be/BhZnk8egLI0?si=_GCsCNDnVzHimVX_",
    "kitty" : "https://youtu.be/wisJXAT_8sg?si=ACl6kixZ9Uppzttq",
    "fucker" : "https://youtu.be/Fbv6-50S1lc?si=emH5cKAyGm2Sddb7"

}


def speak(text) :
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def aiprocess(command) :
    print("Gathering information...")
    speak("Gathering information...")

    co = cohere.Client(api_key)

    response = co.chat(
    message=f"{command} explain shortly as short as u can",
    preamble="You are a virtual assistant named jarvis skilled in general tasks like alexa and google cloud and answer the question as short as you can"
)
    
    print(response.text)
    speak(response.text)
    

def processCommand(c) :
    if "open google" in c.lower() :
        webbrowser.open("https://google.com")
        speak("opening google")
    elif "open youtube" in c.lower() :
        webbrowser.open("https://www.youtube.com/")
        speak("opening youtube")
    elif "open whatsapp" in c.lower() :
        webbrowser.open("https://web.whatsapp.com/")
        speak("opening whatsapp")
    elif "open facebook" in c.lower() :
        webbrowser.open("https://www.instagram.com/")
        speak("opening facebook")
    elif "open instagram" in c.lower() :
        webbrowser.open("https://www.facebook.com/")
        speak("opening instagram")
    elif c.lower().startswith("play") :
        song = c.lower().split(" ")[1]
        link = music[song]
        webbrowser.open(link)
        speak(f"playing {song}")
    elif "open news" in c.lower() :
        webbrowser.open("https://www.youtube.com/live/uUGzaNJXq7E?si=aFFfxYq2XAdt6Vq5")
        speak(f"open geo news")
    elif "open game" in c.lower() :
        webbrowser.open("https://www.crazygames.com/")
        speak("opening games")
    else :
        aiprocess(c)

if __name__ == '__main__' :
    print("Initializing jarvis. Say jarvis to give a command")
    speak("Initializing jarvis. Say jarvis to give a command")

    while True :
        r = sr.Recognizer()

        try :
            with sr.Microphone() as source :
                r.adjust_for_ambient_noise(source, duration=0.1)
                print("Listening.....")
                audio = r.listen(source, timeout=2, phrase_time_limit=3)
            print("Recognizing....")
            word = r.recognize_google(audio)

            if word.lower() == "jarvis" :
                print("Jarvis activated....")
                print("How can I assist you ayyan ?")
                speak("Jarvis activated. How can I assist you ayyaan ?")
                with sr.Microphone() as source :
                    
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print("Recognizing....")
                    processCommand(command)

        except Exception as e:
            print("Error ; {0}".format(e))
       