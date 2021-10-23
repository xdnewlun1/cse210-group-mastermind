import random

class Board:
    def __init__(self):
        self._items= []
        self.line = "_" * 20 

    def display_board(self,roster): # player [] is in the roster 
        """Sets up the board with an entry for each player.
        
        Args:
            self (Board): an instance of Board.
            roster (Roster): get Roster
        """

        print(self.line) # print out line 
        for player in roster.players: # going through players 
            name = player.get_name() # get players name from player.get_name() 
            guess = player.get_move() # get guess from player.get_move
            if guess == None:
                guess = "----"
            hint = player.get_code() # hint comes from player.get_code()
            if hint == None:
                hint = "****"
            print(f"Player {name}: {guess}, {hint}\n")
        print(self.line)

        # xanders code 
        # player = roster.get_current()
        # hint = player.get_code()
        # if hint == None:
        #     hint = "****"

        # guess = player.get_move()
        # if guess == None:
        #     guess = "----"
        # self._items[player] = [guess, hint]

        # print(self.line)
        
        # roster.next_player()

        # import random
        # line = "-"* 20
        # players =["Tom","Jen"]
        # code = str(random.randint(1000, 10000))
        # guess = "_" * 4
        # hint = "*" * 4
        # #self._piles[player] = [code, guess, hint]
        # # piles[name]= [code, guess, hint]
        # # print(piles[name])
        # print(line)
        # print(f"Player {players[0]}: {code},{guess},{hint}")
        # print(f"Player {players[1]}: {code},{guess},{hint}")
        # print(line)    


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
