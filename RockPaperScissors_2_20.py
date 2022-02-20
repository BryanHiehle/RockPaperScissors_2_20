import random

cpu = random.randint(1,3)

#print(cpu)
print("Would you like to play the game?")
playGame = input()
if playGame == "Yes":

    while True:
        print("Pick one of the following numbers","\n 1 for Rock"
          "\n 2 for Paper"
          "\n 3 for Scissors")
        userSelect = input()
        if userSelect == "1":
            print("You picked Rock!")
        #Computer selection vs User selection
            if cpu == 1:
            #Computer selected Rock
                print("Computer picked Rock! \n Draw!")
            elif cpu == 2:
            #Computer selected Paper
                print("Computer picked Paper! \n You lose!")
            elif cpu == 3:
            #Computer selected Scissors
                print("Computer picked Scissors! \n You win!")
        elif userSelect == "2":
            print("You picked Paper!")
            #Computer selection vs User selection
            if cpu == 1:
            #Computer selected Rock
                print("Computer picked Rock! \n You win!")
            elif cpu == 2:
        #Computer selected Paper
                print("Computer picked Paper! \n Draw!")
            elif cpu == 3:
                #Computer selected Scissors
                print("Computer picked Scissors! \n You lose!")
        elif userSelect == "3":
            print("You picked Scissors")
            #Computer selection vs User selection
            if cpu == 1:
            #Computer selected Rock
                print("Computer picked Rock! \n You lose!")
            if cpu == 2:
        #Computer selected Paper
                print("Computer picked Paper! \n You win!")
            if cpu == 3:
            #Computer selected Scissors
                print("Computer picked Scissors! \n Draw!")
        print("Would you like to play again?")
        playRep = input()
        if playRep == "No":
            print("Thank you for playing Bryan's first project!")
            break


else:
    print("Thank you for playing Bryan's first python project!")
