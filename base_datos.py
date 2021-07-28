import sqlite3
class database:
	def __init__(self,db):
		self.conexion = sqlite3.connect(db)
		self.exe = self.conexion.cursor()
		self.exe.execute("CREATE TABLE IF NOT EXISTS CONTACT(ID INTEGER PRIMARY KEY AUTOINCREMENT,nombre VARCHAR(20),prefijo VARCHAR(20),numero VARCHAR(20),relacion VARCHAR(20))")
	def insertar(self,name,prefix,number,relation):
		self.exe.execute("INSERT INTO CONTACT VALUES(NULL,?,?,?,?)",(name,prefix,number,relation))
		self.conexion.commit()
	def recorrer(self):
		self.exe.execute("SELECT*FROM CONTACT")
		self.rows = self.exe.fetchall()
		return self.rows
	def borrar(self,key):
		self.exe.execute("DELETE FROM CONTACT WHERE ID = ?",(key,))
		self.conexion.commit()
	def __del__(self):
		self.conexion.close()
