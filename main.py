from random import randint
from clipart import rock, paper, scissors


class Game:
    choices_list = [rock, paper, scissors]

    def __init__(self):
        self.player_pick = None

    def init_game(self):
        print("****** ROCK PAPER SCISSORS ******\n\n")
        print('Type 0 for "rock", 1 for "paper" or 2 for "scissors"\n')

        self.player_pick = int(input('What do you choose? '))
        
        while self.player_pick > 2:
            self.player_pick = int(input("You\'ve enter an invalid number.\nPlease enter again: "))

    def check_winner(self):
        if self.player_pick <= 2:
            print("\n\n******** Your Choice ********")
            player_choice = self.choices_list[self.player_pick]
            print(player_choice)
        
            print("******** Computer's Choice ********")
            computer_pick = randint(0, len(self.choices_list) - 1)
            computer_choice = self.choices_list[computer_pick]
            print(computer_choice)
        
            # player_wining_composition = [[0, 2], [1, 0], [2, 1]]
            # computer_wining_composition = [[0, 1], [1, 2], [2, 0]]
            if self.player_pick == 0 and computer_pick == 2 or self.player_pick > computer_pick:
                print("*" * 27)
                print(f"* {' ' * 7} You Win {' ' * 7} *")
                print("*" * 27)
            elif self.player_pick == 2 and computer_pick == 0 or self.player_pick < computer_pick:
                print("*" * 28)
                print(f"* {' ' * 7} You Lose {' ' * 7} *")
                print("*" * 28)
            elif self.player_pick == computer_pick:
                print("*" * 32)
                print(f"* {' ' * 7} A Tight Game {' ' * 7} *")
                print("*" * 32)

    def play(self):
        self.init_game()
        self.check_winner()


game = Game()
game.play()
