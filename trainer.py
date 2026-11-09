import json

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
  

# words = load_words()
# words.append(add_word())
# save_words(words)










