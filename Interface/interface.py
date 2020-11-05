from tkinter import *
import tkinter as tk
from tkinter import messagebox
from Connector.connector import Connector

# TODO: Poner mensaje cargando

class Interface (tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.window = master

    def execute_interface(self):
        self.__configurate_window()
        self.__configurate_frame()
        self.__configurate_labels()
        self.__configurate_entry()
        self.__configurate_checkbutton()
        self.__configurate_radiobutton()
        self.__configurate_button()

    def __configurate_window(self):
        self.window.title("TRZ - TRZearcher")
        self.window.resizable(False, False)

    def __configurate_frame(self):
        self.frame = Frame(self.window, bg="#cce7e8", width='650', height='500', bd=10, relief='ridge')
        self.frame.pack()

    def __configurate_labels(self):
        Label(self.frame, text='Desarrollado por TRZ', font=('Comic Sans MS', 7), fg="#cce7e8", bg="black").place(x=532, y=460)
        Label(self.frame, text='BIENVENIDO A TRZEARCHER', font=('Comic Sans MS', 20), bg="#cce7e8").place(x=100, y=30)
        Label(self.frame, text='Producto a buscar', font=('Comic Sans MS', 15), bg="#cce7e8").place(x=135, y=100)
        Label(self.frame, text='Paginas en las cuales buscar:', font=('Comic Sans MS', 15), bg="#cce7e8").place(x=135, y=150)
        Label(self.frame, text='Tipo de busqueda:', font=('Comic Sans MS', 15), bg="#cce7e8").place(x=135, y=290)

    def __configurate_entry(self):
        self.product = StringVar()
        Entry(self.frame, justify='center', font=('Comic Sans MS', 10), textvariable=self.product).place(x=326, y=106)

    def __configurate_checkbutton(self):
        self.compra_gamer = IntVar()
        Checkbutton(self.frame, text='Compra Gamer', font=('Comic Sans MS', 12), variable=self.compra_gamer, onvalue=1, offvalue=0, bg="#cce7e8").place(x=135, y=180)
        self.compra_gamer.set(1)
        self.full_hard = IntVar()
        Checkbutton(self.frame, text='Full H4rd', font=('Comic Sans MS', 12), variable=self.full_hard, onvalue=1, offvalue=0, bg="#cce7e8").place(x=135, y=210)
        self.full_hard.set(1)
        self.gezatek = IntVar()
        Checkbutton(self.frame, text='Gezatek', font=('Comic Sans MS', 12), variable=self.gezatek, onvalue=1, offvalue=0, bg="#cce7e8").place(x=135, y=240)
        self.gezatek.set(1)
        self.venex = IntVar()
        Checkbutton(self.frame, text='Venex', font=('Comic Sans MS', 12), variable=self.venex, onvalue=1, offvalue=0, bg="#cce7e8").place(x=295, y=180)
        self.venex.set(1)
        self.overdrive = IntVar()
        Checkbutton(self.frame, text='Overdrive', font=('Comic Sans MS', 12), variable=self.overdrive, onvalue=1, offvalue=0, bg="#cce7e8").place(x=295, y=210)
        self.overdrive.set(1)

    def __configurate_radiobutton(self):
        self.option = IntVar()
        Radiobutton(self.frame, text='Publicación con la frase exacta', variable=self.option, value=1, font=('Comic Sans MS', 12),
                    bg="#cce7e8").place(x=135, y=320)
        Radiobutton(self.frame, text='Publicación que contenga todas las palabras', variable=self.option, value=2,
                    font=('Comic Sans MS', 12), bg="#cce7e8").place(x=135, y=350)
        Radiobutton(self.frame, text='Publicación que contenga algunas de las palabras', variable=self.option, value=3,
                    font=('Comic Sans MS', 12), bg="#cce7e8").place(x=135, y=380)
        self.option.set(3)

    def __code_button(self):
        if (str(self.product.get()).strip() == "") and (self.compra_gamer.get() + self.full_hard.get() + self.gezatek.get() + self.venex.get() + self.overdrive.get() <= 0):
            messagebox.showerror(message="Recordar que:\n - La entrada del producto no puede estar vacia\n - Al menos hay que seleccionar una pagina", title="Problema con TRZearcher")
        else:
            Connector(self.product.get(),self.compra_gamer.get(), self.full_hard.get(), self.gezatek.get(), self.venex.get(), self.overdrive.get(), self.option.get())
            self.window.destroy()

    def __configurate_button(self):
        Button(self.frame, text="BUSCAR", font=('Comic Sans MS', 13), bg="dark gray", command=self.__code_button, fg="#cce7e8", background='black').place(x=270, y=430)

