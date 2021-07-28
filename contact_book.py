from tkinter import *
from tkinter import messagebox
from base_datos import database
class contacto():
	def __init__(self,root):
		self.bd = database("base_datos.db")
		self.nombre = StringVar()
		self.prefijo = StringVar()
		self.numero_tel = StringVar()
		self.relacion = StringVar()
		self.lista_relacion = ["Trabajo","Amigo","Familia"]
		self.relacion_opcion = StringVar()
		self.relacion_opcion.set("Relacion")
		self.listbox = Listbox(root,width=54,height=13,font=("Arial",13))
		self.listbox.grid(row=0,column=0,pady=10,padx=10,columnspan=4)
		self.label_nombre = Label(root,text="Nombre:",font=("Arial",16),bg="light gray")
		self.label_nombre.grid(row=1,column=0,padx=8,pady=10)
		self.entrada_nombre = Entry(root,textvariable=self.nombre,font=("Arial",14),width=30)
		self.entrada_nombre.grid(row=1,column=1,pady=10,columnspan=3)
		self.label_telefono = Label(root,text="Teléfono:",font=("Arial",16),bg="light gray")
		self.label_telefono.grid(row=2,column=0,pady=10)
		self.entrada_prefijo = Entry(root,textvariable=self.prefijo,font=("Arial",14),width=10)
		self.entrada_prefijo.grid(row=2,column=1,pady=10)
		self.label_guion = Label(root,text="-",font=("Impact",14),bg="light gray")
		self.label_guion.grid(row=2,column=2,pady=10)
		self.entrada_telefono = Entry(root,textvariable=self.numero_tel,font=("Arial",14),width=12)
		self.entrada_telefono.grid(row=2,column=3,pady=10)
		self.label_relacion = Label(root,text="Relación:",font=("Arial",16),bg="light gray")
		self.label_relacion.grid(row=3,column=0,pady=10)
		self.relacion_menu = OptionMenu(root,self.relacion_opcion,*self.lista_relacion)
		self.relacion_menu.grid(row=3,column=1)
		self.boton_guardar = Button(root,text="Guardar",font=("Arial",15),width=20,command=self.guardar)
		self.boton_guardar.grid(row=4,column=0,pady=20,columnspan=2)
		self.boton_borrar = Button(root,text="Borrar",font=("Arial",15),width=17,command=self.eliminar)
		self.boton_borrar.grid(row=4,column=2,pady=20,columnspan=2)
		self.entrada_nombre.focus()
		self.imprimir()
		self.listbox.bind("<<ListboxSelect>>",self.seleccionar)
	def limpiar(self):
		self.entrada_nombre.delete(0,END)
		self.entrada_prefijo.delete(0,END)
		self.entrada_telefono.delete(0,END)
		self.relacion_opcion.set("Relacion")
		self.entrada_nombre.focus()
	def guardar(self):
		if str.isdigit(self.entrada_nombre.get()) == True:
			messagebox.showwarning("Advertencia","El nombre no debe tener numeros")
			self.limpiar()
		elif self.entrada_nombre.get() == "" or self.entrada_prefijo.get() == "" or self.entrada_telefono.get() == "":
			messagebox.showwarning("Advertencia","Tiene que llenar todos los campos")
		elif len(self.entrada_prefijo.get()) != 4:
			messagebox.showwarning("Advertencia","El prefijo telefónico debe contener 4 caracteres")
		elif len(self.entrada_telefono.get()) != 7:
			messagebox.showwarning("Advertencia","El número telefónico debe contener 7 caracteres")
		else:
			try:
				self.bd.insertar(self.entrada_nombre.get(),self.entrada_prefijo.get(),self.entrada_telefono.get(),self.relacion_opcion.get())
				self.imprimir()
				self.limpiar()
				messagebox.showinfo("Guardado Exitosamente","Contacto Guardado")
			except:
				messagebox.showwarning("Error","Ha surgido un problema al guardar")
	def seleccionar(self,event):
		self.limpiar()
		self.index = self.listbox.curselection()[0]
		self.seleccionar = self.listbox.get(self.index)
		print(self.seleccionar[0])
		self.entrada_nombre.delete(0,END)
		self.entrada_nombre.insert(END,self.seleccionar[1])
		self.entrada_prefijo.delete(0,END)
		self.entrada_prefijo.insert(END,self.seleccionar[2])
		self.entrada_telefono.delete(0,END)
		self.entrada_telefono.insert(END,self.seleccionar[3])
		self.relacion_opcion.set(f"{self.seleccionar[4]}")
	def eliminar(self):
		self.bd.borrar(self.seleccionar[0])
		self.limpiar()
		self.listbox.delete(0,END)
		self.imprimir()
	def imprimir(self):
		for self.row in self.bd.recorrer():
			self.listbox.insert(END,self.row)
if __name__ == '__main__':
   root = Tk()
   root.geometry("505x500")
   root.config(bg="light gray")
   root.title("Contact Book")
   root.resizable(0,0)
   contacto(root)
   root.mainloop()
