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

    def display_board(self,roster):
        """Sets up the board with an entry for each player.
        
        Args:
            self (Board): an instance of Board.
            roster (Roster): get Roster
        """
        player = roster.get_current()
        hint = player.get_code()
        if hint == None:
            hint = "****"
        guess = player.get_move()
        if guess == None:
            guess = "----"
        roster.next_player()
        self._items[name] = [guess, hint]
    def update(self,hint, guess):
        pass
    
    def _create_hint(self, code, guess):
        pass
    def reprint_board(self):
        pass


    def prepare(self, player):
        pass
