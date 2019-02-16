import sqlite3

class StudentData:

	def __init__(self,db):
		self.con = sqlite3.connect(db)
		self.cur = self.con.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY,name TEXT,roll INTEGER,branch TEXT,sem INTEGER,fees INTEGER,cat TEXT)")

	def insert(self,name,roll,branch,sem,fees,cat):
		self.cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?,?,?)",(name,roll,branch,sem,fees,cat))
		self.con.commit()

	def search(self,name="",roll="",branch="",sem="",fees="",cat=""):
		self.cur.execute("SELECT * FROM student WHERE name=? OR roll=? OR branch=? OR sem=? OR fees=? OR cat=?",(name,roll,branch,sem,fees,cat))
		val = self.cur.fetchall()
		return val

	def update(self,id,name,roll,branch,sem,fees,cat):
		self.cur.execute("UPDATE student SET name=?,roll=?,branch=?,sem=?,fees=?,cat=? WHERE id=?",(name,roll,branch,sem,fees,cat,id))
		self.con.commit()

	def delete(self,id):
		self.cur.execute("DELETE FROM student WHERE id=?",(id,))
		self.con.commit()

	def view(self):
		self.cur.execute("SELECT * FROM student")
		val = self.cur.fetchall()
		return val

	def __del__(self):
		self.con.close()

