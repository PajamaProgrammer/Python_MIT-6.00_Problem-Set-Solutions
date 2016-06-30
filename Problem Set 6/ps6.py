# MIT 6.00, Problem Set 6, Word Game II
# Name: Pajama Programmer
# Date: 22-Jan-2016
#
# pick_best_word(hand) has an average time of 0.11 seconds on my machine
# pick_best_word_faster(hand) has an average time of 0.05 seconds on my machine
# It really is faster!
# I had my doubts because of the function I use to generate ever possible combination of subsets...
# would take a time hit do to recursion and what not...
# I am not sure if it would remain faster for larger hand sizes...

import random
import string
import time

   
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

points_dict = {}    #dictionary maps a word to its points value
words_dict = {}     #dictionary maps each letter to a list of words that start with that letter
rearrange_dict = {}     #dictionary maps the aphabetized letter arrangement of the word to the word

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# PS6, Problem #3
def pick_best_word(hand):
    """
    Return the highest scoring word from points_dict that can be made with the given hand.
    Return '.' if no words can be made with the given hand.
    """
    pts_words = {}
    for char in hand:
        for word in words_dict[char]:
            if is_valid_word(word, hand):
                pts_words.setdefault(points_dict[word], word)

    points = list(pts_words.keys())
    if points:
        points.sort(reverse = True)
        word = pts_words.get(points[0], '.')
    else:
        word = '.'
    
    return word
    
def get_words_to_points(word_list):
    """
    Return a dict that maps every word in word_list to its point value. 
    """
    for word in word_list:
        points_dict[word] = get_word_score(word)

    return points_dict

def get_words_to_alphabet(word_list):
    """
    returns a dict that maps each character in the alphabet to a list of words that start with that character
    """
    for word in word_list:
        (words_dict.setdefault(word[0], [])).append(word)
    return words_dict

# PS6, Problem #4
def pick_best_word_faster(hand):
    """
    Return the highest scoring word from points_dict that can be made with the given hand.
    Return '.' if no words can be made with the given hand.
    """
    pts_words = {}
    chars = ""
    for letter in hand.keys():
        for i in range(hand[letter]):
            chars += letter   
    
    chars = "".join(sorted(chars))

    combinations = generate_combinations(chars) + [chars]

    for perm in combinations:
        pos_word = rearrange_dict.get(perm)
        if pos_word:
            pts_words.setdefault(points_dict[pos_word], pos_word)

    points = list(pts_words.keys())
    if points:
        points.sort(reverse = True)
        word = pts_words.get(points[0], '.')
    else:
        word = '.'
        
    return word

def generate_combinations(string):
    """
    Helper function I wrote, it accepts a string and will generate every possible subset of that string
    """
    A = string
    comb = []
    
    if len(A) < 1:
        return [A]
    
    for i in range(1,len(string)+1,1):
        substring = A[:i-1] + A[i:]
        if substring == "":
            break
        if substring not in comb:
           comb += [A[:i-1] + A[i:]] 
        
        morecombs = generate_combinations(substring)
        for c in morecombs:
            if c not in comb:
                comb += [c]
    return comb

# PS6, Problem #4
def get_word_rearrangements(word_list):
    for word in word_list:
        rearrange_dict["".join(sorted(word))] = word
    return rearrange_dict

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def get_time_limit(pts_dict=points_dict, k=1):  #modifying function to have optional arguments
    """
     Return the time limit for the computer player as a function of the
    multiplier k.
     points_dict should be the same dictionary that is created by
    get_words_to_points.
    """
    start_time = time.time()
    # Do some computation. The only purpose of the computation is so we can
    # figure out how long your computer takes to perform a known task.
    for word in pts_dict:
        get_frequency_dict(word)
        get_word_score(word, HAND_SIZE)
    end_time = time.time()

    return (end_time - start_time) * k

# (end of helper code)
# -----------------------------------

#
# PS 5, Problem #1: Scoring a word
#
def get_word_score(word, n=HAND_SIZE):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    # TO DO ...
    score = 0
    count = 0
    for letter in word:
        count+=1
        score += SCRABBLE_LETTER_VALUES[letter]
    if count == n:
        score += 50;
    return score

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print (letter," ", end="")   # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = int(n / 3)
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# PS 5, Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    h = hand.copy()
    for letter in word:
        h[letter] -= 1

    return h

#
# PS 5, Problem #3: Test word validity
#
#def is_valid_word(word, hand, word_list):
def is_valid_word(word, hand):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    if points_dict.get(word): #is the word valid, if yes, is it composed of letters in the hand
        freq = get_frequency_dict(word)
        for letter in word:
            if freq[letter] > hand.get(letter, 0):
                return False
        return True

    return False
        
#    PS5 Implementation....
#    h = hand.copy()
#    try:
#        word_list.index(word)
#        for letter in word:
#            if h.get(letter,0):
#                h[letter] -= 1
#            else:
#                return False
#        return True
#    except:
#        return False

#
# PS 5, Problem #4: Playing a hand
#
def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    # TO DO ...
    total = 0
    n = HAND_SIZE
    game_time = 0
    time_limit = get_time_limit()

    while time_limit <= 0:
        try:
            time_limit = float(input("Enter time limit, in seconds, for players: "))
            if time_limit <=0:
                print("Invalid time limit...")
        except:
            print("Invalid time limit...")
    print("Time limit is %.2f" %(time_limit))
    
    while n:              
        print("\nCurrent Hand: ", end="")
        display_hand(hand)

        start_time = time.time()
        #word = input("Enter word, or a . to indicate that you are finished: ")
        print("Enter word, or a . to indicate that you are finished: ", end="")
        word = pick_best_word_faster(hand)
        print(word)

        end_time = time.time()
        total_time = end_time-start_time
        game_time += total_time
        diff = time_limit - game_time

        if word == ".":
            print("Total Score: %.2f points." %(total))
            break

        print("It took %.2f seconds to provide an answer." %(total_time))
        
        if diff < 0:
            print("Total time exceeds %.2f. " %(time_limit), end="")
            print("Total Score: %.2f points." %(total))
            break
        else:
            print("You have %.2f seconds remaining." %(diff))


        if not(is_valid_word(word, hand)):
            print("Invalid word, please try again.")
        else:
            if total_time <= 0:     #to catch strange hiccups, like super fast speeds and prevent divide by zero
                total_time = 1
            score = get_word_score(word, HAND_SIZE)/total_time
            total += score
            n -= len(word)
            hand = update_hand(hand, word)
            print("%s earned %.2f points. Total: %.2f points" %(word, score, total))
    
        
    

#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    # TO DO ...
    #print ("play_game not implemented.")         # delete this once you've completed Problem #4
    #play_hand(deal_hand(HAND_SIZE), word_list) # delete this once you've completed Problem #4
    
    ## uncomment the following block of code once you've completed Problem #4
    hand = deal_hand(HAND_SIZE) # random init
    while True:
        cmd = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_list)
            print ()
        elif cmd == 'r':
            play_hand(hand.copy(), word_list)
            print ()
        elif cmd == 'e':
            break
        else:
            print ("Invalid command.")

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    points_dict = get_words_to_points(word_list)
    words_dict = get_words_to_alphabet(word_list)
    rearrange_dict = get_word_rearrangements(word_list)
    play_game(word_list)
    """
    hand = deal_hand(HAND_SIZE)
    display_hand(hand)
    print("Test 1",pick_best_word_faster(hand))
    print("Test 2",pick_best_word(hand))
    """
