
class Board:

    """- equals players guess * equals wrong X means correct number 0 
    correct number 
    incorrect spot
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
        self.line = "_" * 20
        self.guess = "_" * 4
        self.hint = "*" * 4
        self.code = ""

    def print_board(self,player,code):
        # secret code shows as ----

        players = player.get_name()
        self.code = code.get_hints()
        print(self.line)
        print(f"Player {players[0]}: {self.code},{self.guess},{self.hint}")
        print(f"Player {players[1]}: {self.code},{self.guess},{self.hint}")
        print(self.line)

    def update(self,hint, guess):
        pass
    
    def _create_hint(self, code, guess):
        pass
    def reprint_board(self):
        pass
