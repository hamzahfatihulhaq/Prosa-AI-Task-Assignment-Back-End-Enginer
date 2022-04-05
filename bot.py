import json
from multiprocessing import reduction
import random

with open('intents.json', 'r') as f:
    intents = json.load(f)


questions = {}
answers = {}

for intent in intents['intents']:
    tag = intent['tag']
    questions[tag] = list(map(lambda x: x.lower(), intent['patterns']))
    answers[tag] = list(map(lambda x: x.lower(), intent['responses']))

def bot_processing(qs,trigger):
    for i in questions:
        for j in questions[i]:
            if qs == j:
                trigger = True
                return i,trigger
    return " ",trigger
def get_response(tagbot,trigger):
    tag = tagbot

    if trigger :
        random_answer = random.randint(0,len(answers[tag])-1)
        msg = answers[tag][random_answer]
        trigger = False
        return msg,trigger
    else:
        msg = 'saya tidak mengerti...'
        return msg,trigger

def Bot(msg):
    msg = msg.lower()
    trigger = False 
    tag,trigger = bot_processing(msg,trigger)
    resp,trigger = get_response(tag,trigger)
    
    return resp,tag

def firstConv():
    msg = 'Hi, Selamat datang, saya bot demo disini, silahkan bertanya'
    return msg

def endConv():
    msg = "Terima Kasih, Sampai jumpa lagi"
    return msg

if __name__ == "__main__":
    bot_name = 'bot'

    print(f'{bot_name}  : {firstConv()}')

    while True:
        qs = input('user : ')

        if qs == 'keluar':
            resp = "Terima Kasih, Sampai jumpa lagi"
            print(f'{bot_name}  : {resp}')
            break
        else:
            resp,tag = Bot(qs)

            print(f'{bot_name}  : {resp} ({tag})')
            if tag == 'goodbye':
                resp = "Terima Kasih, Sampai jumpa lagi"
                print(f'{bot_name}  : {resp}')
                break