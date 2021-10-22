import random
class Code:
    """The secret code to be guessed in the game. The responsibility of Code is to 
        generate the new code and do guess checking against player guesses.

    Stereotype:
        Service Provider, Information Holder

    Attributes:
        _code (int): The Games Secret Code
        _game_running (boolean): The game running variable
    """

    def __init__(self):
        """The class constructor.

        Args:
            self (Code): an instance of Code
        """
        self._code = format(random.randint(1000,9999), '04d')
        self._game_running = True
    
    def check_player_guess(self, guess):
        """Checks the current players guess against the code
        If code and guess match - _game_running stops and console sends out "{Player} has won"
        If code ang guess do not match - gen_player_result() will run to generate the xo* code and board can print
        
        Args:
            self (Code): an instance of Code
            guess (int): the players guess from the console
        """
        if(self._code == guess):
            self._game_running = False
            #Director would need to say a player has won from _game_running becoming false

    def gen_player_result(self, guess):
        """Generate the player XO* code
        1. Break Guess into a list with 4 indiviudal parts, same with code
        2. Check each number by position, and check number in total to gen XO or *

        Args:
            self (Code): an instance of Code
            guess (int): a player guess passed from console as an int
        """
        exp_guess = [int(x) for x in str(guess)]
        exp_code = [int(x) for x in str(self._code)]
        XO_code = ""
        for guess_digit in range(0,4):
            for code_digit in range(0,4):
                if exp_guess[guess_digit] == exp_code[guess_digit]:
                    XO_code = XO_code + "X"
                    break
                elif exp_guess[guess_digit] == exp_code[code_digit]:
                    XO_code = XO_code + "O"
                    break
                elif code_digit == 3 and exp_guess[guess_digit] != exp_code[code_digit]:
                    XO_code = XO_code + "*"
        return XO_code
                