import random
print('''
   _____                      _______ _            _   _                 _               
  / ____|                    |__   __| |          | \ | |               | |              
 | |  __ _   _  ___ ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ / __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ | '__|
 | |__| | |_| |  __\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __| |   
  \_____|\__,_|\___|___|___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                         
                                                                                         
''')
print("Welcome to the Number Guessing Game.")
print("I'm thinking of a number between 1 to 100.")
correct_number=random.randint(1,101)
difficulty=input("Choose the difficulty. Type easy or hard: ").lower()
e=10
h=5
if difficulty=="easy":
    while(e!=0):
        print(f"You have {e} attempts remaining to guess the number.")
        guess_number=int(input("Make a Guess: "))
        if guess_number==correct_number:
            print("You got it!")
            break
        e-=1
    if e==0:
        print("You Lose!")

elif difficulty=="hard":
    while(h!=0):
        print(f"You have {h} attempts remaining to guess the number.")
        guess_number=int(input("Make a Guess: "))
        if guess_number==correct_number:
            print("You got it!")
            break
        h-=1
    if h==0:
        print("You Lose!")