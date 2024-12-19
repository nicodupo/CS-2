'''
name: Nico DuPont
description: simple hang man game code
date: 12/19/24
log: 1.0
bugs: none
sources: W3school
'''
import random
HANGMAN_BOARD = ['''
        +---+
            |
            |
            |
            ===''', '''
        +---+
        O   |
            |
            |
        ===''', '''
        +---+
        O   |
        |   |
            |
        ===''', '''
        +---+
        O   |
       /|   |
            |
        ===''', '''
        +---+
        O   |
       /|\  |
        |
        ===''', '''
        +---+
        O   |
       /|\  |
        |
       /
        ===''', '''
        +---+
        O   |
       /|\  |
       / \  |
        ===''']

def main():

    

    words = ['sister','chicken','fruit','rice','game','rockstar','cup','bowl','steak', 'season', 'sport','weight','race','lean']
    word = random.choice(words) #takes a random choice out of words
    attempts = 0 #sets attempts to zero
    dashes = list('_' * len(word)) #takes the ammount of dashes and sets it equal to word length in letters
    while attempts < 6:
    
        
        print(HANGMAN_BOARD[attempts]) #prints the board at attempts
        print(attempts) #prints number of attempts used
        print(HANGMAN_BOARD[attempts]) #reprints board and attempts 
        print(''.join(dashes)) #prints the ammount of dashes for the given word
        user_guess = input ("guess a letter:") #prompts the user to guess a letter
        if user_guess.isalpha(): #checks if user guess is a letter
            if user_guess in list(word): 
                loc = 0 #starts the check for if the letter is there at the zeroith position
                for i in range(len(word)): #makes the program check for however many dashes the word is long
                    if word[i] == user_guess: #if the letter is not in user guess
                        dashes[loc] = user_guess #than put the letter in that position
                    loc += 1
            else:  #if not
                print ('guess is not in word')
                attempts += 1 #add one to ammount of attempts
        else:
            print('user guess is not valid')

        
        # def my_dashes(length, word):
        #     count = 0 
        #     while count < len(word):
        #         dashes = dashes + "_"
        #         count = +-2
        #         count = count + 1
        #         dashes = my_dashes(word)
        #     return dashes
        
        if attempts == 6:  
            print("you loose")


        if word == str(''.join(dashes)):#if word has a full set of dashes
            print('you win!')
            exit()

main()
