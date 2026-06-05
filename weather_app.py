import customtkinter as ctk
from tkinter import messagebox
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


weather_conditions = [
    "Sunny",
    "Cloudy",
    "Rainy",
    "Stormy",
    "Windy",
    "Foggy"
]


def get_weather():
    city = city_entry.get().strip()

    if city == "":
        messagebox.showerror("Error", "Please enter city name")
        return

    temp = random.randint(20, 38)
    humidity = random.randint(40, 95)
    wind = random.randint(2, 20)
    condition = random.choice(weather_conditions)

    result_label.configure(
        text=f"""
City: {city}

Temperature: {temp} °C
Humidity: {humidity}%
Wind Speed: {wind} km/h
Condition: {condition}
"""
    )


def clear_data():
    city_entry.delete(0, "end")
    result_label.configure(text="")


app = ctk.CTk()
app.title("Live Weather Dashboard Pro")
app.geometry("550x600")

title = ctk.CTkLabel(
    app,
    text="Live Weather Dashboard Pro",
    font=("Arial", 24, "bold")
)
title.pack(pady=20)

city_entry = ctk.CTkEntry(
    app,
    placeholder_text="Enter City Name",
    width=320
)
city_entry.pack(pady=20)

search_btn = ctk.CTkButton(
    app,
    text="Get Weather",
    command=get_weather,
    width=220
)
search_btn.pack(pady=10)

clear_btn = ctk.CTkButton(
    app,
    text="Clear",
    command=clear_data,
    width=220
)
clear_btn.pack(pady=10)

result_label = ctk.CTkLabel(
    app,
    text="",
    font=("Arial", 18),
    justify="left"
)
result_label.pack(pady=30)

app.mainloop()