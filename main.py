from tkinter import *
import tkinter as tk
from tkinter.ttk import *

root = Tk()

root.title("Juego del Ahorcado")
root.geometry("800x600")

stringEntered = tk.Label(background="green",width=60,text="BIENVENIDO AL JUEGO DEL AHORCADO",padx=20,pady=20,font=("Courier",20)).pack()
btnLabel = tk.Button(text="Empezar el juego",pady=10,padx=10).pack()


root.mainloop()

