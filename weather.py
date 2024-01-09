import customtkinter
import requests

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

api_key = '94ee22f2cdc025d7d753b74d2d7ce109'

weather_icons = {
    "Clear": "☀️ Sunny",
    "Clouds": "☁️ Cloudy",
    "Rain": "🌧️ Rain",
    "Thunderstorm": "⛈️ Storm",
    "Snow": "❄️ Snow",
    "Partly Cloudy": "⛅ Partly Sunny"
}

def get_weather():
    client_input = city_entry.get()
    try:
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={client_input}&units=metric&APPID={api_key}")
        weather = weather_data.json()['weather'][0]['main']
        temp = weather_data.json()['main']['temp']
        
        result_label.configure(text=f"{client_input}\n{temp}°C\n{weather_icons.get(weather, "")} ", pady=10)

        
     

    except Exception as e:
        result_label.configure(text="Invalid City")
        icon_label.configure(text="")

# Create main application window
app = customtkinter.CTk()
app.geometry("300x300")
app.resizable(False, False)
app.title("Weather App")

# Create and place GUI elements
label = customtkinter.CTkLabel(app, text="Type your city", font=("Helvetica", 16))
label.pack(pady=10)

city_entry = customtkinter.CTkEntry(app, font=("Helvetica", 14))
city_entry.pack(pady=10)

search_button = customtkinter.CTkButton(app, text="Search", command=get_weather, font=("Helvetica", 14))
search_button.pack(pady=10)

result_label = customtkinter.CTkLabel(app, text="", font=("Helvetica", 14), wraplength=600)
result_label.pack(pady=10)

# Label to display weather icon
icon_label = customtkinter.CTkLabel(app, text="", font=("Helvetica", 14))
icon_label.pack(pady=10)

app.mainloop()