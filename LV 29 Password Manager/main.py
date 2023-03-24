from tkinter import *
from tkinter import messagebox
from pw_generator import PasswordGenerator
import pyperclip

pw_generator = PasswordGenerator()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def insert_password():
    input_pw.delete(0, END)
    password = pw_generator.generate_password()
    input_pw.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = input_website.get()
    user_mail = input_user_mail.get()
    pw = input_pw.get()
    
    if len(website) == 0 or len(user_mail) == 0 or len(pw) == 0:
        messagebox.showerror(title="Empty fields", message="Eines der Eingabefelder wurde nicht ausgefüllt.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Sie haben die folgenden Informationen für diese Seite hinzugefügt Sir: \nEmail: {user_mail} \nPasswort: {pw}.\n\n Ist das in Ordnung so.")
        if is_ok:
            with open("Lv 30 Password Manager 2 JSON Errorhandling/login_data.txt", mode="a") as login_data:
                login_data.write(f"{website} | {user_mail} | {pw} \n")
            login_data.close()
            clear_entry_fields()

def clear_entry_fields():
        input_website.delete(0, END)
        input_user_mail.delete(0, END)
        input_pw.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

# # # # # # # # # # # # # # # # # # # # # # # # # #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# # # # # # # # # # # # # # # # # # # # # # # # # #
# Canvas
canvas = Canvas(width=200, height=200)
lock = PhotoImage(file="Lv 30 Password Manager 2 JSON Errorhandling/logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(column=1, row=0)

# # # # # # # # # # # # # # # # # # # # # # # # # #
# Labels
lb_website = Label(text="Website:")
lb_website.grid(column=0, row=1, sticky="W")
lb_user_mail = Label(text="Email/Username:")
lb_user_mail.grid(column=0, row=2, sticky="W")
lb_pw = Label(text="Password:")
lb_pw.grid(column=0, row=3, sticky="W")

# # # # # # # # # # # # # # # # # # # # # # # # # #
# Buttons
btn_gen_password = Button(text="Generate Password", command=insert_password)
btn_gen_password.grid(column=2, row=3)
btn_add = Button(text="Add", width=30, command=save_data)
btn_add.grid(column=1, row=4, columnspan=2, sticky="W")

# # # # # # # # # # # # # # # # # # # # # # # # # #
# Entries
input_website = Entry(width=35)
input_website.grid(column=1, row=1, columnspan=2, sticky="W")
input_website.focus()
input_user_mail = Entry(width=35)
input_user_mail.grid(column=1, row=2, columnspan=2, sticky="W")
input_pw = Entry(width=21)
input_pw.grid(column=1, row=3, sticky="W")


window.mainloop()
