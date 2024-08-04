from tkinter import*
from tkinter import messagebox
import json
import random
import pyperclip
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list+=[random.choice(letters) for char in range(nr_letters)]
    password_list+=[random.choice(symbols) for char in range(nr_symbols)]
    password_list+=[random.choice(numbers) for char in range(nr_numbers)]
    random.shuffle(password_list)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    input_password.insert(0,password)
    pyperclip.copy(password)

def find_password():
    website=input_website.get()
    try:
        with open("data.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No data file found.")
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Missing",message="Data not found.")
def save():
    website=input_website.get()
    email=input_email.get()
    password=input_password.get()
    new_data={
        website:{
            "email":email,
            "password":password
        }
    }
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any field empty.")
    else:
        is_ok=messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save?")
        
        if is_ok:
            try:  
                with open("data.json","r") as data_file:
                    data=json.load(data_file)
                    data.update(new_data)
                
            except FileNotFoundError:
                with open("data.json","w") as data_file:
                    json.dump(new_data,data_file,indent=4)
            else:
                with open("data.json","w") as data_file:
                    json.dump(data,data_file,indent=4)
            finally:
                input_website.delete(0,END)
                input_password.delete(0,END)
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
canvas=Canvas(width=200,height=200)
lock_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(row=0,column=1)

label_website=Label(text="Website:")
label_website.grid(row=1,column=0)
label_email=Label(text="Email/Username:")
label_email.grid(row=2,column=0)
label_Password=Label(text="Password:")
label_Password.grid(row=3,column=0)
input_website=Entry(width=35)
input_website.grid(row=1,column=1,)
button_search=Button(text="Search",command=find_password)
button_search.grid(column=2,row=1)
input_email=Entry(width=35)
input_email.grid(row=2,column=1,)
input_email.insert(0,"pratyush.snj@gmail.com")
input_password=Entry(width=35,)
input_password.grid(row=3,column=1,)
button_generate=Button(text="Generate Password",command=generate_password)
button_generate.grid(row=3,column=2,)
button_add=Button(text="Add",width=36,command=save)
button_add.grid(row=4,column=0,columnspan=3)

window.mainloop()