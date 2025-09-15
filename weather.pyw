import tkinter as tk
import requests

API_KEY = "e656a8c1bef68e74402d18fbfcc51f3e"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

def get_weather():
    city = city_entry.get().strip()
    if not city:
        result_label.config(text="⚠️ Please enter a city name")
        return

    url = BASE_URL + f"q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        result_label.config(text="❌ City not found")
        return

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    weather = data["weather"][0]["main"]

    result_label.config(
        text=f"Weather in {city}\nCondition: {weather}\n🌡 Temp: {temp}°C\n💧 Humidity: {humidity}%\n🔽 Pressure: {pressure} hPa"
    )

# -------- GUI Setup --------
root = tk.Tk()
root.title("Weather App")
root.geometry("350x400")
root.resizable(False, False)

# Canvas for gradient background
canvas = tk.Canvas(root, width=350, height=400)
canvas.pack(fill="both", expand=True)

# Draw vertical gradient
def draw_gradient(canvas, color1, color2):
    for i in range(400):
        r1, g1, b1 = root.winfo_rgb(color1)
        r2, g2, b2 = root.winfo_rgb(color2)
        r = int(r1 + (r2 - r1) * i / 400) >> 8
        g = int(g1 + (g2 - g1) * i / 400) >> 8
        b = int(b1 + (b2 - b1) * i / 400) >> 8
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_line(0, i, 350, i, fill=color)

draw_gradient(canvas, "#010404", "#04080e")  # light blue → deep blue

# Entry for city
city_entry = tk.Entry(root, font=("Arial", 14), justify="center")
canvas.create_window(175, 50, window=city_entry, width=200)

# Search button
search_btn = tk.Button(root, text="Get Weather", font=("Arial", 12, "bold"),
                       bg="#000dff", fg="black", command=get_weather)
canvas.create_window(175, 100, window=search_btn, width=150, height=35)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14), justify="center", bg=None)
canvas.create_window(175, 250, window=result_label, width=300)

root.mainloop()
