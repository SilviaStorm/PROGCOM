from tkinter import *
from tkinter import ttk

class g:

	def __init__(self,v): #Constructor "init" q recibe "(self,v)"
		self.v = v
		self.v.configure(bg='pink')
		self.vainas = ("Leche-$2890","Huevos-$7150","Pan-$2000","Chocolate-$7650","Cafe-$11000","Arepas-$1000","Queso-$6750","Harina-$2600","Azucar-$2700","Sal-$900","Aceite-$14690","Mantequilla-$10050", "Libra de cebolla-$1000","Cebolla-$2050",)
		self.cC = IntVar()
		self.T = IntVar()
		self.total = 0
		self.dibujarComponentes()

	def dibujarComponentes(self):
		self.v.title("Super Market")
		self.v.geometry("600x450")
		Label(self.v,text="¿Qué quieres comprar?").place(x=10,y=10)
		Label(self.v,text="¿Cuanto quieres comprar?").place(x=10,y=60)
		Label(self.v,text="El total es: ").place(x=450,y=400)
		self.combo = ttk.Combobox(self.v,state="readonly")
		self.combo.place(x=10,y=35)
		self.combo["values"]=self.vainas
		self.combo.current(0)
		Entry(self.v,textvariable=self.cC).place(x=10,y=85)
		Entry(self.v,textvariable=self.T).place(x=520,y=400)
		Button(self.v,text="Agregar",command=self.agregarProducto).place(x=10,y=110)

		self.tabla = ttk.Treeview(self.v,columns=("Cantidad","Subtotal"))
		self.tabla.heading("#0",text="Producto")
		self.tabla.heading("Cantidad",text="Cantidad")
		self.tabla.heading("Subtotal",text="Subtotal")
		self.tabla.place(x=10,y=150)

	def agregarProducto(self):
		texto = self.combo.get()
  
		datos = texto.split("-$")
		producto = datos[0]
		precio = datos[1]
		cantidad = self.cC.get()
		subtotal = int(precio)*int(cantidad)
		self.tabla.insert("",END,text=producto,values=(cantidad,"$"+str(subtotal)))
		self.total = self.total + subtotal
		self.T.set("$"+str(self.total))
obj = g(Tk())
obj.v.mainloop()