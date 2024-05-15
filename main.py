from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=befadb78791ca79af1bdf504e223ab13").json()
    w_lebal1.config(text=data["weather"][0]["main"])
    wb_lebal1.config(text=data["weather"][0]["description"])
    temp_lebal1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_lebal1.config(text=data["main"]["pressure"])    

    
win = Tk()
win.title("ALI")
win.config(bg = "blue")
win.geometry("500x570")
name_lebal = Label(win,text="Ali Weather App",font=("Time New Roman",40,"bold"))
name_lebal.place(x=25,y=50,height=50,width=450)

city_name = StringVar()
list_name = ["Karachi", "Lahore", "Islamabad", "Peshawar", "Multan"]
com = ttk.Combobox(win,text="Ali Weather App",values=list_name,font=("Time New Roman",20,"bold"),textvariable=city_name)

com.place(x=25,y=120,height=50,width=450)


w_lebal = Label(win,text="Weather Climate",font=("Time New Roman",20))
w_lebal.place(x=25,y=260,height=50,width=210)

w_lebal1 = Label(win,text="",font=("Time New Roman",20))
w_lebal1.place(x=250,y=260,height=50,width=210)



wb_lebal = Label(win,text="Weather Description",font=("Time New Roman",16))
wb_lebal.place(x=25,y=330,height=50,width=210)

wb_lebal1 = Label(win,text="",font=("Time New Roman",17))
wb_lebal1.place(x=250,y=330,height=50,width=210)



temp_lebal = Label(win,text="Temperature",font=("Time New Roman",20))
temp_lebal.place(x=25,y=400,height=50,width=210)

temp_lebal1 = Label(win,text="",font=("Time New Roman",20))
temp_lebal1.place(x=250,y=400,height=50,width=210)



per_lebal = Label(win,text="Pressure",font=("Time New Roman",20))
per_lebal.place(x=25,y=470,height=50,width=210)

per_lebal1 = Label(win,text="",font=("Time New Roman",20))
per_lebal1.place(x=250,y=470,height=50,width=210)

done_button = Button(win,text="Done",font=("Time New Roman",20,"bold"),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)




win.mainloop()