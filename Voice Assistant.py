import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)





def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis Sir. Please tell me how may i help you")

def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing")
        query=r.recognize_google(audio,Language='en-in')
        print(f"User said: ",{query})
    except Exception as e:
        #print(e)
        print("say that again please")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttis()
    server.login('youremail@gmail.com','password')
    server.sendmail('yourmail@gmail.com',to,content)
    server.close()
    
    
        
    

if __name__=="__main__":
    wishMe()
    #while True:
    if 1:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak("results")
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')
            
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
            
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is{strTime}")

        elif 'email to yash' in query:
            try:
                speak("what should i say")
                content=takeCommand()
                to="yash12@gmail.com"
                sendEmail(to,content)
                speak("email sent")
            except exception as e:
                print(e)
                speak("sorry not able to send")
                
            
            
            





























        
    
