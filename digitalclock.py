import tkinter as tk
from tkinter import *
from time import strftime

def Createwidgets():
    root.dateLabel=Label(root,text="DATE : "+strftime("%d/%m/%Y"),font=("Helvetica",50), bg="skyblue",fg="white")
    root.dateLabel.grid(sticky="nw")
    root.timeLabel=Label(root,font=("Helvetica",100),bg="skyblue",fg="white")
    root.timeLabel.grid(sticky="news")
    updateTime()
def updateTime():
        root.timeLabel.config(text=strftime("%H:%M:%S"))
        root.timeLabel.after(1000,updateTime)
root=tk.Tk()
root.title("DIGITAL CLOCK")
root.config(bg="skyblue")
root.resizable(False,False)
Createwidgets()
root.mainloop()
