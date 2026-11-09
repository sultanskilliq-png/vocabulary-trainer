import json
import random
def add_word():
    word = input('write your words: ')
    meaning = input('write your meaning: ')
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


    
words= load_words()
# words.append(add_word())
# save_words(words)
# choes = pick_word(words)
# result = quiz(choes)
# save_words(words)
# print(result)
# print(words)
most_wordd = most_word(words)
print(most_wordd)









