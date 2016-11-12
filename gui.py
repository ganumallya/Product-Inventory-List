from Tkinter import *
import tkMessageBox
import csv
products = []

# Esempio di GUI
def makeWindow():

	def readCsv():
		with open('test1.csv','rb') as file:
			csvRow = csv.reader(file)
			for row in csvRow:
				products.append(row)

	def writeCsv():
		with open('test1.csv','w') as file:
			csvRow =csv.writer(file)
			csvRow.writerows(products)


	def update_listbox():
		lBox.delete(0,END)
		for prod in products:
			lBox.insert(END,prod[0])
			

	def onSelect(evt):
		w = evt.widget
		index=int(w.curselection()[0])
		value = w.get(index)
		name.set(value)
		price.set(products[index][1])

	def onUpdate():
		try:
			products[int(lBox.curselection()[0])][0] = eName.get()
			products[int(lBox.curselection()[0])][1] = ePrice.get()
			update_listbox()
			writeCsv()
		except IndexError:
			print "Indexx Error"
			tkMessageBox.showinfo("Index Error","Please make sure item is selected, before editing")
	
	def onAdd():
		products.append([eName.get(),ePrice.get()])
		update_listbox()
		writeCsv()

	def onDelete():
		del products[lBox.curselection()[0]]
		update_listbox()
		writeCsv()

	w1=Tk()
	w1.title("Product Inventory List")
	
	 # Width, height in pixe\
	f=Frame(w1,width=600,height=600)
	f1=Frame(f,width=400, height=200)
	f2=Frame(f,width=400,height=200)
	f3=Frame(f,width=400,height=200)
	f.pack()
	f1.pack()
	f2.pack()
	f3.pack()
	
	readCsv()


	b1=Button(f2,text="Add",command=onAdd)
	b2=Button(f2,text="Update",command=onUpdate)
	b3=Button(f2,text="Delete",command=onDelete)
	b1.pack(side=LEFT)
	b2.pack(side=LEFT)
	b3.pack(side=LEFT)

	labName=StringVar()
	labPrice=StringVar()
	labelName = Label(f1,textvariable=labName,justify="center")
	labelPrice = Label(f1,textvariable=labPrice,justify="center")
	labName.set('Product Name :')
	labPrice.set('Price :')

	name=StringVar()
	eName= Entry(f1,justify="center",textvariable=name,bg="grey",bd=5)
	name.set(products[0][0])

	price=StringVar()
	ePrice= Entry(f1,justify="center",textvariable=price,bg="grey",bd=5)
	price.set(products[0][1])


	labelName.grid(row=0,column=0,sticky='E')
	eName.grid(row=0,column=1,sticky='w')
	labelPrice.grid(row=1,column=0,sticky='E')
	ePrice.grid(row=1,column=1,sticky='w')

	lBox = Listbox(f3,width=35,selectmode="SINGLE")
	update_listbox()
	lBox.pack()




	lBox.bind('<<ListboxSelect>>',onSelect)


	w1.mainloop()

	return w1

makeWindow()

