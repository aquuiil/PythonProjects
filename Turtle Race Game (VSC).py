import turtle
import random
import time

#Setting up screen and turtle
s=turtle.Screen()
s.title('TURTLE RACE GAME!')
s.setup(width=700,height=700)
turtle.bgcolor('turquoise')
player_one=turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_two=player_one.clone()
player_two.color("blue")
player_two.penup()
player_one.goto(300,180)
player_one.pendown()
player_one.circle(20)
player_one.penup()
player_one.goto(-300,200)
player_two.goto(300,-220)
player_two.pendown()
player_two.circle(20)
player_two.penup()
player_two.goto(-300,-200)
die=[1,2,3,4,5,6]

for i in range(20):
    if player_one.pos() >= (300,200):
        print("\nPlayer 1 wins!!!\n")
        break
    elif player_two.pos() >= (300,-200):
        print("\nPlayer 2 wins!!!\n")
        break
    else:
        while player_one.pos() < (300,200) and player_two.pos() < (300,-200):
            time.sleep(1)
            player1_turn=input("\nPlayer 1: Press ENTER to roll dice\n")
            dice_outcome=random.choice(die)
            time.sleep(1)
            print("Your dice has rolled "+str(dice_outcome))
            player_one.fd(20*dice_outcome)
            break
        while player_one.pos() < (300,200) and player_two.pos() < (300,-200):
            time.sleep(1)
            player2_turn=input("\nPlayer 2: Press ENTER to roll dice\n")
            dice_outcome=random.choice(die)
            time.sleep(1)
            print("Your dice has rolled "+str(dice_outcome))
            player_two.fd(20*dice_outcome)
            break



        




