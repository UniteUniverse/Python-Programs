import random
rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")


paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")


scissor=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
game=[rock,paper,scissor]
user=int(input("Type 0 for rock, 1 for paper, 2 for scissor: "))
user1=game[user]
user_print=print(user1)
computer=game[random.randint(0,2)]
computer_print=print(computer)
if user1==rock and computer==scissor:
    print("You won the game.")
elif user1==scissor and computer==paper:
    print("You won the game.")
elif user1==paper and computer==rock:
    print("You won the game.")
elif user1==computer:
    print("Tie")
else:
    print("You lose")