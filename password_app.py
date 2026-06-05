import customtkinter as ctk
import random
import string
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4")
            return

        chars = ""

        if uppercase_var.get():
            chars += string.ascii_uppercase
        if lowercase_var.get():
            chars += string.ascii_lowercase
        if numbers_var.get():
            chars += string.digits
        if symbols_var.get():
            chars += string.punctuation

        if not chars:
            messagebox.showerror("Error", "Select at least one option")
            return

        password = ''.join(random.choice(chars) for _ in range(length))

        password_entry.delete(0, "end")
        password_entry.insert(0, password)

        check_strength(password)

    except ValueError:
        messagebox.showerror("Error", "Enter valid number")


def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        strength_label.configure(text="Strength: Weak", text_color="red")
    elif score == 3:
        strength_label.configure(text="Strength: Medium", text_color="orange")
    else:
        strength_label.configure(text="Strength: Strong", text_color="green")


def copy_password():
    password = password_entry.get()
    if password:
        app.clipboard_clear()
        app.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied successfully")


def clear_all():
    length_entry.delete(0, "end")
    password_entry.delete(0, "end")
    strength_label.configure(text="Strength: ", text_color="white")


app = ctk.CTk()
app.title("Secure Password Generator Pro")
app.geometry("550x650")

title = ctk.CTkLabel(
    app,
    text="Secure Password Generator Pro",
    font=("Arial", 24, "bold")
)
title.pack(pady=20)

length_entry = ctk.CTkEntry(
    app,
    placeholder_text="Enter Password Length",
    width=300
)
length_entry.pack(pady=10)

uppercase_var = ctk.BooleanVar(value=True)
lowercase_var = ctk.BooleanVar(value=True)
numbers_var = ctk.BooleanVar(value=True)
symbols_var = ctk.BooleanVar(value=True)

ctk.CTkCheckBox(app, text="Uppercase Letters", variable=uppercase_var).pack(pady=5)
ctk.CTkCheckBox(app, text="Lowercase Letters", variable=lowercase_var).pack(pady=5)
ctk.CTkCheckBox(app, text="Numbers", variable=numbers_var).pack(pady=5)
ctk.CTkCheckBox(app, text="Symbols", variable=symbols_var).pack(pady=5)

generate_btn = ctk.CTkButton(
    app,
    text="Generate Password",
    command=generate_password,
    width=220
)
generate_btn.pack(pady=10)

password_entry = ctk.CTkEntry(app, width=350)
password_entry.pack(pady=10)

copy_btn = ctk.CTkButton(
    app,
    text="Copy Password",
    command=copy_password,
    width=220
)
copy_btn.pack(pady=10)

clear_btn = ctk.CTkButton(
    app,
    text="Clear",
    command=clear_all,
    width=220
)
clear_btn.pack(pady=10)

strength_label = ctk.CTkLabel(
    app,
    text="Strength: ",
    font=("Arial", 18)
)
strength_label.pack(pady=20)

app.mainloop()