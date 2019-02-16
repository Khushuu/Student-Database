from tkinter import *
from stuBE import StudentData

sdata = StudentData("Students.db")

def select_row(event):
	global tuple_select
	try:
		index = list1.curselection()[0]
		tuple_select = list1.get(index)
		e1.delete(0,END)
		e2.delete(0,END)
		e3.delete(0,END)
		e4.delete(0,END)
		e5.delete(0,END)
		e6.delete(0,END)
		e1.insert(END,tuple_select[1])
		e2.insert(END,tuple_select[2])
		e3.insert(END,tuple_select[3])
		e4.insert(END,tuple_select[4])
		e5.insert(END,tuple_select[5])
		e6.insert(END,tuple_select[6])

	except IndexError:
		pass

def view_command():
	list1.delete(0,END)
	for row in sdata.view():
		list1.insert(END,row)

def search_command():
	list1.delete(0,END)
	for row in sdata.search(name_var.get(),roll_var.get(),branch_var.get(),sem_var.get(),fees_var.get(),cat_var.get()):
		list1.insert(END,row)

def insert_command():
	sdata.insert(name_var.get(),roll_var.get(),branch_var.get(),sem_var.get(),fees_var.get(),cat_var.get())
	list1.delete(0,END)
	list1.insert(END,(name_var.get(),roll_var.get(),branch_var.get(),sem_var.get(),fees_var.get(),cat_var.get()))
	 
def update_command():
	sdata.update(tuple_select[0],name_var.get(),roll_var.get(),branch_var.get(),sem_var.get(),fees_var.get(),cat_var.get())
	view_command()

def delete_command():
	sdata.delete(tuple_select[0])
	view_command()

window = Tk()
window.title("Student Database")
window.geometry("520x350+380+50")

#define the different labels
l1 = Label(window,text="NAME: ")
l1.grid(row=0,column=0,padx=5,pady=5)

l2 = Label(window,text="ROLL NO: ")
l2.grid(row=0,column=2,padx=5,pady=5)

l3 = Label(window,text="BRANCH: ")
l3.grid(row=1,column=0,padx=5,pady=5)

l4 = Label(window,text="SEMESTER: ")
l4.grid(row=1,column=2,padx=5,pady=5)

l5 = Label(window,text="FEES: ")
l5.grid(row=2,column=0,padx=5,pady=5)

l6 = Label(window,text="CATEGORY: ")
l6.grid(row=2,column=2,padx=5,pady=5)

#define the entry box for each value
name_var = StringVar()
e1 = Entry(window,textvariable=name_var)
e1.grid(row=0,column=1)

roll_var = StringVar()
e2 = Entry(window,textvariable=roll_var)
e2.grid(row=0,column=3)

branch_var = StringVar()
e3 = Entry(window,textvariable=branch_var)
e3.grid(row=1,column=1)

sem_var = StringVar()
e4 = Entry(window,textvariable=sem_var)
e4.grid(row=1,column=3)

fees_var = StringVar()
e5 = Entry(window,textvariable=fees_var)
e5.grid(row=2,column=1)

cat_var = StringVar()
e6 = Entry(window,textvariable=cat_var)
e6.grid(row=2,column=3)

#Listbox Widget
list1 = Listbox(window,height=15,width=35)
list1.grid(row=3,column=0,rowspan=10,columnspan=3,padx=1,pady=15)

#bind the listbox with the select_row function
list1.bind('<<ListboxSelect>>',select_row)

#ScrollBar Widget
# sb1 = Scrollbar(window)
# sb1.grid(row=3,column=3,rowspan=10)

#Connecting scrollbar and the listbox
# list1.configure(yscrollcommand=sb1.set)
# sb1.configure(command=list1.yview)

#creating the buttons
b1 = Button(window,text="View Data",width=10,command=view_command)
b1.grid(row=5,column=3)

b1 = Button(window,text="Search",width=10,command=search_command)
b1.grid(row=6,column=3)

b1 = Button(window,text="Insert",width=10,command=insert_command)
b1.grid(row=7,column=3)

b1 = Button(window,text="Update",width=10,command=update_command)
b1.grid(row=8,column=3)

b1 = Button(window,text="Delete",width=10,command=delete_command)
b1.grid(row=9,column=3)

b1 = Button(window,text="Close",width=10,command=window.destroy)
b1.grid(row=10,column=3)

window.mainloop()