from game.console import Console
from game.player import Player
from game.roster import Roster
from game.board import Board
from game.code import Code
# written by zach 
class Director:

    def __init__(self):
        
        self.Console = Console() #displays information
        self._roster = Roster() #keep track of the players
        self.Board = Board() #generates and updates board
        self.Code = Code() #generate code and update display code
        self.winner = ""
        
    def start_game(self):
        
        self.__prepare_game()
        while self.Code._game_running:
            
            self.do_outputs()
            self.get_inputs()
            self.do_updates()

    def __prepare_game(self):
        for n in range(2):
            name = self.Console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._roster.add_player(player)
        self._roster.next_player()

    def do_outputs(self):
        self.Board.display_board(self._roster)
    
    def get_inputs(self):
        self.user_guess = int(self.Console.read(f"{self._roster.get_current().get_name()}, What is your guess? 0000-9999: "))
    
    def do_updates(self):
        self._roster.get_current().set_move(self.user_guess) 
        self.Code.check_player_guess(self.user_guess)
        if self.Code._game_running == False:
            self.winner = self._roster.get_current().get_name()
            print(f"{self.winner} won!")
        else: 
            self._roster.get_current().set_code(self.Code.gen_player_result(self.user_guess) )
            self._roster.next_player()