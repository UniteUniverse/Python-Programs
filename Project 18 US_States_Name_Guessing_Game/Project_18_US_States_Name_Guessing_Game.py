from turtle import*
import pandas

screen=Screen()
screen.title("U.S. State Game")
image="blank_states_img.gif"
screen.addshape(image)
shape(image)
data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()


guessed_states=[]

while len(guessed_states)<50:
    input_state=screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's the another state's name? Write 'Exit' to quit.").title()
    if input_state=="Exit":
        missing_states=[]
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break
    if input_state in all_states:
        guessed_states.append(input_state)
        t=Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==input_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(input_state)


