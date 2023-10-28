import random
class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        self.guess = guess
        self.guess.lower()
        if self.guess in self.word:
            print (f"Good guess! {self.guess} is in the word")
        else:
            self.num_lives -= 1
            print (f"Sorry, {self.guess} is not in the word. Try again.")   
            print (f"You have {self.num_lives} lives left.")     

    def ask_for_input(self):
           while True:
                self.guess = input("Guess a letter!   ")
                self.word_guessed = list(self.word.replace(self.guess, ""))
                self.num_letters = len(set(self.word_guessed))
                if self.guess.isalpha() == False: 
                    print ("Invalid letter. Please enter a single alphabetical character")
                elif self.guess in self.list_of_guesses:
                    print ("You already tried that letter!")
                else:
                    self.check_guess(self.guess)
                    self.list_of_guesses.append(self.guess)
                    print(self.list_of_guesses)

new_game = Hangman(word_list = ["blueberry", "grape", "banana", "raspberry", "nectarine"])
new_game.ask_for_input()