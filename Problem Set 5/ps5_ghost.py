# MIT 6.00, Problem Set 5, Ghost
# Name: Pajama Programmer
# Date: 12-Jan-2016
#
import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def make_word_dict(wordlist):
    """
    Returns a dictionary where the keys are the letters of the alphabet
    and the values are a list of words that start with letter=key


    sequence: word list (strings)
    return: dictionary
    """
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    word_dict = dict()
    for word in wordlist:
        word_dict.setdefault(word[0].upper(), []).append(word.upper())
    return word_dict

def is_valid_fragment(fragment, word_dict):
    #print(fragment)
    key = fragment[0]
    length = len(fragment)
    #print(key)
    for word in word_dict[key]:
        if fragment == word and len(word) > 3:
            #print(word)
            return 'isWord'
        if fragment in word[0:length]:
            #print(word)
            return 'isFrag'
    return 'notValid'

def switch_player(player):
    if player == 1:
        return 2
    return 1
# (end of helper code)
# -----------------------------------

# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.
if __name__ == '__main__':
    
    # Actually load the dictionary of words and point to it with 
    # the wordlist variable so that it can be accessed from anywhere
    # in the program.
    wordlist = load_words()
    word_dict = make_word_dict(wordlist)
    # TO DO: your code begins here!
    player = 1
    true = 1
    tallyP1 = 0
    tallyP2 = 0
    print("\nWelcome to Ghost!")
    while true:
        fragment = ''
        print("Player %d goes first.\n" %(player))
        print("Current word fragment: '%s'" %(fragment.upper()))
        while True:
            print("Player %d's turn." %(player))
            print("Player", player, "says letter: ", end="")
            letter = input()
            while (not letter.isalpha()) or (len(letter) > 1):
                print("Invalid Entry, please try again: ", end="")
                letter = input()
            fragment += letter.upper()

            print("\nCurrent word fragment: '%s'" %(fragment))

            code = is_valid_fragment(fragment,word_dict)
            if code == 'isWord':
                print("Player %d loses because '%s' is a word!" %(player, fragment))
            if code == 'notValid':
                print("Player %d loses because no word begins with '%s'!" %(player, fragment))
            player = switch_player(player)
            if code != 'isFrag': 
                print("Player %d wins!" %(player))
                if player == 1:
                    tallyP1 +=1
                else:
                    tallyP2 +=1
                player = switch_player(player)
                break

        print("\nNew Game? \n0: Exit \n1: Continue")
        true = int(input())

    print("\nPlayer 1 Wins: %d\nPlayer 2 Wins: %d\n" %(tallyP1, tallyP2))

