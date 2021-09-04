from tkinter import *
import tkinter as tk
from tkinter.ttk import *

root = Tk()

root.title("Juego del Ahorcado")
root.geometry("800x600")



def StartPlay():
    btnStart.pack_forget()
    entryCadena.pack()
    btnAccept.pack()
    string.pack()

def acceptString():
    btnAccept.pack_forget()
    entryCadena.pack_forget()
    string.pack_forget()
    EnteredChar()

def EnteredChar():
    lblEnterChar.pack()
    txtEnterChar.pack()
    btnIntent.pack()



string = tk.Label(text="Ingrese un texto")
txtCadena= StringVar()
entryCadena = tk.Entry(textvariable=txtCadena)

btnAccept = tk.Button(text="accept",command=acceptString)

lblEnterChar = tk.Label(text="Ingrese una letra")
char = StringVar()
txtEnterChar =  tk.Entry(textvariable=char)
btnIntent = tk.Button(text="Buscar")

stringEntered = tk.Label(background="green",width=60,text="BIENVENIDO AL JUEGO DEL AHORCADO",padx=20,pady=20,font=("Courier",20)).pack()
btnStart = tk.Button(text="Empezar el juego",pady=10,padx=10,command=StartPlay)

btnStart.pack()

root.mainloop()

