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


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print('you said: {}'.format(command))
        command = command.lower()
        if 'alexa' in command:
            command = command.replace('alexa', '')
            if len(command) < 1:
                error = "Sorry, I didnt hear anything from you"
                print(error)
                talk(error)
            elif len(command) > 1:
                a = 'As u wish, i will' + command
                print(a)
                talk(a)
                talk('processing')
                return command


while True:
    command = take_command()
    if len(command) < 1:
        error = "Sorry, I didnt hear anything from you"
        print(error)
        talk(error)

    response = command.replace('play', '')
    print('playing', response)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M:%S')
        print(time)
        talk('current time is' + time)
    elif 'wikipedia' or 'find' or 'who is' or 'what is' in command:
        search = command.replace('who is', '') or command.replace('find', '') or command.replace('wikipedia',
                                                                                                 '') or command.replace(
            'what is', '')
        info = wikipedia.summary(search, 1)
        print(info)
        talk(info)
    elif 'tell' and 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'shut' and 'up' in command:
        print("Well... Rude")
        talk("Well... Rude")
        break
    else:
        talk('Your english is too broken, please say again')
