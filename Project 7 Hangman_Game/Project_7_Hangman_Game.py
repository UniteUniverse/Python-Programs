import random
word_list=["google", "microsoft", "amazon", "meta", "netflix", "tata", "adani", "jio"]
print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    ''')
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
t=len(stages)
il_stages=t-1
random_word=list(random.choice(word_list))

n=0
blank_list=[]
while n!=len(random_word):
    blank_list+="_"
    n+=1
print(blank_list)
j=blank_list.count("_")
while blank_list!=random_word:
    guess=input("Guess a letter: ").lower()
    if guess in random_word:
        print(stages[il_stages])
    else:
        print(stages[il_stages-1])
        il_stages-=1
    if il_stages==0:
        print("You lose")
        break
    i=0
    while i!=len(random_word):
        if random_word[i]==guess:
            blank_list[i]=guess
        i+=1    
    print(blank_list)
if blank_list==random_word:
    print("You won")