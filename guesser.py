import wordretrieval
# initializes a list of words played in this game
previouswords = []

# initialize game repeation
game_continue=True
# initialize count of wins and losses
wins = 0
losses = 0

while game_continue:
    # retrieve a word and check if there are still words left
    word = wordretrieval.newword(previouswords)
    if word==0:
        print("No more words!")
        break
        
    # converts word into a list of letters
    wordsplit = list(word)
    # initializes a list to save each letter guess (for display)
    letterguesses = []

    # initializes number of guesses per round
    guesses = 7
    # main loop for each word guessing round
    while guesses>0:
        # gets user input of a word or letter
        userinput = str(input("Enter a word or letter: "))
        if len(userinput)==1:
            # letter, userinput should be one character, hence len()=1
            letterguesses.append(userinput)
            
            # if the letter is not found within the word letter list, find returns -1
            if word.find(userinput)==-1:
                guesses = guesses - 1
                print(f"This letter is not in the word. You have {guesses} guesses left.")
            else:
                # initializes and builds a string to display user guesses using list comprehension
                display = ""
                for letter in wordsplit:
                    if letter in letterguesses:
                        display += letter
                    else:
                        display += " _ "
                print(f"This letter is in the word. Your progress is: {display}")

                # if the user has successfully built the full word using all the letters, they win
                if display == word:
                    print(f"You win! You have {guesses} guesses left.")
                    break

        elif len(userinput)>1:
            #word guess because length of guess is greater than 1
            if userinput == word:
                # if the user has successfully guessed the word
                print("You win!")
                break
            else:
                guesses = guesses - 1
                print("Guess again!  You have {guesses} guesses left.")
        else:
            print("Please input a valid character or string.")
            # This else statement is for catching errors like no user input
    
    # tallies up the wins and losses
    if guesses==0:
        losses += 1
    else:
        wins += 1
    
    # gives the player the word at the end of the round
    print(f"The word is \"{word}\". You have won {wins} rounds and lost {losses} rounds.")

    # asks player if they want to continue game (by breaking initial condition of the while loop)
    game_continue = bool(input("Type nothing and press enter to end the game, or type anything and press enter to continue: "))

    # if they keep playing, add already guessed words to previouswords to track progress
    if game_continue:
        previouswords.append(word)
    else:
        break