from game.console import Console
from game.player import Player
from game.roster import Roster
from game.board import Board
from game.code import Code
# written by zach 
class Director:

    def __init__(self):
        
        self.Console = Console() #displays information
        self.Player = Player() #keep track of their identity and last move
        self._roster = Roster() #keep track of the players
        self.Generate = Board() #generates and updates board
        self.Code = Code() # generate code and update display code
        self.winner = ""
        
    def start_game(self):
        
        self.__prepare_game()
        while self.game_running:
            
            self.do_outputs()
            self.get_inputs()
            self.do_updates()

    def __prepare_game(self):
        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._roster.add_player(player)

    def do_outputs(self):
        self.Board.display_board(self._roster.players)
    
    def get_inputs(self):
        self.user_guess = self.Console.read(int("What is your guess? 0000-9999: "))
    
    def do_updates(self): 
        self.Code.check_player_result(self, self.user_guess)
        if self.Code.game_running == False:
            self.winner = self.Roster.get_current 
            print(f"{self.winner} won!")

        else: 
            self.Code.gen_player_result(self, self.user_guess) 
            self.Board.reprint_board() 
            self.Roster.next_player