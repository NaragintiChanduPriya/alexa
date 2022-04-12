import speech_recognition as jarvis
import pyttsx3
import pywhatkit
import datetime
from playsound import playsound
import wikipedia
import pyjokes

listener = jarvis.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with jarvis.Microphone() as source:
            print("listening.....")
            voice = listener.listen(source)
            order = listener.recognize_google(voice)
            order = order.lower()
            if 'alexa' in order:
                order = order.replace('alexa', '')

            else:
                talk("call me alexa boss!")

    except:
        pass
    return order


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing '+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is person' in command:
        person = command.replace('who the person', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('I will take any chance to spend more time with u')
        print('I will take any chance to spend more time with u')
    elif 'are you single' in command:
        song = "single am ready to mingle"
        pywhatkit.playonyt(song)
        talk('I am single my dear!!!!')

    elif 'message' in command:
        talk("enter phonenumber with countrycode")
        phno = input("enter phonenumber with countrycode: ")
        talk("enter a msg to send")
        msg = input("enter a msg to send: ")
        talk("mention hour")
        h = int(input("mention hour: "))
        talk("mention minute")
        m = int(input("mention minute: "))
        pywhatkit.sendwhatmsg(phno,msg,h,m)
        talk("successfully sent")
    elif 'search' in command:
        talk("enter data to search boss!!")
        print("enter data to search!!!")
        msg = input()
        pywhatkit.search(msg)
        print("searching......!!!!")
    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    elif 'alarm' in command:
        talk("Enter the time!!!")
        time = input("Enter the time:")
        while True:
            now = datetime.datetime.now().strftime('%H:%M:%S')
            if now == time:
                talk("Time to wake up...boss!!!")
                playsound('hello.mp3')
                talk('Completed!!!')
            elif now > time:
                break

    else:
        talk('Boss!!!Please say the command again.')


while True:
    run_alexa()
