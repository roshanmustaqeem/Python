# import random 
# num1=10
# num2=20

# ch=random.randint(num1,num2)
# print("------------Nubmer guessing game--------- ")
# print(f"enter a number between {num1} and {num2} ")
# guesses=0
# while True:
#   guess=int(input("enter your guess: "))
#   guesses+=1

#   if guess<num1:
#     print("guess is low , guess a higher nubmer")
#   elif guess>num2:
#     print("guess is higher, guess a lower number")
#   elif guess==ch:
#     print(f"your guess was correct the numer was{guess}")
#     print(f"nubmer of guesses taken :{guesses}")
#     print("------------end of guessing game--------- ")
#     break

import random 

choices=("stone","paper","scissors")
print("-------welcome to game-------")
print("stone","paper","scissors")
while True:
    user=None
    computer=random.choice(choices)
    while user not in choices: 
     user=input("enter your choice: ")
    print(f"player:{user}")
    print(f"computer:{computer}")
    if user=="stone" and computer=="scissors":
     print("you won!")
    elif user=="paper" and computer=="stone":
     print("you won!")
    elif user=="scissors" and computer=="paper":
     print("you won!")
    elif user==computer:
     print("its a tie")
    else:
        print("you lost")
    question=input("do you wanna play again?(y/n): ")
    if question!="y":
        break
print("thanks for playing!")