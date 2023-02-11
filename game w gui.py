#Name: Wyatt Avilla
#Date: 11-26-22
#Functionality: Creates windows with buttons that interact and synchronize with class Fifteen
from tkinter import *
import tkinter.font as font
from fifteen import Fifteen

fifteen = Fifteen()

gui = Tk()  #Houses game tiles
gui.title("Game Tiles")
f = font.Font(family='Helveca', size='12', weight='bold')


def update_button_vals(): #changes button color and state based off tiles from instance of class Fifteen
    buttons = [button0, button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15]
    button_text_vars = [b0txt, b1txt, b2txt, b3txt, b4txt, b5txt, b6txt, b7txt, b8txt, b9txt, b10txt, b11txt, b12txt, b13txt, b14txt, b15txt]
    for x in range(16):
        button_text_vars[x].set(fifteen.tiles[x])
        (buttons[x])["bg"] = "mediumpurple"
        (buttons[x])["state"] = "normal"
        if fifteen.tiles[x] == 0:
            (button_text_vars[x]).set("")
            (buttons[x])["bg"] = "mediumpurple4"
            (buttons[x])["state"] = "disabled"

    if fifteen.is_solved():
        print("game over !")

def button_press(val):  #checks if valid move, updates board state accordingly
    tile_value = fifteen.tiles[val]
    if fifteen.is_valid_move(tile_value):
        fifteen.update(tile_value)
    update_button_vals()
    

def shuffle_button_click(): #shuffles puzzle on click
    fifteen.shuffle()
    update_button_vals()

def solve_button_click():  #solves puzzle on click
    fifteen.solve()
    update_button_vals()

b0txt = StringVar()    #Instantiating string variables for tile buttons
b1txt = StringVar()
b2txt = StringVar()
b3txt = StringVar()
b4txt = StringVar()
b5txt = StringVar()
b6txt = StringVar()
b7txt = StringVar()
b8txt = StringVar()
b9txt = StringVar()
b10txt = StringVar()
b11txt = StringVar()
b12txt = StringVar()
b13txt = StringVar()
b14txt = StringVar()
b15txt = StringVar()

#Instatiates all buttons and binds them to button_press(val) with the val corresponding to the button's number 
button0 = Button(textvariable=b0txt, font=f, activebackground="mediumpurple4", width=20, height=10, bg='mediumpurple', fg='black', command=lambda:button_press(0))
button0.grid(row=1, column=0)
button1 = Button(textvariable=b1txt, font=f, activebackground="mediumpurple4", width=20, height=10, bg='mediumpurple', fg='black', command=lambda:button_press(1))
button1.grid(row=1, column=1)
button2 = Button(textvariable=b2txt, font=f, activebackground="mediumpurple4", width=20, height=10, bg='mediumpurple', fg='black', command=lambda:button_press(2))
button2.grid(row=1, column=2)
button3 = Button(textvariable=b3txt, font=f, activebackground="mediumpurple4", width=20, height=10, bg='mediumpurple', fg='black', command=lambda:button_press(3))
button3.grid(row=1, column=3)
button4 = Button(textvariable=b4txt, font=f, activebackground="mediumpurple4", width=20, height=10, bg='mediumpurple', fg='black', command=lambda:button_press(4))
button4.grid(row=2, column=0)
button5 = Button(textvariable=b5txt, font=f, activebackground="mediumpurple4", width=20, height=10, bg='mediumpurple', fg='black', command=lambda:button_press(5))
button5.grid(row=2, column=1)
button6 = Button(textvariable=b6txt, font=f, activebackground="mediumpurple4", width=20, height=10, bg='mediumpurple', fg='black', command=lambda:button_press(6))
button6.grid(row=2, column=2)
button7 = Button(textvariable=b7txt, font=f, activebackground="mediumpurple4", width=20, height=10, bg='mediumpurple', fg='black', command=lambda:button_press(7))
button7.grid(row=2, column=3)
button8 = Button(textvariable=b8txt, font=f, activebackground="mediumpurple4", width=20, height=10, bg='mediumpurple', fg='black', command=lambda:button_press(8))
button8.grid(row=3, column=0)
button9 = Button(textvariable=b9txt, font=f, activebackground="mediumpurple4", width=20, height=10, bg='mediumpurple', fg='black', command=lambda:button_press(9))
button9.grid(row=3, column=1)
button10 = Button(textvariable=b10txt, font=f, activebackground="mediumpurple4", width=20, height=10, bg='mediumpurple', fg='black', command=lambda:button_press(10))
button10.grid(row=3, column=2)
button11 = Button(textvariable=b11txt, font=f, activebackground="mediumpurple4", width=20, height=10, bg='mediumpurple', fg='black', command=lambda:button_press(11))
button11.grid(row=3, column=3)
button12 = Button(textvariable=b12txt, font=f, activebackground="mediumpurple4", width=20, height=10, bg='mediumpurple', fg='black', command=lambda:button_press(12))
button12.grid(row=4, column=0)
button13 = Button(textvariable=b13txt, font=f, activebackground="mediumpurple4", width=20, height=10, bg='mediumpurple', fg='black', command=lambda:button_press(13))
button13.grid(row=4, column=1)
button14 = Button(textvariable=b14txt, font=f, activebackground="mediumpurple4", width=20, height=10, bg='mediumpurple', fg='black', command=lambda:button_press(14))
button14.grid(row=4, column=2)
button15 = Button(textvariable=b15txt, font=f, activebackground="mediumpurple4", width=20, height=10, bg='mediumpurple', fg='black', command=lambda:button_press(15))
button15.grid(row=4, column=3)

shuffle_button = Button(font=f, activebackground="snow4", width=20, height=10, bg = "snow3", text="Shuffle", command=lambda:shuffle_button_click())
shuffle_button.grid(row=5,column=1)

solve_button = Button(font=f, activebackground="snow4", width=20, height=10, bg = "snow3", text="Solve", command=lambda:solve_button_click())
solve_button.grid(row=5, column=2)

update_button_vals()
mainloop()

