import tkinter as tk
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter.messagebox import showinfo
from threading import Thread
from PIL import Image, ImageTk, ImageSequence
root = tk.Tk()
message = tk.Label(root,text="श्रीकृष्ण",font = 'arial 25 bold',bg= 'orange')
message.place(x=100, y=650)#.pack()
shree=r"./Shree.ico"
root.geometry('645x1000')
root.configure(bg='red')
root.resizable(True, True)
root.iconbitmap(shree)
root.title('Chotu')
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import subprocess
import os
from ecapture import ecapture as ec
import time
import requests, json , sys
#PyAudio
#PyWhatkit
#Pyjokes
#Wikipedia
#OpenweatherApi

listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
engine. setProperty("rate", 110)
engine. setProperty('volume', 0.5)
voices= engine.getProperty('voices') 
engine. setProperty('voice', 'voices[0].id')

def engine_talk(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        engine_talk("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        engine_talk("Good Afternoon Sir !")  
  
    else:
        engine_talk("Good Evening Sir !") 
  
    assname =("Shree 2 point o")
    engine_talk("I am your Assistant")
    engine_talk(assname)
    user_commands()
def play_gif():
    try:
        global img
        img = Image.open("ai.gif")

        lbl = Label(root)
        lbl.place(x=0,y=0)

        for img in ImageSequence.Iterator(img):
            try:
                img=ImageTk.PhotoImage(img)
                lbl.config(image=img)
                root.update()
            except AttributeError:
                print("got it")
        root.after(0,play_gif)
    except:
        print("hello")
def user_commands():
    try:
        with sr.Microphone() as source:
            print('Listening')
            engine_talk('Sir,How can I help you')
            time.sleep(2)
            voice = listener.listen(source)
            print('Recognizing')
            command = listener.recognize_google(voice,language='en-ind')
            
            command = command.lower()
            '''
            var = StringVar()

            label = tk.Label( root, textvariable=var,
                             wraplength=300, justify="center",font=("Arial", 14))
            var.set(command)
            label.place(relx=0.0,
                        rely=1.0,
                        anchor='sw')
            #label.destroy()
            '''
            if 'shree' in command:
                command = command.replace('shree', '')
                print(command)
                run_chotu()
            else:
                talk("you are not my boss,I can't listen to you")  
    
    except:
        pass
    return command

def run_chotu():
    play_gif()
    command = user_commands()
    if 'play' in command:
        song = command.replace('play', '')
        #print("New command is" +command)
        #print("The bot is telling us; Playing" +command)
        engine_talk('playing' +song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        engine_talk('The current time is' +time)
    elif 'date' in command:
         date = datetime.datetime.now().astimezone()
         mydate=(date.replace("India Standard Time",""))
         engine_talk('Todays date is' +mydate)
    elif 'who is' in command or 'wikipedia' in command:
        engine_talk('Searching Wikipedia...')
        name = command.replace('who is', '')
        info = wikipedia.summary(name, 1)
        engine_talk("According to Wikipedia")
        var = StringVar()

        label = tk.Label( root, textvariable=var,
                             wraplength=300, justify="center",font=("Arial", 14))
        var.set(info)
        label.place(relx=0.0,
                    rely=1.0,
                    anchor='sw')
        engine_talk(info)
        label.destroy()
        #print(info)
        engine_talk(info)
    elif 'joke' in command:
        engine_talk(pyjokes.get_joke())
    elif 'how' in command:
        engine_talk('I am fine,Thank You')
    elif 'doing' in command:
        engine_talk('I am talking to you')
    elif 'name' in command:
        engine_talk('My name is shree')
    elif 'your name' in command:
        engine_talk('I am your personal assistant and my name is chhotu')
    elif 'from' in command:
        engine_talk('I am from Jalgaon Jamod')
    elif 'make' in command:
        engine_talk('Shrikant and Krishnakant make me')
    elif 'open youtube' in command:
            webbrowser.open_new_tab("https://www.youtube.com")
            engine_talk("opening Youtube")
    elif 'open google' in command:
            webbrowser.open_new_tab("https://www.google.com")
            engine_talk("opening Google")
            
    elif 'open gmail' in command:
            webbrowser.open_new_tab("https://gmail.com")
            engine_talk("Opening Google Mail")
            
    elif 'open googlemap' in command or 'open map' in command or 'open gmap' in command:
            webbrowser.open_new_tab("https://www.google.com/maps")
            engine_talk("opening Google Map")
            
    elif 'news' in command:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            engine_talk('Here are some headlines from the Times of India,Happy reading')
            
    elif "camera" in command or "take a photo" in command or "capture" in command:
            ec.capture(0,"robo camera","img.jpg")
    elif 'search'  in command:
            command = command.replace("search", "")
            webbrowser.open_new_tab(command)
            
    elif 'wynk' in command:
            command = command.replace("wynk", "")
            engine_talk('Opening wynk')
            webbrowser.open_new_tab("https://wynk.in/music" +command)
    elif 'say' in command:
            command = command.replace("say","")
            print(command)
            engine_talk(command)
    elif 'best friend' in command:
            engine_talk('You are my bestfriend')           
    elif "weather" in command:
            webbrowser.open_new_tab("https://www.timeanddate.com/weather/india/jalgaon-jamod/ext")
            engine_talk('Weather in Jalgaon Jamod')
    elif "log off" in command or "sign out" in command:
            engine_talk("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
    elif "shut down" in command:
            engine_talk("Ok , your pc will shut down in 10 sec make sure you exit from all applications")
            os.system("shutdown /s /t  1")
    elif "restart" in command:
            engine_talk("Ok , your pc will restart in 10 sec make sure you exit from all applications")
            os.system("shutdown /r /t  1")
    elif 'mad' in command or 'idiot' in command:
            engine_talk('Sorry Sir')
    elif 'whatsapp' in command:
            command  = r"C:\Users\Unknown\Desktop\App\dist\whatsapp.exe"
            os.system(command)
    elif 'good morning' in command:        
            engine_talk('Good Morning')
    elif 'good afternoon' in command:        
            engine_talk('Good Afternoon')
    elif 'good evening' in command:        
            engine_talk('Good Evening')        
    elif 'good night' in command:
            engine_talk('Good Night')
    elif 'song' in command:
            engine_talk('My fourite song is Malare')
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=0G2VxhV_gXM")
    elif 'on google' in command:
            command = command.replace("on google","")
            engine_talk(command)
            webbrowser.open(command)
            
    elif 'speak in marathi' in command:
            engine_talk('Sure,here is my friend priti')
            engine_talk('You can talk to her in marathi')
            marathi='pritimarathi.py'
            os.system(marathi)
            time.sleep(50)
    elif 'make a note' in command or 'remember' in command or 'note' in command:
            command = command.replace("make a note" , "")
            os.system(command)
            print(command)
    elif 'chrome' in command:
        engine_talk("Opening Chrome")
        os.startfile(r'C:\Program Files\Google\Chrome\Application\chrome.exe')
    elif 'wait' in command or 'quiet' in command:
        engine_talk("waiting for 5 seconds")
        time.sleep(5)

    elif 'stop' in command or 'bye' in command:
        engine_talk("Bye Sir Hava A Nice Day")
        sys.exit()
    else:
        pywhatkit.search(command)
        #engine_talk('Here is your answer from google')
        info = wikipedia.summary(command, 1)
        #engine_talk("According to Wikipedia")
        #print(info)
        var = StringVar()

        label = tk.Label( root, textvariable=var,
                             wraplength=300, justify="center",font=("Arial", 14))
        var.set(info)
        label.place(relx=0.0,
                    rely=1.0,
                    anchor='sw')
        engine_talk(info)
        label.destroy()
    while True:
        run_chotu()
if __name__ == '__main__':
    Thread(target = run_chotu).start()
    Thread(target = play_gif).start()


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Item")
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        fileMenu.add_command(label="Chotu", command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=editMenu)

    def exitProgram(self):
        exit()
def exitProgram(self):
        exit()
def exit():
   sys.exit()
   
download_icon = tk.PhotoImage(file="12.png")
download_button = ttk.Button(
                root,
                image=download_icon,
                command=run_chotu
            )

download_button.place(x=300,y=650)#pack(
                #ipadx=5,
                #ipady=5,
                #expand=True
            #)

button =Button(root,text='Click here',bg='green',font= ('Helvetica 20 bold italic'),activebackground='orange',command = run_chotu,)
root.bind('f', lambda event: wishMe())
button.place(x=250, y=710)#.pack()
button = ttk.Button(root,text='Exit',command = exit)
button.place(x=290, y=772)#.pack()
root.mainloop()














