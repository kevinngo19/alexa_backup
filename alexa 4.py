import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
from bs4 import BeautifulSoup
import smtplib
import time

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)





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

    except:
        print('Sorry Alexa could not recognize your voice')
        talk('I could not recognize your voice')
        run_alexa()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def run_alexa():

    command1 = take_command()
    response = command1.replace('play', '')
    print('playing', response)
    if 'play' in command1:
        song = command1.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command1:
        time = datetime.datetime.now().strftime('%H:%M:%S')
        print(time)
        talk('current time is' + time)
    elif 'wikipedia' or 'find' or 'who is' or 'what is' in command1:
        search = command1.replace('who is', '') or command1.replace('find', '') or command1.replace('wikipedia', '') or command1.replace('what is', '')
        info = wikipedia.summary(search, 1)
        print(info)
        talk(info)
    elif 'tell' and 'joke' in command1:
        talk(pyjokes.get_joke())
    elif 'check the price' in command1:

        URL = 'https://www.amazon.com.au/gp/product/B079HYCWR1/ref=ox_sc_act_title_1?smid=A2NLI3B5IXPZVP&psc=1'

        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

        def send_mail():
            print('sending gmail')
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()

            server.login('your gmail', 'password')
            print('login successfully')

            page = requests.get(URL, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            name = soup.find(id='productTitle').get_text()
            price = soup.find(id='priceblock_ourprice').get_text()
            title = name.strip()
            print(title, '|', price)

            subject = 'hey, the price fell down (under $100)'
            body = 'check the amazon link: https://www.amazon.com.au/gp/product/B079HYCWR1/ref=ox_sc_act_title_1?smid=A2NLI3B5IXPZVP&psc=1'
            part1 = '|'
            body2 = title + part1 + price
            msg = f'subject: {subject}\n\n{body2}\n\n{body}'

            server.sendmail('younr gmail', 'the gmail account u want to send to', msg)
            print('GMAIL HAS BEEN SENT SUCSESSFULLY!')

            server.quit()

        def check_price():
            print('checking price')
            page = requests.get(URL, headers=headers)

            soup = BeautifulSoup(page.content, 'html.parser')

            price = soup.find(id='priceblock_ourprice').get_text()
            converted_price = float(price.replace('$', ''))
            if (converted_price <= 100.00):
                send_mail()
            else:
                print('still too expensive')
        check_price()
    elif 'product price' in command1:
        print('checking price')
        page = requests.get(URL, headers=headers)

        soup = BeautifulSoup(page.content, 'html.parser')
        name = soup.find(id='productTitle').get_text()
        price = soup.find(id='priceblock_ourprice').get_text()
        print(name.strip(), end='|')
        print(price)
        talk(name, 'with the current price at:', price)
    else:
        talk('Your english is too broken, please say again')

while True:
    run_alexa()
    time.timeit




