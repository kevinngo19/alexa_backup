import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print('you said: {}'.format(command))
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                a = 'As u wish, i will' + command
                print(a)
                talk(a)
                talk('processing')
                return command
            else:
                print('bye bye')
                exit()

    except:
        print('Sorry Alexa could not recognize your voice')
        talk('I could not recognize your voice')
        run_alexa()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def run_alexa():
    command1 = take_command()

    if len(str(command1)) <= 0:
        e = "Sorry I couldn't hear what you said"
        print(e)
        talk(e)
    elif len(str(command1)) <= 1:
        e = "Sorry I couldn't hear what you said"
        print(e)
        talk(e)
    else:
        response = command1.replace('play', '')
        print('playing', response)
        if 'play' in command1:
            song = command1.replace('play', '')
            talk('playing' + song)
            pywhatkit.playonyt(song)
        elif 'are' and 'you' and 'gay' in command1:
            e = "I think you are gay boi because u bang on man"
            talk(e)
            print(e)
        elif 'time' in command1:
            time = datetime.datetime.now().strftime('%H:%M:%S')
            print(time)
            talk('current time is' + time)
        elif 'wikipedia' or 'find' or 'who is' or 'what is' in command1:
            search = command1.replace('who is', '') or command1.replace('find', '') or command1.replace('wikipedia',
                                                                                                        '') or command1.replace(
                'what is', '')
            info = wikipedia.summary(search, 1)
            print(info)
            talk(info)
        elif 'tell' and 'joke' in command1:
            talk(pyjokes.get_joke())
        else:
            talk('Your english is too broken, please say again')


while True:
    run_alexa()
