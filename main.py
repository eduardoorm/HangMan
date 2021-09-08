from tkinter import *
import tkinter as tk
from tkinter.ttk import *

root = Tk()

root.title("Juego del Ahorcado")
root.geometry("800x600")

def StartPlay():
    btnStart.pack_forget()
    entryPalabra.pack()
    btnAccept.pack()
    string.pack()

def acceptString():
    btnAccept.pack_forget()
    entryPalabra.pack_forget()
    string.pack_forget()
    EnteredChar()

def EnteredChar():
    lblEnterChar.pack()
    txtEnterChar.pack()
    btnIntent.pack()
   


def findLetter():
    char = txtEnterChar.get()
    txt = list(txtPalabra.get())
    intents = 10
    i=0
    characters= ("_ "*len(txt))
    lblShowString.config(text=characters)
    txtEnterChar.delete(0,END)
    


    if char in txt:
        entryLabelResult.config(text="Se encontro la palabra  :D")
        
    else:
        entryLabelResult.config(text="No se encontro la palabra :c")
    
    # i+=1





string = tk.Label(text="Ingrese una palabra")
txtPalabra= StringVar()
entryPalabra = tk.Entry(textvariable=txtPalabra)


btnAccept = tk.Button(text="accept",command=acceptString)

lblEnterChar = tk.Label(text="Ingrese una letra")
char = StringVar()
txtEnterChar =  tk.Entry(textvariable=char)
btnIntent = tk.Button(text="Buscar",command=findLetter)

stringEntered = tk.Label(background="green",width=60,text="BIENVENIDO AL JUEGO DEL AHORCADO",padx=20,pady=20,font=("Courier",20)).pack()
btnStart = tk.Button(text="Empezar el juego",pady=10,padx=10,command=StartPlay)
btnStart.pack()


entryLabelResult = Label(text="")
entryLabelResult.pack()

lblShowString = Label(text="")
lblShowString.pack()
root.mainloop()

