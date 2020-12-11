import tkinter as tk
import requests
from tkmacosx import Button

def forward():
    print("Successful Execution: Forward")
    requests.request(method = 'GET', url="http://192.168.1.116:8080/fwd")


def reverse():
    print("Successful Execution: Reverse")
    requests.request(method='GET', url="http://192.168.1.116:8080/rev")


def right():
    print("Successful Execution: Right")
    requests.request(method='GET', url="http://192.168.1.116:8080/right")


def left():
    print("Successful Execution: Left")
    requests.request(method='GET', url="http://192.168.1.116:8080/left")


def run():
    print("You're gonna regret that\n")
    requests.request(method = 'GET', url="http://192.168.1.116:8080/run?a=3&b=0.7&c=1.9&d=0.8&e=0.7&f=3.15")

window = tk.Tk()
window.columnconfigure([0,2], minsize=250)
window.rowconfigure([0, 2], minsize=100)
window.title("PyUI v2.6.2 BETA")
label = tk.Label(
    text = "Welcome to PyUI\u2122!\nCopyright \u00A9 2020 Alizain Fatehali\nDelicious, LLC\n A subdivision of "
           "SCRUMptious, INC.", foreground = "white", background = "black", width = 25, height = 10)
label.grid(row = 1, column = 1)

button1 = tk.Button(text = "Forward", foreground = "blue", background = "purple", width = 25, height = 10,
                    command =forward)
button1.grid(row=0, column=1, sticky="n")

button2 = tk.Button(text = "Reverse", foreground = "green", background = "blue", width = 25, height = 10,
                    command = reverse)
button2.grid(row=2, column=1, sticky="s")

button3 = tk.Button(text = "Right", foreground = "purple", background = "red", width = 25, height = 10,
                    command = right)
button3.grid(row=1, column=2, sticky="e")

button4 = tk.Button(text = "Left", foreground = "red", background = "orange", width = 25, height = 10,
                    command = left)
button4.grid(row=1, column=0, sticky="w")

run = tk.Button(text = "DANGER:\nDO NOT PRESS", foreground = "red", background = "orange", width = 25, height = 10,
                    command = run)
run.grid(row = 0, column = 2)


def tryfwd(event):
    forward()


def tryrev(event):
    reverse()


def tryright(event):
    right()


def tryleft(event):
    left()


window.bind("<w>", tryfwd)
window.bind("<s>", tryrev)
window.bind("<d>", tryright)
window.bind("<a>", tryleft)
window.bind("<Up>", tryfwd)
window.bind("<Down>", tryrev)
window.bind("<Left>", tryleft)
window.bind("<Right>", tryright)


#label.pack()
# button1.pack()
# button2.pack()
# button3.pack()
# button4.pack()


window.mainloop()
