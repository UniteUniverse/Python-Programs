from tkinter import*
from pandas import *
from random import *
BACKGROUND_COLOR = "#B1DDC6"
try:
    data=read_csv("data\words_to_learn.csv")
except FileNotFoundError:
    original_data=read_csv("data\hindi_to_english- Sheet1.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")
current_card={}
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card=choice(to_learn)
    canvas.itemconfig(card_title, text="Hindi",fill="black")
    canvas.itemconfig(card_word, text=current_card["Hindi"], fill="black")
    canvas.itemconfig(card_background, image=front_card_img)
    flip_timer=window.after(3000, func=flip_card)
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"],fill="white") 
    canvas.itemconfig(card_background,image=back_card_img) 
def is_known():
    to_learn.remove(current_card)
    data=DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()
window=Tk()
window.title("Flash Card App")
window.config(padx=20,pady=20,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000, func=flip_card)
canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
front_card_img=PhotoImage(file="images\card_front.png")
back_card_img=PhotoImage(file="images\card_back.png")
card_background=canvas.create_image(400,263,image=front_card_img)
card_title=canvas.create_text(400,156,text="Title", font=("Arial",40,"italic"))
card_word=canvas.create_text(400,263,text="Word", font=("Arial",80,"bold"))
canvas.grid(column=0,row=0,columnspan=2)
cross_image=PhotoImage(file="images\wrong.png")
unknown_button=Button(image=cross_image,highlightthickness=0, command=next_card)
unknown_button.grid(column=0,row=1)
right_image=PhotoImage(file=r"images\right.png")
known_button=Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(column=1,row=1)

next_card()

window.mainloop()
