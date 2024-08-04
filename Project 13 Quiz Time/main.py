from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
print('''                                                                 ,----,                                       
                                                                ,/   .`|                                       
    ,----..                                                   ,`   .'  :                     ____              
   /   /   \                      ,--,                      ;    ;     /   ,--,            ,'  , `.            
  /   .     :             ,--,  ,--.'|           ,----,   .'___,/    ,'  ,--.'|         ,-+-,.' _ |            
 .   /   ;.  \          ,'_ /|  |  |,          .'   .`|   |    :     |   |  |,       ,-+-. ;   , ||            
.   ;   /  ` ;     .--. |  | :  `--'_       .'   .'  .'   ;    |.';  ;   `--'_      ,--.'|'   |  ||    ,---.   
;   |  ; \ ; |   ,'_ /| :  . |  ,' ,'|    ,---, '   ./    `----'  |  |   ,' ,'|    |   |  ,', |  |,   /     \  
|   :  | ; | '   |  ' | |  . .  '  | |    ;   | .'  /         '   :  ;   '  | |    |   | /  | |--'   /    /  | 
.   |  ' ' ' :   |  | ' |  | |  |  | :    `---' /  ;--,       |   |  '   |  | :    |   : |  | ,     .    ' / | 
'   ;  \; /  |   :  | : ;  ; |  '  : |__    /  /  / .`|       '   :  |   '  : |__  |   : |  |/      '   ;   /| 
 \   \  ',  . \  '  :  `--'   \ |  | '.'| ./__;     .'        ;   |.'    |  | '.'| |   | |`-'       '   |  / | 
  ;   :      ; | :  ,      .-./ ;  :    ; ;   |  .'           '---'      ;  :    ; |   ;/           |   :    | 
   \   \ .'`--"   `--`----'     |  ,   /  `---'                          |  ,   /  '---'             \   \  /  
    `---`                        ---`-'                                   ---`-'                      `----'   
                                                                                                               
''')
question_bank=[]
n=0
while n<len(question_data):
    new_Question=Question(question_data[n]["text"],question_data[n]["answer"])
    question_bank.append(new_Question)
    n+=1

quiz=QuizBrain(question_bank)
quiz.next_question()
while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
