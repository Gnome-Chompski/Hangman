# Hangman game

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    stsecretWord = list(secretWord)
    counter = 0
    for i in range(len(stsecretWord)):
        if stsecretWord[i] in lettersGuessed:
            counter += 1
        else:
            pass
    return counter == len(secretWord)



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    stsecretWord = list(secretWord)
    currguess = ''
    for i in range(len(stsecretWord)):
        if stsecretWord[i] in lettersGuessed:
            currguess += stsecretWord[i]
        else:
            currguess += ' _ '
    return currguess



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(len(lettersGuessed)):
        if lettersGuessed[i] in alphabet:
            alphabet.remove(lettersGuessed[i])
        else:
            pass
    corralpha = ''.join(alphabet)
    return corralpha
    
lettersGuessed = []

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    stsecretWord = list(secretWord)
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    guesses = 8
    
    while isWordGuessed(secretWord, lettersGuessed) is False:
        print("-------------")
        print("You have " + str(guesses) + " guesses left.")
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ")
        guessl = guess.lower()
        
        if guessl in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        elif guessl in stsecretWord:
            lettersGuessed.append(guessl)
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            guesses -= 1
            lettersGuessed.append(guessl)            
            
        if guesses == 0:
            break
        
    if isWordGuessed(secretWord, lettersGuessed) is True:
        print("-------------")
        print("Congratulations, you won!")
    else:
        print("-------------")
        print("Sorry, you ran out of guesses. The word was " + secretWord)
        
    

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
