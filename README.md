# Welcome to Word Guesser!

In this game, you have to guess a random dictionary word. Each turn, you have to guess either individual letters or an entire word. When you guess incorrectly, the number of guesses you have decreases by 1. Guess the word before your chances run out to win!


# How to Run the Game
This game uses Python 3.8 and up.
Download this [repository](https://github.com/sock8m/word-guessing-game/tree/main) and open a terminal inside the downloaded folder. Enter this command within the terminal to start:

    python guesser.py

# Files
1. **guesser.py**: contains the bulk of the game code
2. **wordretrieval.py**: retrieves new words for each round from the words_dictionary.json file, takes in previouswords, a list or previously used words, as an argument to avoid repeating any words in one game
3. **words_dictionary.json**: a json file containing all possible words that can show up within the game