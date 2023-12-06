import tkinter as tk
from tkmacosx import Button
import requests


def fwd():
   requests.request(method='GET', url="http://192.168.1.116:8080/fwd")
   print("The robot has moved forward")


def rvs():
   requests.request(method='GET', url="http://192.168.1.116:8080/rev")
   print("The robot has moved backwards")


def right():
   requests.request(method='GET', url="http://192.168.1.116:8080/right")
   print("The robot has turned right")


def left():
   requests.request(method='GET', url="http://192.168.1.116:8080/left")
   print("The robot has turned left")


window = tk.Tk()
label = tk.Label(text="Welcome to Sarah's Python GUI!", font=[('calibri', 'bold')], fg="black", bg="white",
                highlightbackground="#7ec0ee")


fwdbutton = tk.Button(text="Forward", font='calibri', fg="blue", bg="white", width=35, height=5, command=fwd)
revbutton = tk.Button(text="Reverse", font="calibri", fg="blue", bg='#54FA9B', width=35, height=5, command=rvs)
leftbutton = tk.Button(text="Right turn", font="calibri", fg="blue", bg="orange", width=35, height=5, command=right)
rightbutton = tk.Button(text="Left turn", font="calibri", fg="blue", bg="purple", width=35, height=5, command=left)


def handle_keypress(event):
   fwd()
   print(event.char)


window.bind("<Key>", handle_keypress)


label.pack()
fwdbutton.pack()
revbutton.pack()
leftbutton.pack()
rightbutton.pack()
window.mainloop()

