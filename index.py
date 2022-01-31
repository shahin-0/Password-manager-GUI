from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    passEntry.insert(0, password)
    pyperclip.copy(password)

def save():
    
    website = webEntry.get()
    email = userEntry.get()
    password = passEntry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                    f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                webEntry.delete(0, END)
                passEntry.delete(0, END)

# UI begins here
window = Tk()
window.title("PyLock")
window.minsize(height=650,width=800)

canvas = Canvas(height=250,width=250)
logo = PhotoImage(file="password_manager\logo.png")
canvas.create_image(100, 100, image=logo)
canvas.place(x=330,y=50)

webHead = Label(text="Website", font="Nunito")
emailHead = Label(text="E-mail/Username", font="Nunito")
passHead = Label(text="Password", font="Nunito")

webHead.place(x=150,y=340)
emailHead.place(x=150,y=370)
passHead.place(x=150,y=400)

webEntry = Entry(width=35)
userEntry = Entry(width=35)
passEntry = Entry(width=35)

webEntry.place(x=330,y=350)
userEntry.place(x=330,y=380)
passEntry.place(x=330,y=410)

genButton = Button(text="Generate",width=10,command=generate_password)
addButton = Button(text="Add", width=10, height=1,command=save)


genButton.place(x=550,y=405)
addButton.place(x=370,y=470)

#UI ends here



window.mainloop()
