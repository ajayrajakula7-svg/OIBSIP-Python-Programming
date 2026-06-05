import customtkinter as ctk
from tkinter import messagebox
import json
import os
from datetime import datetime
import matplotlib.pyplot as plt

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

DATA_FILE = "user_data.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            content = file.read().strip()
            if not content:
                return []
            return json.loads(content)
    except:
        return []


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def clear_fields():
    name_entry.delete(0, "end")
    weight_entry.delete(0, "end")
    height_entry.delete(0, "end")
    result_text.set("")


def calculate_bmi():
    try:
        name = name_entry.get()
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())

        if not name:
            messagebox.showerror("Error", "Please enter your name")
            return

        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            category = "Underweight"
            advice = "Increase healthy calorie intake and exercise."
            color = "orange"
        elif bmi < 25:
            category = "Normal"
            advice = "Maintain your healthy lifestyle."
            color = "green"
        elif bmi < 30:
            category = "Overweight"
            advice = "Regular exercise and balanced diet recommended."
            color = "yellow"
        else:
            category = "Obese"
            advice = "Consult a doctor and follow a structured health plan."
            color = "red"

        result_text.set(
            f"BMI: {bmi:.2f}\nCategory: {category}\nAdvice: {advice}"
        )
        result_label.configure(text_color=color)

        data = load_data()
        data.append({
            "name": name,
            "weight": weight,
            "height_cm": height_cm,
            "bmi": round(bmi, 2),
            "category": category,
            "date": str(datetime.now())
        })
        save_data(data)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values")


def show_history():
    data = load_data()
    if not data:
        messagebox.showinfo("History", "No history found")
        return

    history = ""
    for entry in data:
        history += f"{entry['name']} - BMI: {entry['bmi']} ({entry['category']})\n"

    messagebox.showinfo("BMI History", history)


def show_chart():
    data = load_data()
    if not data:
        messagebox.showinfo("Chart", "No data available")
        return

    names = [entry["name"] for entry in data]
    bmi_values = [entry["bmi"] for entry in data]

    plt.figure(figsize=(6, 4))
    plt.bar(names, bmi_values)
    plt.title("BMI History Chart")
    plt.xlabel("Users")
    plt.ylabel("BMI")
    plt.show()


app = ctk.CTk()
app.title("Smart BMI Health Analyzer Pro")
app.geometry("550x650")

title = ctk.CTkLabel(
    app,
    text="Smart BMI Health Analyzer Pro",
    font=("Arial", 24, "bold")
)
title.pack(pady=20)

name_entry = ctk.CTkEntry(app, placeholder_text="Enter your name", width=320)
name_entry.pack(pady=10)

weight_entry = ctk.CTkEntry(app, placeholder_text="Enter weight (kg)", width=320)
weight_entry.pack(pady=10)

height_entry = ctk.CTkEntry(app, placeholder_text="Enter height (cm)", width=320)
height_entry.pack(pady=10)

calculate_btn = ctk.CTkButton(
    app,
    text="Calculate BMI",
    command=calculate_bmi,
    width=220
)
calculate_btn.pack(pady=10)

clear_btn = ctk.CTkButton(
    app,
    text="Clear",
    command=clear_fields,
    width=220
)
clear_btn.pack(pady=10)

history_btn = ctk.CTkButton(
    app,
    text="View BMI History",
    command=show_history,
    width=220
)
history_btn.pack(pady=10)

chart_btn = ctk.CTkButton(
    app,
    text="Show BMI Chart",
    command=show_chart,
    width=220
)
chart_btn.pack(pady=10)

result_text = ctk.StringVar()
result_label = ctk.CTkLabel(
    app,
    textvariable=result_text,
    font=("Arial", 16),
    wraplength=450
)
result_label.pack(pady=20)

app.mainloop()