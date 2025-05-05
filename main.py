import datetime

from time import strftime

import speech_recognition as sr
import os
import win32com.client
from wikipedia import languages
import webbrowser
import openai
import datetime
import random
from config import apikey

from openai import OpenAI

client = OpenAI(api_key=apikey)

chatStr = []

def chat(query):
    global chatStr

    # Append user's message
    chatStr.append({"role": "user", "content": query})

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Jarvis, an intelligent voice assistant."},
                *chatStr
            ],
            temperature=0.7,
            max_tokens=256
        )

        reply = response.choices[0].message.content
        say(reply)

        # Append assistant's response to chat history
        chatStr.append({"role": "assistant", "content": reply})

        return reply

    except Exception as e:
        print("Error from OpenAI:", e)
        say("Sorry, I encountered an error.")
        return "Error"



'''
def ai(prompt):
    text=f"OpenAI response for prompt: {prompt}\n***************************\n\n"
    client  = openai.OpenAI(api_key=apikey)

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[ {"role": "user", "content": "Write an email to my boss for resignation"}],
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    )
   # todo: wrap this inside of a try catch block
    print(response["choices"][0]["text"])
    if os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1,3434322)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intellegence')[1:]).strip() }.txt", "w") as f:
        f.write(text)
'''

def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio=r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language="en-in")
            print(f"User said: {query}\n")
            return query
        except Exception as e:
            return "some error occured"
if __name__ == '__main__':
    print('Pycharm')
    say("Hello, I am Jarvis AI")
    while True:
        print("Listening...")
        query = takeCommand()
        # todo:Add more sites
        sites=[["youtube","https://www.youtube.com"], ["wikipedia" ,"https://www.wikipedia.com"],["Google" ,"https://www.google.com","instagram" ,"https://www.instagram.com"] ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                webbrowser.open("https://youtube.com")
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
         # todo:Add a featrue to play a specific song
        if "open music" in query:
            musicPath =r"C:\Users\hp\Downloads\LXNGVX - Royalty Funk [NCS Release].mp3"
            os.startfile(f"open {musicPath}")

        elif "the time" in query:
            musicPath = r"C:\Users\hp\Downloads\LXNGVX - Royalty Funk [NCS Release].mp3"
            hour=datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            # strftime= datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time is {hour} bajke {min}minutes")

        elif "open Camera".lower() in query.lower():
            os.system("start microsoft.windows.camera:")

        # elif "Using artificial intelligence".lower() in query.lower():
        #     ai(prompt=query)
        elif "Jarvis Quit".lower() in query.lower():
            exit()
        elif "reset chat".lower() in query.lower():
            chatStr = []
        else:
            print("Chatting....")
            chat(query)
        # say(query)
