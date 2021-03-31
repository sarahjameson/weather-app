# imports
import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
import PIL
from PIL import ImageTk
from PIL import Image

# url for weather website
url = "https://weather.com/en-IE/weather/today/l/27f7448da771eafb4a2624954dcbbf1ac43688cbf81be0ddd18bcd3df14743fb"

master = Tk()
master.title("Weather App")
master.config(bg = "white")

img = Image.open("/Users/sarahjameson/Desktop/Resume Projects/weather_app/weather.png")
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

def weather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    location = soup.find("h1",class_="CurrentConditions--location--1Ayv3").text
    temperature = soup.find("span",class_="CurrentConditions--tempValue--3KcTQ").text
    weather_prediction = soup.find("div",class_="CurrentConditions--phraseValue--2xXSr").text
    
    location_label.config(text=location)
    temperature_label.config(text=temperature)
    weather_prediction_label.config(text=weather_prediction)

    temperature_label.after(60000,weather)
    master.update()

location_label = Label(master,font=("Calibri bold",20),bg="white")
location_label.grid(row=0,sticky="N",padx=100)
temperature_label = Label(master,font=("Calibri bold",70),bg="white")
temperature_label.grid(row=1,sticky="W",padx=40)
Label(master, image=img,bg="white").grid(row=1,sticky="E")
weather_prediction_label = Label(master,font=('Calibri Bold',15),bg="white")
weather_prediction_label.grid(row=2,sticky="W",padx=40)

weather()
master.mainloop()
