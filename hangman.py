import random 

print("Welcome to the Hangman App!")

words_file = open('words.txt', 'r')
words = words_file.read().split()

stages = [
    '''
     +-----+
     |     |
     0     |
    /|\    |
    / \    |
           |
============
''','''
     +-----+
     |     |
     0     |
    /|\    |
    /      |
           |
============
''','''
     +-----+
     |     |
     0     |
    /|\    |
           |
           |
============
''','''
     +-----+
     |     |
     0     |
    /|     |
           |
           |
============
''','''
     +-----+
     |     |
     0     |
     |     |
           |
           |
============
''','''
     +-----+
     |     |
     0     |
           |
           |
           |
============
''','''

'''
]

search_word = random.choice(words)
#print(search_word)
lives_count = 7
guessed_word = '_'*len(search_word)
checked_letters = []

print(f"You need to guess this word: {guessed_word}")

def guess(guessed_letter):
    global guessed_word
    count = 0
    tmp_list = list(guessed_word)
    if guessed_letter in search_word:
        for letter in search_word:
            if letter == guessed_letter:
                tmp_list[count] = guessed_letter
            count += 1                               
    else:
        global lives_count
        print(f"There is no {guessed_letter} in this word")
        lives_count = lives_count - 1
    
    guessed_word = "".join(tmp_list) 
    return(guessed_word)

def check_live():
    if lives_count == 0:
        return(0)
    else:
        return(1)

def check_win():
    if "_" in guessed_word:
        return(0)
    else:
        return(1)
    
while check_win() == 0 and check_live() == 1:
    print(stages[lives_count - 1])
    print(f"Lives left: {lives_count}")
    print(f"Letters checked: {checked_letters}")
    x = input("Guess the letter: ")
    checked_letters.append(x)
    guessed_word = guess(x)
    print(f"You need to guess this word: {guessed_word}")

if check_win() == 1:
    print(f"You won, the word was: {search_word}")
else:
    print(f"You lost, the word was: {search_word}")
