
# First Working Code for Rock-Paper-Scissors

from random import randint

# print(ord('p'),ord('P'))

for i in range(1):
    class RPS():
        def __init__(self):
            self.player1_name = input("Please enter your name: ")
            self.player1 = (input('Select any one of the options \nRock(r), Paper(p) and Scissors(s): '))
            self.player1 = self.player1.lower()
            print(self.player1)
            self.sys_opt()

        def sys_opt(self):
            self.comp_selected = randint(1, 3)
            print(self.comp_selected)
            if self.comp_selected == 1:
                self.comp_player2 = 'r'
                print(self.comp_player2)
                self.check_win()
            elif self.comp_selected == 2:
                self.comp_player2 ='p'
                print(self.comp_player2)
                self.check_win()

            elif self.comp_selected == 3:
                self.comp_player2 = 's'
                print(self.comp_player2)
                self.check_win()

        def check_win(self):
            if self.player1 == self.comp_player2:
                print("Its a TIE !!")
                # break:
            elif self.player1 == 'r' and self.comp_player2 == 'p':
                print("Computer wins !!")
                # break
            elif self.player1 == 'p' and self.comp_player2 == 'r':
                print(self.player1_name," wins")
            elif self.player1 == 'p' and self.comp_player2 == 's':
                print("Computer wins !!")
            elif self.player1 == 's' and self.comp_player2 == 'p':
                print(self.player1_name," wins")
            elif self.player1 == 's' and self.comp_player2 == 'r':
                print("Computer wins !!")
            elif self.player1 == 'r' and self.comp_player2 == 's':
                print(self.player1_name," wins")

mycode = RPS()
# mycode.sys_opt()
# mycode.check_win()
