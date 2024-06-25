import random
class RockPaperScissors:
    def __init__(self) :
        self.choices={1:"Rock",2:"Paper",3:"Scissors"}
        self.user_score=0
        self.comp_score=0
    def get_user_choice(self):
        while True:
            user_choice=input("Choose your move (1 for Rock ,2 for paper and 3 for scissors)")
            if user_choice in ["1","2","3"]:
                return int(user_choice)
            else:
                print("Please enter a valid choice!")
    def get_comp_choice(self):
        return random.randint(1,3)
    
    def who_wins(self,user_choice,comp_choice):
        if user_choice==comp_choice:
            return "Tie!"
        elif(user_choice==1 and comp_choice==3) or (user_choice==2 and comp_choice==1) or (user_choice==3 and comp_choice==2):
            self.user_score+=1
            return "YOU WIN! YOU GOT A POINT"
        else:
            self.comp_score+=1
            return "Computer wins!!"



    def play_game(self):
        while True:
            user_choice=self.get_user_choice()
            comp_choice=self.get_comp_choice()
            print(f"you chose:{self.choices[user_choice]}")
            print(f"Computers choice:{self.choices[comp_choice]}")

            result=self.who_wins(user_choice,comp_choice)
            print(result)
            print(f"Score -You:{self.user_score},Computer:{self.comp_score}")

            play_again=input("Do you want to play again? (Y/N):")
            if play_again.lower=="n":
                break
        print("Thanks for playing!:-")



if __name__=="__main__":
    game=RockPaperScissors()
    game.play_game()
