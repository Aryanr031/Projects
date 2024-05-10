'''
                                                    AI VOICE ASSISTANT
'''
import pyttsx3                      #It is a text-to-speech conversion library.
import speech_recognition as sr     #It is used as AI.
import wikipedia                    #to access and parse data from Wikipedia.
import webbrowser                   #provides a high-level interface to allow displaying web-based documents to users.
import datetime                     #to work with date as well as time
import os                           #provides functions for interacting with the operating system.
import pywhatkit
import pyjokes                      #to create one-line jokes
import sys                          #provides access to some functions that interact strongly with the interpreter
import time
import requests
import smtplib
from det import sender, password

s = sender
p = password
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)   #setting the voice and the speed for our Assistant. 
engine.setProperty('rate', 170)
 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

tDate=datetime.datetime.now()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hello Good Morning, Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon, Sir")

    else:
        speak("Good Evening, Sir")

    speak("I am your Personal Assistant")
    speak("Today is "+tDate.strftime("%d") + " of " + 
            tDate.strftime("%B") + tDate.strftime("%Y")
             + ". And its currently "+ tDate.strftime("%I")+ tDate.strftime("%M")+ tDate.strftime("%p"))
    speak("How are you Sir?")
    speak("Tell me What can I do for you")

def takeCommand():                      # This function will take microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.............")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing.............")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said:-\n{query}\n")

    except Exception:
        print("\nSorry Please, Say that again...")
        return "None"
    return query

mailIds = { 
    "Aryan":"va1082905@gmail.com",
    "Dhruv":"2020a1r032@mietjammu.in",
    "Ajeet":"aarnavbassan7@gmail.com"
}

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(s, p)
    server.sendmail(s, to, content)
    server.close()

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        
        if 'your name' in query:
            speak("My name is Rock")

        elif 'what' and 'about' in query:
            speak("I am having a good Day sir. What can I do for you")

        elif 'how' and 'are' in query:
            speak("I am having a good Day sir.") 

        elif 'know' and 'alexa ' in query:
            speak("Yes ,  she is the sxxxinspiration of my birth")
        
        elif 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'on youtube' in query:
            song=query.replace('in youtube', "")
            speak("playing" + song)
            pywhatkit.playonyt(song)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'google search' in query:
            import wikipedia as googleScrap
            speak("Searching Google...")
            query = query.replace("google search","")
            try:
                pywhatkit.search(query)
                result = googleScrap.summary(query,2)
                print(result)
                speak(result)
            except:
                speak("No Data found!")

        elif 'play music' in query:
            music_dir = 'C:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)    

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        #elif 'Turn' and ' on wifi ':
          #  os.system('cmd /c')
            
        
        elif 'open'and 'website' in query:
            speak("Tell me the name of the website")
            name = takeCommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            speak("Website Opened")

        elif 'news' in query:
             
            try:
                url= "https://newsapi.org/v2/top-headlines?country=in&apiKey=a667022b88da456fbc7018faa2063664"
                data = requests.get(url).json()
                i = 1
                
                speak('here are some top news')
                print('''=============== Top Headlines ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e))
 
        elif "write a note" in query:
            speak("What should i write, Sir")
            note=takeCommand()
            file=open("newtext.txt","w")
            file.write(note)
        
        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))
        
        elif "weather" in query:
            api_key="54aff85cf91f7522ddcb00066447e96c"
            url="https://api.openweathermap.org/data/2.5/weather?q=jammu&mode=json&units=metric&appid="+api_key
            
            speak("Weather in  Jammu")
            response = requests.get(url).json()
            temp=response["main"]["temp" ]
            humid=response["main"]["humidity"]
            flike=response["main"]["feels_like"]
            speak(f"temperature in jammu is {temp} degree celsius")
            speak(f"Humidity is {humid} percent")
            speak(f" and it feels like {flike} degree")   
                    
        elif 'open application' in query:
            speak("which application you want to open")
            app = takeCommand().lower()   

            if "vscode" in app:
                os.startfile("C:\\Users\\Aryan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

            elif "Powerpoint" in app:
                os.startfile("C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")

            elif "google" and "chrome" in app:
                os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            
        elif "close" in query:
            speak("which application you want to close")
            app1 = takeCommand().lower()

            if 'vscode' in app1:
                os.system("TASKKILL /f /m Code.exe")
                time.sleep(10)

            elif "Powerpoint" in app1:
                os.system("TASKKILL /f /m POWERPNT.EXE")
                time.sleep(4)

            elif "Google chrome" in app1:
                os.system("TASKKILL /f /m chrome.exe")
                time.sleep(4)
                
            elif "brave" in app1:
                os.system("TASKKILL /F /IM brave.exe")
                time.sleep(4)

            elif "microsoft" in app1:
                os.system("TASKKILL /F /IM msedge.exe")
                time.sleep(4)
                
            elif "music" in app1:
                os.system("TASKKILL /F /IM vlc.exe")
                time.sleep(4)
                
        elif 'email' in query:
            try:
                speak("To whom you want to send mail?")
                receiver = takeCommand()
                for items in mailIds:
                    if receiver in items:
                        to = mailIds.get(receiver)
                speak("What should I say?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send this email")

        elif 'exit' in query:
            speak("Thankyou Sir, Have a nice day!")
            sys.exit()