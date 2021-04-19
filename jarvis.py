import pyttsx3
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Mornig!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
         speak("Good Evening!")

    speak("I am Edith sir. Pleas tell me how may help you?")

def takecommand():
    #it takes microphone input from the user and retures string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        qurey = r.recognize_google(audio, language='en-in')
        print(f"User said: {qurey}\n")

    except Exception as e:
        #print(e)
        print('Say that aging pleas...')
        return"None"
    return qurey


if __name__ == "__main__":
    wishMe()
    while True:
        qurey = takecommand().lower()

        #Locgic for executing tasks pased on qury
        if 'wikipedia' in qurey:
              speak('Searching wikipedia...')
              qurey = qurey.replace("wikipedia", "")
              results = wikipedia.summary(qurey, sentences=2)
              speak("According to wikipedia")
              print(results)
              speak(results)

        elif 'open youtube' in qurey:
            webbrowser.open("youtube.com")
            speak('opening youtube...')
         
        elif 'open google' in qurey:
            webbrowser.open("google.com")
            speak('opening google...')

        elif 'who are you ' in qurey:
            speak('I am your assistant Edith sir')

        elif 'the time' in qurey:
            strTime = datetime.datetime.now().strftime('%I:%M %P')
            speak(f"The time is{strTime}")

        elif 'send email to Harry' in qurey:
            try:
                speak("what should I say?")
                content = takecommand()
                to = "amey.pople@rbhs.org.in"
                sendEmail(to, content)
                speak("Email has been send")
            except Exception as e:
                print(e)
                speak("sorry sir I was not able to send the Email")
        