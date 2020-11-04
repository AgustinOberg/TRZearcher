from tkinter import *
from Connector.connector import Connector

# TODO: Modularizar y crear metodo para el main
# TODO: Poner mensaje cargando
# TODO: Validar opciones u opciones por default

window = Tk()
window.title("TRZ - TRZearcher")
window.resizable(False, False)


frame = Frame(window, bg="#cce7e8", width='650', height='500', bd=10, relief='ridge')
frame.pack()

Label(frame, text='Desarrollado por TRZ', font=('Comic Sans MS', 7), fg="#cce7e8", bg="black").place(x=532, y=460)
Label(frame, text='BIENVENIDO A TRZEARCHER', font=('Comic Sans MS', 20), bg="#cce7e8").place(x=100, y=30)
Label(frame, text='Producto a buscar', font=('Comic Sans MS', 15), bg="#cce7e8").place(x=135, y=100)
Label(frame, text='Paginas en las cuales buscar:', font=('Comic Sans MS', 15), bg="#cce7e8").place(x=135, y=150)
Label(frame, text='Tipo de busqueda:', font=('Comic Sans MS', 15), bg="#cce7e8").place(x=135, y=290)

product = StringVar()
Entry(frame, justify='center', font=('Comic Sans MS', 10), textvariable=product).place(x=326, y=106)
#TODO : Validar que no sea vacio, JOPTIONPANE

compra_gamer = IntVar()
Checkbutton(frame, text='Compra Gamer', font=('Comic Sans MS', 12), variable=compra_gamer, onvalue=1, offvalue=0,
            bg="#cce7e8").place(x=135, y=180)
full_hard = IntVar()
Checkbutton(frame, text='Full H4rd', font=('Comic Sans MS', 12), variable=full_hard, onvalue=1, offvalue=0,
            bg="#cce7e8").place(x=135, y=210)
gezatek = IntVar()
Checkbutton(frame, text='Gezatek', font=('Comic Sans MS', 12), variable=gezatek, onvalue=1, offvalue=0,
            bg="#cce7e8").place(x=135, y=240)
venex = IntVar()
Checkbutton(frame, text='Venex', font=('Comic Sans MS', 12), variable=venex, onvalue=1, offvalue=0,
            bg="#cce7e8").place(x=295, y=180)
overdrive = IntVar()
Checkbutton(frame, text='Overdrive', font=('Comic Sans MS', 12), variable=overdrive, onvalue=1, offvalue=0,
            bg="#cce7e8").place(x=295, y=210)

option = IntVar()
radio_button_1 = Radiobutton(frame, text='Publicación con la frase exacta', variable=option, value=1, font=('Comic Sans MS', 12),
            bg="#cce7e8").place(x=135, y=320)
radio_button_2 = Radiobutton(frame, text='Publicación que contenga todas las palabras', variable=option, value=2,
            font=('Comic Sans MS', 12), bg="#cce7e8").place(x=135, y=350)
radio_button_3 = Radiobutton(frame, text='Publicación que contenga algunas de las palabras', variable=option, value=3,
            font=('Comic Sans MS', 12), bg="#cce7e8").place(x=135, y=380)

def __code_button():
    Connector(product.get(),compra_gamer.get(), full_hard.get(), gezatek.get(), venex.get(), overdrive.get(), option.get())
    window.destroy()

Button(frame, text="BUSCAR", font=('Comic Sans MS', 13), bg="dark gray", command=__code_button,
       fg="#cce7e8", background='black').place(x=270, y=430)
window.mainloop()
