import random

class Board:
    """- equals players guess * equals wrong X means correct number 0 correct number  incorrect spot
    --------------------
    Player Matt: ----, ****
    Player John: ----, ****
    --------------------
    Matt's turn:
    What is your guess? 1111

    --------------------
    Player Matt: 1111, xooo
    Player John: ----, ****
    --------------------
    John's turn:
    What is your guess? 4356"""

    def __init__(self):
        self._items= []

    def display_board(self,roster,code):
        """Sets up the board with an entry for each player.
        
        Args:
            self (Board): an instance of Board.
        """
        name = roster.get_current()
        guess = "----"
        hint = "****"
        self._items[name] = [code, guess, hint]

    def update(self,hint, guess):
        pass
    
    def _create_hint(self, code, guess):
        pass
    def reprint_board(self):
        pass


    def prepare(self, player):
        pass

    def _create_hint(self, code, guess):
        """Generates a hint based on the given code and guess.

        Args:
            self (Board): An instance of Board.
            code (string): The code to compare with.
            guess (string): The guess that was made.

        Returns:
            string: A hint in the form [xxxx]
        """ 
        hint = ""
        for index, letter in enumerate(guess):
            if code[index] == letter:
                hint += "x"
            elif letter in code:
                hint += "o"
            else:
                hint += "*"
        return hint

