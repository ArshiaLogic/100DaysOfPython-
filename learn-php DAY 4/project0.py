import random

player = int(input("What do you choose? Type 0 for Rock, 1 for paper, 2 for Sciossors: "))
#--------------------Crash handeler--------------------
if player > 2:
    print("Please put right number")
else:

    #--------------------Hands--------------------

    rock = '''

        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)

    '''

    paper = '''

        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)

    '''

    Sciossors = '''

        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)

    '''

    #--------------------Lists--------------------
    hands = [rock, paper, Sciossors]

    #--------------------computer brain--------------------
    computer_chose = random.randint(0, 2)




    #--------------------What player see--------------------
    print(hands[player])
    print(f"computer chose: {hands[computer_chose]}")

    #--------------------------------Conditions--------------------------------

    #--------------------Tie--------------------
    if computer_chose == player:
        print("Tie")
    #--------------rock and Sciossors--------------
    elif player == 2 and computer_chose == 0:
        print("You lose") 
    elif player == 0 and computer_chose == 2:
        print("You win")
    #--------------rock and paper--------------
    elif player ==0  and computer_chose ==1 :
        print("You lose") 
    elif player ==1  and computer_chose ==0 :
        print("You win")         
    #--------------paper and Sciossors--------------
    elif player ==1  and computer_chose ==2 :
        print("You lose") 
    elif player ==2  and computer_chose ==1 :
        print("You win")       

