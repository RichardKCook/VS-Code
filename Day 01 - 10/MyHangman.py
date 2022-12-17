import random

def run():
    word_list = ["aardvark", "baboon", "camel"]



    word = word_list[random.randint(0,len(word_list)-1)]

    #TODO-1: - Create an empty List called display.
    #For each letter in the chosen_word, add a "_" to 'display'.
    #So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

    wordASlist = []
    for letter in word:
        wordASlist += letter


    display=[]
    for _ in word:
        display += "_"

    print(display)

    guess = input("What letter would you like to guess?\n").lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].



    
    

    if display == word_list:
        return(0)
    j=0
    while j < 7:
        if j == 6:
            print("you lose")
            return(0)
        i=0
        while i < len(word):
            
            if guess == word[i]:
                
                display[i] = guess
                
                i += 1

            else:
                
                i += 1
        print(display)
        if display == wordASlist:
                    print("you win")
                    return(0)
        j+=1
        guess = input("What letter would you like to guess?\n").lower()
run()
#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.