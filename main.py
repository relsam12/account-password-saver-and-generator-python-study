from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ------------------------- FINDING THE EXIST ACCOUNT ----------------------------#
def find_account():
    website_name = text_box_website.get()
    try:
        with open("data.json", "r") as data:
            finding_acc = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR!!!", message="File not Found!!!")
    else:
        if website_name in finding_acc:
            acc_email = finding_acc[website_name]["email_usname"]
            acc_pass = finding_acc[website_name]["password"]
            messagebox.showinfo(title=website_name, message=f"Email/Username : {acc_email}\n"
                                                            f"Account Password : {acc_pass}")
        else:
            messagebox.showinfo(title="ERROR!!!", message=f"The Account of {website_name} is doesn't exist")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    text_box_password.insert(END, string=f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_data = text_box_website.get()
    username_email_data = text_box_email_username.get()
    password_data = text_box_password.get()
    new_data = {
        website_data: {
            "email_usname": username_email_data,
            "password": password_data
        }}

    if len(website_data) == 0 or len(username_email_data) == 0 or len(password_data) == 0:
        messagebox.showwarning(title="Caution !!!", message="Don't Leave any field blank !!!")
    else:
        # using the Catching Exceptions Error 👇
        try:
            with open("data.json", mode="r") as data:
                # we do 3 steps with JSON:
                # 1. reading the data
                read_data = json.load(data)
        except FileNotFoundError:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)
        else:
            # 2. updating the old data with the new data
            read_data.update(new_data)
            with open("data.json", "w") as data:
                # 3. saving the updated data to the data file.json
                json.dump(read_data, data, indent=4)
        finally:
            text_box_website.delete(0, END)
            text_box_email_username.delete(0, END)
            text_box_password.delete(0, END)
            text_box_email_username.insert(END, string="example@gmail.com/example1234")
            text_box_website.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

label_email_username = Label(text="Email/Username:")
label_email_username.grid(column=0, row=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

text_box_website = Entry(width=35)
text_box_website.grid(column=1, row=1)
text_box_website.focus()

text_box_email_username = Entry(width=54)
text_box_email_username.grid(column=1, row=2, columnspan=3)
text_box_email_username.insert(END, string="example@gmail.com/example1234")

text_box_password = Entry(width=35)
text_box_password.grid(column=1, row=3)

check_account_button = Button(text="Check Account", width=15, command=find_account)
check_account_button.grid(column=2, row=1)

button_add = Button(text="Add", width=46, command=save)
button_add.grid(column=1, row=4, columnspan=3)

button_generate_pass = Button(text="Generate Password", command=generator_password, width=15)
button_generate_pass.grid(column=2, row=3, columnspan=2)

window.mainloop()
