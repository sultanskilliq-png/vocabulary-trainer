#vocabulary-trainergit 

def add_word():

    word = input('write your words: ')
    meaning = input ('write your meaning: ')
    example = input ('write your example: ')

    data = {"wrong":0 , "word":word , "meaning":meaning , "example":example}
    return data

