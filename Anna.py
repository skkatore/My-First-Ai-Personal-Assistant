import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser 
import wikipedia
'''from google import pygoogletranslation'''
import requests
from bs4 import BeautifulSoup
import os
import random
import pygame
from pygame import mixer
import keyboard
import pyjokes

recognizer = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',180)

def speak(response):
    print("Assistant:", response)
    engine.say(response)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello I am Anna Your Personal AI Assistant. Please tell me how may I Assist You?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query.lower()

def TaskExe():

    def OpenApps():
        speak("Ok Boss , Wait a Second!")

       
        if 'chrome' in query:
            speak("Opening chrome!")
            codePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(codePath)

        elif 'vm' in query:
            speak("Opening vm!")
            codePath = "C:\Program Files\Oracle\VirtualBox\VirtualBox.exe"
            os.startfile(codePath)

        elif 'PyCharm' in query:
            speak("Opening PyCharm!")
            codePath = "C:\Program Files\JetBrains\PyCharm Community Edition 2022.3.3\bin\pycharm64.exe"
            os.startfile(codePath)

        elif 'code' in query:
            speak("Opening code!")
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'youtube' in query:
            speak("Opening youtube!")
            webbrowser.open("youtube.com")

        elif 'google' in query:
            speak("Opening google!")
            webbrowser.open("google.com")

        elif 'mail' in query:
            speak("Opening mail!")
            webbrowser.open("mail.com")

        elif 'stackoverflow' in query:
            speak("Opening stacjoverflow!")
            webbrowser.open("stackoverflow.com")

        elif 'amazon' in query:
            speak("Opening amazon!")
            webbrowser.open("amazon.com")

        elif 'flipcart' in query:
            speak("Opening flipcart!")
            webbrowser.open("flipcart.com")

        elif 'naukri' in query:
            speak("Opening naukri!")
            webbrowser.open("naukri.com")

        elif 'google map' in query:
            speak("Opening google map!")
            webbrowser.open("google map.com")

        elif 'udemy' in query:
            speak("Opening udemy!")
            webbrowser.open("udemy.com")

        elif 'chatgpt' in query:
            speak("Opening chatgpt!")
            webbrowser.open("chatgpt.com")

        elif 'github' in query:
            speak("Opening github!")
            webbrowser.open("github.com")

        elif 'whatsapp' in query:
            speak("Opening whatsapp!")
            webbrowser.open("whatsapp.com")

        elif 'spotify' in query:
            speak("Opening spotify!")
            webbrowser.open("spotify.com")

        speak("Your Command Has Been Completed Succesfully!")

    def CloseAPPS():
        speak("Ok Sir , Wait A Second!")

        if 'chrome' in  query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'vm' in query:
            os.system("TASKKILL /F /im vm.exe")

        elif 'PyCharm' in query:
            os.system("TASKKILL /F /im PyChram.exe")

        elif 'code' in query:
            os.system("TASKKILL /F /im code.exe")

        elif 'youtube' in query:
            webbrowser("TASKKILL /F /im youtube.com")


        elif 'google' in query:
            webbrowser("TASKKILL /F /im google.com")

        elif 'mail' in query:
            webbrowser("TASKKILL /F /im mail.com")

        elif 'stackoverflow' in query:
            webbrowser("TASKKILL /F /im stackoverflow.com")

        elif 'amazon' in query:
            webbrowser("TASKKILL /F /im amazon.com")

        elif 'flipcart' in query:
            webbrowser("TASKKILL /F /im flipcart.com")

        elif 'naukri' in query:
            webbrowser("TASKKILL /F /im naukri.com")

        elif 'google map' in query:
            webbrowser("TASKKILL /F /im google map.com")
        
        elif 'udemy' in query:
            webbrowser("TASKKILL /F /im udemy.com")

        elif 'chatgpt' in query:
            webbrowser("TASKKILL /F /im chatgpt.com")

        elif 'github' in query:
            webbrowser("TASKKILL /F /im github.com")

        elif 'whatsapp' in query:
            webbrowser("TASKKILL /F /im whatsapp.com")

        elif 'spotify' in query:
            webbrowser("TASKKILL /F /im spotify.com")

        speak("Your Command Has Been Completed Succesfully!")

    def YoutubeAuto():
        speak("Whats Your Command Sir!")
        comm = takeCommand()

        if 'pause' in comm:
            keyboard.press('k')

        elif 'play' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('1')

        elif 'full screen' in comm:
            keyboard.press('f')

        speak("Done Boss!")

    def get_weather(city):
        api_key = "YOUR_API_KEY"  # Replace with your own OpenWeatherMap API key
        query = query.replace("Anna","")
        query = query.replace("google search","")
        web = "https://www.google.com=" +query
        webbrowser.open(web)
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"] - 273.15  # Convert temperature from Kelvin to Celsius
            speak(f"The current weather in {city} is {weather_description}. The temperature is {temperature:.1f}°C.")
        else:
            speak("Sorry, I couldn't fetch the weather information for that city.")

    def search_wikipedia(query):
        try:
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        except wikipedia.exceptions.WikipediaException:
            speak("Sorry, I couldn't find any relevant information on Wikipedia.")

    def search_on_google(query):
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)

    def play_music():
        speak("Ok Boss , Playing Music!")
        music_dir = 'C:\\Users\\skato\\Music\\music 1'
        songs = os.listdir(music_dir)
        print(songs)    
        os.startfile(os.path.join(music_dir, songs[0]))
        speak("Your song has been started!")
        speak("Enjoy Your Music!")

    '''def TakeHindi():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='hi')
            print(f"User said: {query}\n")

        except Exception as e:
        # print(e)    
            print("Say that again please...")  
            return "None"
            return query.lower()

    def Tran():
        speak("tell me the line")
        line = TakeHindi()
        traslate = pygoogletranslation()
        result = traslate.pygoogletranslation(line)
        speak("The Translation for this line is:" +Text)
        Text = result.text '''

    if __name__ == "__main__":
            wishMe()
    while True:
    # if 1:

        query = takeCommand()

        if 'hello' in query:
            speak("Hello Boss , I Am Anna .")
            speak("How May I Assist You?")

        elif 'how are you' in query:
            speak("I Am Fine Boss!")
            speak("Whats About You?")

        elif 'you need a break' in query:
            speak("Ok Boss , You Can Call Me Aany Time")
            break

        elif 'i love you' in query:
            speak("I Love You Too boss!")
            speak("But As   AI Friend!")

        elif 'good girl' in query:
            speak("Thank you boss!")

        elif 'my world' in query:
            speak("Yours Mom Dad is your World!")

        elif 'my favourite hero' in query:
            speak("Prabhas Is Your Most Favourit Hero Boss")

        elif 'my favourite singer' in query:
            speak("Guru Randhava Is Your Favourit Singer")

        elif 'youtube search' in query:
            speak("Ok Sir ,This Is What I Found For Your Search!")
            query = query.replace("Anna","")
            query = query.replace("youtube search","")
            web = "https://www.youtube.com/results?search_query=" +query
            webbrowser.open(web)
            speak("Done Boss!")

        elif 'open google' in query:
            speak("Ok Boss , This Is What I Found For Your Search!")
            query = query.replace("Anna","")
            query = query.replace("open google","")
            web = "https://www.google.com/search?q=" +query
            webbrowser.open(web)
            speak("Done Boss!")

        elif 'websit' in query:
            speak("Ok Boss!")
            speak("Opening website!")
            query = query.replace("Anna","")
            query = query.replace("website","")
            query = query.replace("  ","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            speak("This What I Found!")

        elif"weather" in query:
            speak("Sure, which city?")
            city = takeCommand()
            get_weather(city)

        elif "who is" in query or "what is" in query:
            query = query.replace("who is", "").replace("what is", "").strip()
            search_wikipedia(query)

        elif "search" in query:
            speak("Sure, what would you like to search for?")
            query = takeCommand()
            search_on_google(query)
            
        elif "time" in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}.")
        
        elif "date" in query:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today's date is {current_date}.")

        if "play music" in query:
            play_music()
        
        elif 'wikipedia' in query:
            speak("Searching Wikipedia...") 
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'play my favourite song' in query:
            speak("Ok Boss , Starting song!")
            music_dir = 'C:\\Users\\skato\\Music\\music 1'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Your song has been started!")
            speak("Enjoy Your song!")

        elif 'by' in query:
            speak("Ok Boss ,  Bye!")
            break

        elif 'open chrome' in query:
            OpenApps()

        elif 'open vm' in query:
            OpenApps()

        elif 'open PyCharm' in query:
            OpenApps()

        elif 'open code' in query:
            OpenApps()

        elif 'open youtube' in query:
            OpenApps()

        elif 'open google' in query:
            OpenApps()
 
        elif 'open mail' in query:
            OpenApps()
 
        elif 'open stackoverflow' in query:
            OpenApps()

        elif 'open amazon' in query:
            OpenApps()

        elif 'open flipcart' in query:
            OpenApps()

        elif 'open naukri' in query:
            OpenApps()

        elif 'open google map' in query:
            OpenApps()

        elif 'open udemy' in query:
            OpenApps()

        elif 'open chatgpt' in query:
            OpenApps()

        elif 'open github' in query:
            OpenApps()

        elif 'open whatsapp' in query:
            OpenApps()

        elif 'open spotify' in query:
            OpenApps()

        elif 'open play music' in query:
            OpenApps()

        elif 'Close chrome' in query:
            CloseAPPS()

        elif 'Close vm' in query:
            CloseAPPS()

        elif 'Close PyCharm' in query:
            CloseAPPS()

        elif 'Close code' in query:
            CloseAPPS()

        elif 'Close youtube' in query:
            CloseAPPS()

        elif 'Close google' in query:
            CloseAPPS()
 
        elif 'Close mail' in query:
            CloseAPPS()
 
        elif 'Close stackoverflow' in query:
            CloseAPPS()

        elif 'Close amazon' in query:
            CloseAPPS()

        elif 'Close flipcart' in query:
            CloseAPPS()

        elif 'Close naukri' in query:
            CloseAPPS()

        elif 'Close google map' in query:
            CloseAPPS()

        elif 'Close udemy' in query:
            CloseAPPS()

        elif 'Close chatgpt' in query:
            CloseAPPS()

        elif 'Close github' in query:
            CloseAPPS()

        elif 'Close whatsapp' in query:
            CloseAPPS()

        elif 'Close spotify' in query:
            CloseAPPS()

        elif 'paus' in query:
            keyboard.press('k')

        elif 'play' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('1')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'youtube tools ' in query:
            YoutubeAuto()

        elif 'my location' in query:
            speak("Ok Sir , Wait A Second")
            speak("I Am Tracking Your Location")
            webbrowser.open("https://www.google.com/maps/place/Pune,+Maharashtra+411032/@18.5815568,73.9195308,14z/data=!3m1!4b1!4m6!3m5!1s0x3bc2c6b34b728c8f:0x83e1c9ed4200a082!8m2!3d18.5930989!4d73.921781!16s%2Fg%2F1hhw711y_?entry=ttu")
            speak("Your Location  Has Been Tracked")

        elif 'jokes' in query:
            speak("Ok Boss!")
            speak("Getting Jokes for You!")
            get = pyjokes.get_joke()
            speak(get)
            speak("How was it!")

        elif 'repeat my words' in query:
            speak("Yours Repeatation Command Has Been Enabled!")
            jj = takeCommand()
            speak(f"You Said : {jj}")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Boss, Now its {strTime}")

        elif 'alarm' in query:
            speak("Tell Me The Time !")
            time = input(": Enter The time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H,%M,%S")

                if now == time:
                    speak("Time To Weak Up Boss!")
                    speak("Alarm Closed!")
                
                elif now>time:
                    break
            
        elif 'remember that' in query:
            rememberMsg = query.replace("remember that","")
            rememberMsg = rememberMsg.replace("Anna","")
            speak("You Told Me To Remind ;"+rememberMsg)
            remeber = open('date.txt','w')
            remeber.write(rememberMsg)
            remeber.close()

        elif 'what do you remember' in query:
              remeber = open('date.txt','r')
              speak("You Told me to :"+remeber.read())       

        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("Anna","")
            query = query.replace("google search","")
            query = query.replace("google","")
            webbrowser.search(query)
            webbrowser.open(web)
            speak("This is what i found for you boss!")

            try:
                result = googleScrap(query,3)
                speak(result)

            except:
                speak("")

            

TaskExe()