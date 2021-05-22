import tkinter as tk
from tkinter import *
from senAna import setData
import pandas as pd

df = pd.DataFrame()
polarity = 0.0056
window = tk.Tk()

window.title("Sentiment Analysis")
window.geometry("1300x700")

label1 = tk.Label(text="SENTIMENT ANALYSIS", bg="yellow",fg="red", font=("ALGERIAN","32"))
label1.place(x=400,y=0)
label2 = tk.Label(text="   ")
label2.grid(column=0,row=1)
label2 = tk.Label(text="   ")
label2.grid(column=0,row=2)
label2 = tk.Label(text="   ")
label2.grid(column=0,row=3)
label2 = tk.Label(text="   ")
label2.grid(column=0,row=4)
label2 = tk.Label(text="Enter the details for API",font="Castellar")
label2.place(x=60,y=100)


label2 = tk.Label(text="Api Key", font="Forte")
label2.grid(column=2,row=5)
e1 = Entry(window, width=65, borderwidth=5)
e1.grid(row=5, column=3, columnspan=3, padx=10, pady=10)

label2 = tk.Label(text="Api Secret Key", font="Forte")
label2.grid(column=2,row=6)
e2 = Entry(window, width=65, borderwidth=5)
e2.grid(row=6, column=3, columnspan=3, padx=10, pady=10)

label2 = tk.Label(text="Access Token", font="Forte")
label2.grid(column=2,row=7)
e3 = Entry(window, width=65, borderwidth=5)
e3.grid(row=7, column=3, columnspan=3, padx=10, pady=10)

label2 = tk.Label(text="Secret Access Token", font="Forte")
label2.grid(column=2,row=8)
e4 = Entry(window, width=65, borderwidth=5)
e4.grid(row=8, column=3, columnspan=3, padx=10, pady=10)

def getInfo():
    apiKey = e1.get()
    apiKeySecret = e2.get()
    accessToken = e3.get()
    accessTokenSecret = e4.get()
    empty = Exception
    try:
        if apiKey=='' or apiKeySecret=='' or accessToken=='' or accessTokenSecret=='':
            raise empty
    except empty:
        display = tk.Text(master=window, height=6, width=35)
        display.grid(column=3, row=14)
        display.insert(tk.END, "CREDENTIALS ARE EMPTY")
    else:
        try:
            df, polarity = setData(apiKey, apiKeySecret, accessToken, accessTokenSecret)
            label3 = tk.Label(text="POLARITY", fg="blue", font=("Forte", "20"))
            label3.place(x=275, y=375)
            display = tk.Text(master=window, height=6, width=35)
            display.grid(column=3, row=14)
            display.insert(tk.END, "POLARITY = {}".format(polarity))
            print(df)
        except Exception:
            display = tk.Text(master=window, height=6, width=25)
            display.grid(column=3, row=14)
            display.insert(tk.END, "WRONG CREDENTIALS")

label2=tk.Label(text = "   ")
label2.grid(column=0, row=9)

label2 = tk.Label(text = " Press Done Button to run the Program.",font="Castellar")
label2.grid(column=1, row=11)

button = tk.Button(text=" DONE ", font="Stencil", command=getInfo)
button.grid(column=3, row=12, columnspan=3, padx=10, pady=10)
window.mainloop()