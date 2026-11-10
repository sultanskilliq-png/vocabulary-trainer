import json
import random
def add_word():
    word = input('write your words: ')
    while word.strip() == "":
        word = input('write your words: ')

    meaning = input('write your meaning: ')
    while meaning.strip() == "":
        meaning = input('write your meaning: ')

    example = input('write your example: ')
    while example.strip() == "":
        example = input('write your example: ')

    data = {"wrong": 0, "word": word, "meaning": meaning, "example": example}
    return data

def save_words(words):
    with open('vocabulary-trainer.json', 'w') as f:
        json.dump(words, f)

def load_words():

    try:
        with open('vocabulary-trainer.json','r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return []
  
def pick_word(data):

    word = random.choice(data)
    return word 

def quiz(data):

    choes = data['word']
    
    print(choes)

    user_choies = input('write your mening: ')

    if user_choies == data['meaning']:
        return True
    
    data['wrong']+=1
    return 'wrong'
    

    
    
def most_word(data):


    weights = []
    for word in data:
        weights.append(word["wrong"]+1)
    pick = random.choices(data,weights=weights)

    return pick[0]




def stats(data):
    
    result= sorted(data,key=lambda s:s['wrong'],reverse=True)[:5]
    return result


def menu():
    words = load_words() 

    while True:
        user = input('add, quiz, repeted, total,  , q: ')

        if user == 'add':
    
            words.append(add_word())
            save_words(words)

        elif user == 'quiz':
            for i in range(3):
                print(quiz(most_word(words)))
                save_words(words)  # keeps the +1 in the file

        elif user == 'repeted':
            print(most_word(words))   # print added, save removed

        elif user=='total':
            print(len(words))

        elif user=='wrong':
            print(stats(words))

        
        elif user == 'q' or user == 'Q':
            break
        
        else:
            print('wrong choice, try again')
menu()







