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
    string.pack_forget( )
    global newArray 
    newArray = list(txtPalabra.get())
    for i,value  in enumerate(newArray) :
        newArray[i]="_"
    
    ShowString(newArray)  
    EnteredChar()

def EnteredChar():
    lblEnterChar.pack()
    txtEnterChar.pack()
    btnIntent.pack()

def convertListToString(list):
    stringTxt = "".join(list)
    return stringTxt

def ShowString(newArray):
    stringTxt = " ".join(newArray)
    lblShowString.config(text=stringTxt)

def findLetter():
    char = txtEnterChar.get()
    txt = list(txtPalabra.get())
    print("txt",txt)
    ShowString(newArray)
    txtEnterChar.delete(0,END)
    
    if char in txt:
        entryLabelResult.config(text="Se encontro la palabra  :D")
        index = txt.index(char)
        newArray[index] = char
        ShowString(newArray)

    else:
        entryLabelResult.config(text="No se encontro la palabra :c")
    

string = tk.Label(text="Ingrese una palabra")
txtPalabra= StringVar()
entryPalabra = tk.Entry(textvariable=txtPalabra)

newArray =[]
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

