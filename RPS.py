#Program plays three games of rock, paper, scissors

# imports input program
from choice_choice import choice
def compare ( choice1, choice2):
    """compares rock, paper, scissors"""
    if choice1 == "rock":
        if choice2 == "rock":
          print ("tie")
        elif choice2 == "paper":
          print ("paper wins")
        elif choice2 == "scissors":
          print ("rock wins")
    elif choice1 == "paper":
        if choice2 == "rock":
          print ("paper wins")
        elif choice2 == "scissors":
          print ("scissors wins")
    else:
        if choice2 == "rock":
          print ("rock wins")
        elif choice2 == "paper":
          print ("scissors wins")
        elif choice2 == "scissors":
          print ("tie")


rounds = int(raw_input("Enter number of rounds: "))
player1_name = raw_input("Enter player1 name: ")
player2_name = raw_input("Enter player2 name: ")
counter = 0
while counter != 3:
    choice1 = choice()
    choice2 = choice()
    compare (choice1,choice2)
    counter += 1
    
print("Thanks for playing {} and {}!".format(player1_name, player2_name))

