from tkinter import *
from Connector.connector import Connector
import os

window = Tk()
window.title("TRZ - Scrapy Master")
window.resizable(False, False)
iconPath = os.path.abspath("./resources/icon.ico")


frame = Frame(window, bg="#E6B0AA", width='650', height='500', bd=10, relief='ridge', cursor='hand2')
frame.pack()

Label(frame, text='Desarrollado por TRZ', font=('Microsoft YaHei', 7), fg="#E6B0AA", bg="black").place(x=532, y=460)
Label(frame, text='BIENVENIDO A SCRAPY MASTER', font=('Microsoft YaHei', 20), bg="#E6B0AA").place(x=100, y=30)
Label(frame, text='Producto a buscar', font=('Microsoft YaHei', 15), bg="#E6B0AA").place(x=135, y=100)
Label(frame, text='Paginas en las cuales buscar:', font=('Microsoft YaHei', 15), bg="#E6B0AA").place(x=135, y=150)
Label(frame, text='Tipo de busqueda:', font=('Microsoft YaHei', 15), bg="#E6B0AA").place(x=135, y=290)

product = StringVar()
Entry(frame, justify='center', font=('Microsoft YaHei', 10), textvariable=product).place(x=326, y=106)

compra_gamer = IntVar()
Checkbutton(frame, text='Compra Gamer', font=('Microsoft YaHei', 12), variable=compra_gamer, onvalue=1, offvalue=0,
            bg="#E6B0AA").place(x=135, y=180)
full_hard = IntVar()
Checkbutton(frame, text='Full H4rd', font=('Microsoft YaHei', 12), variable=full_hard, onvalue=1, offvalue=0,
            bg="#E6B0AA").place(x=135, y=210)
gezatek = IntVar()
Checkbutton(frame, text='Gezatek', font=('Microsoft YaHei', 12), variable=gezatek, onvalue=1, offvalue=0,
            bg="#E6B0AA").place(x=135, y=240)
venex = IntVar()
Checkbutton(frame, text='Venex', font=('Microsoft YaHei', 12), variable=venex, onvalue=1, offvalue=0,
            bg="#E6B0AA").place(x=295, y=180)
overdrive = IntVar()
Checkbutton(frame, text='Overdrive', font=('Microsoft YaHei', 12), variable=overdrive, onvalue=1, offvalue=0,
            bg="#E6B0AA").place(x=295, y=210)

option = IntVar()
radio_button_1 = Radiobutton(frame, text='Publicación con la frase exacta', variable=option, value=1, font=('Microsoft YaHei', 12),
            bg="#E6B0AA").place(x=135, y=320)
radio_button_2 = Radiobutton(frame, text='Publicación que contenga todas las palabras', variable=option, value=2,
            font=('Microsoft YaHei', 12), bg="#E6B0AA").place(x=135, y=350)
radio_button_3 = Radiobutton(frame, text='Publicación que contenga algunas de las palabras', variable=option, value=3,
            font=('Microsoft YaHei', 12), bg="#E6B0AA").place(x=135, y=380)

def __code_button():
    Connector(product.get(),compra_gamer.get(), full_hard.get(), gezatek.get(), venex.get(), overdrive.get(), option.get())
    window.destroy()

Button(frame, text="BUSCAR", font=('Microsoft YaHei', 13), bg="dark gray", command=__code_button,
       fg="#E6B0AA", background='black').place(x=270, y=430)

window.mainloop()
