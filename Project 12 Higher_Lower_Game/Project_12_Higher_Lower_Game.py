import art
import game_data
import random
import replit
i=0
k=True
while k==True:
    print(art.logo)
    compare_A=random.choice(game_data.data)
    compare_A=list(compare_A.values())
    n=0
    new_compare_A=[]
    while n<len(compare_A):
        if n==1:
            n+=1
            continue
        new_compare_A.append(str(compare_A[n]))
        n+=1
    print(f"Compare A: {', '.join(new_compare_A)}")
    print(art.vs)
    compare_B=random.choice(game_data.data)
    compare_B=list(compare_B.values())
    n=0
    new_compare_B=[]
    while n<len(compare_B):
        if n==1:
            n+=1
            continue
        new_compare_B.append(str(compare_B[n]))
        n+=1
    print(f"Compare B: {', '.join(new_compare_B)}")
    user_input=input("Who has more followers:? Type 'A' or 'B'").upper()
    if compare_A[1]>compare_B[1] and user_input=="A":
        i+=1
        print(f"You are right! Current score: {i}" )
        replit.clear()
    else:
        print(f"Sorry that's wrong! Final Score: {i}")
        k=False

