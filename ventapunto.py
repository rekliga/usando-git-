import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
ventana = tk.Tk()
ventana.geometry("600x300")
ventana.title("Punto de Venta")

var = tk.StringVar()
usuario = tk.Label(ventana,text="Usuario").pack()
wrusuario = tk.Entry(ventana,width=25).pack()

contrasena = tk.Label(ventana,text="Usuario",width=25).pack()
entrada = tk.Entry(ventana, width=25, show="*")
entrada.insert(0, "")
entrada.pack()

def click_boton():
    texto = tk.Label(ventana,text=f'Se almacenó "{entrada.get()}" correctamente').pack()
def validacion():
    if entrada.get()=="ilker":
        tk.Label(ventana,text="contraseña correcta").pack() 
        ventana.withdraw()
        win=tk.Toplevel()
        win.geometry("800x600")
        win.title("Compra")
        notebook = ttk.Notebook(win)
        notebook.pack(fill='both',expand='yes')
        pes0 = ttk.Frame(notebook)
        pes1 = ttk.Frame(notebook)
        salir = ttk.Frame(notebook)
        notebook.add(pes0,text='titulo1')
        notebook.add(pes1,text='titulo 2')
        notebook.add(salir,text='salir')
        ext = tk.Button(salir,text='salir',command=cerrarventana).pack()
    else:
        messagebox.showwarning("Advertencia","Contraseña Erronea")
print(entrada.get())
def cerrarventana():
    ventana.destroy()
boton1 = tk.Button(ventana,
				text="Envíar",
				bg="red",
				padx=75,
				pady=10,
				command=validacion).pack()
ventana.mainloop()
