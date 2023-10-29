import random
class Hangman:

    """
   This class is used to run the game Hangman
   
   Attributes:
      word (list) - a randomly chosen word (by the computer) from the word list given when calling the Hangman class. The word is converted to a list of individual letters (strings) to enable this attribute to function in the class.
      word_guessed (list) - a list of letters in the chosen word that have been guessed correctly.  Until the letters have been guessed correctly, the letter is replaced by "_".
      num_letters (int) - the number of unique letters in the chosen word remaining - which have not yet been guessed.
      num_lives (int) - the number of lives left, default is 5, can be changed when calling the class.
      word_list (list) - a list of words entered when calling the Hangman class for the computer to randomly choose from.
      list_of_guesses (list) - a list of the letters which have already been guessed (correctly or incorrectly)

    """


    def __init__(self, word_list, num_lives = 5):
        self.word = list(random.choice(word_list))
        self.word_guessed = []   
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    
    def check_guess(self, guess):

        """
        This function is used to check if the letter guessed by the user is in the word chosen by the computer.  It converts the input to lower case.  If it is correct, num_letters reduces by 1.  If it is incorrect num_lives reduces by 1.

        Args:
           guess (str) - the letter guessed and inputted by the user

        Returns:
           str: "Good guess! {guess} is in the word" if the guess is in the word; "Sorry, {guess} is not in the word. Try again. You have {number of lives} lives left" otherwise.
        
        """

        self.guess.lower()
        if self.guess in self.word:
            print (f"Good guess! {self.guess} is in the word")
            self.word_guessed = [x if x == self.guess or x in self.list_of_guesses else "_" for x in self.word] 
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print (f"Sorry, {self.guess} is not in the word. Try again.")   
            print (f"You have {self.num_lives} lives left.")
            
   
    def ask_for_input(self):

        """
        This function asks the user to guess a letter, and checks it is a single alphabetical character and that it has not already been guessed.  Once it receives a valid input it calls the check_guess function and adds the guessed letter to list_of_guesses.

        Returns:
            str: "Invalid letter. Please enter a single alphabetical character" if the input it not a single alphabetical character.  "You already tried that letter" if the letter has already been guessed.    
           
        """

        self.guess = input("Guess a letter!   ")
        if len(self.guess) >1 or self.guess.isalpha() == False: 
            print ("Invalid letter. Please, enter a single alphabetical character")
        elif self.guess in self.list_of_guesses:
            print ("You already tried that letter!")
        else:
            self.list_of_guesses.append(self.guess)
            self.check_guess(self.guess)
            
def play_game(word_list):  

    """
    This function runs the whole game with a specified word list and number of lives.

    Args:
        word_list (list) - a list of words to be entered when calling the function, which the computer will randomly choose from.
        
    Returns:
        str: "You lost!" if the number of lives reaches 0, or "Congratulations. You won the game!" if the user guesses all letters correctly before losing all their lives.

    """

    num_lives = 5  
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:  
            print ("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:    
            print ("Congratulations. You won the game!") 
            break      
               
play_game(["blueberry", "grape", "banana", "raspberry", "nectarine"])