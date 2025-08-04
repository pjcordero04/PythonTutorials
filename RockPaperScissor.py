import random


rps = ["rock", "paper", "scissor"]
user_in = -1
your_score = 0
opponent_score = 0

print("This is a best of 5 rock, paper and scissor game. Good luck!")
while(your_score<3 and opponent_score<3):

    user_in = int(input("Press 1 for rock, 2 for paper and 3 for sscissor.\nPress 4 to end the game\n"))
    if(user_in == 4):
        break

    r = random.randint(0,2)
    print(f"You chose: {rps[user_in-1]} and opponent chose: {rps[r]}")

    if rps[user_in-1] == "rock" and rps[r] == "scissor":
        print("You win!")
        your_score+=1
        print(f"Score\t you: {your_score}\t opponent: {opponent_score}\n")

    elif rps[user_in-1] == "paper" and rps[r] == "rock":
        print("You win!")
        your_score+=1
        print(f"Score\t you: {your_score}\t opponent: {opponent_score}\n")
 
    elif rps[user_in-1] == "scissor" and rps[r] == "paper":
        print("You win!")
        your_score+=1
        print(f"Score\t you: {your_score}\t opponent: {opponent_score}\n")

    elif user_in-1 == r:
        print("It's a draw!")

    else:
        print("You lose!")
        opponent_score+=1
        print(f"Score\t you: {your_score}\t opponent: {opponent_score}\n")

if(your_score>=3 or opponent_score>=3):
    if(your_score>opponent_score):
        print("You won the best of 5!")
    else:
        print("You lose the best of 5!")