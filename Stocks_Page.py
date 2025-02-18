import sqlite3
import bcrypt
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import colorchooser
import customtkinter

root = customtkinter.CTk()
root.title('Emrex SMS')
# root.iconbitmap('c:/gui/codemy.ico')
# root.attributes('-fullscreen',True)
root.geometry("1000x550")
username = ""

def query_database():
	global username
	# Clear the treeview
	for record in my_tree.get_children():
		my_tree.delete(record)

	c.execute("SELECT * FROM stock_table WHERE user = ?", (username,))

	# Save database
	conn.commit()

	records = c.fetchall()
	
	# Add our data to the screen
	global count
	count = 0
	
	#for record in records:
	for record in records:
		if count % 2 == 0:
			my_tree.insert(parent='', index='end', iid=count, text='', values=record, tags=('evenrow',))
		else:
			my_tree.insert(parent='', index='end', iid=count, text='', values=record, tags=('oddrow',))
		# increment counter
		count += 1

# -----------------------  OPTIONS IT 3 ------------------------------------------------------ #

def search_records_name():
	global username
	lookup_record = search_entry_name.get()
	# close search box
	search_name.destroy()
	# Clear the treeview
	for record in my_tree.get_children():
		my_tree.delete(record)
	
	records = c.execute("SELECT * FROM stock_table WHERE user = ?", (username,)).fetchall()
	matching_records = linear_search(records, lookup_record, 1)

	# Save database
	conn.commit()

	# Add our data to the screen
	global count
	count = 0
	
	#for record in records:
	for record in matching_records:
		if count % 2 == 0:
			my_tree.insert(parent='', index='end', iid=count, text='', values=record, tags=('evenrow',))
		else:
			my_tree.insert(parent='', index='end', iid=count, text='', values=record, tags=('oddrow',))
		# increment counter	
		count += 1

def search_records_id():
	global username
	lookup_record = search_entry_id.get()
	# close search box
	search_id.destroy()
	# Clear the treeview
	for record in my_tree.get_children():
		my_tree.delete(record)
	

	records = c.execute("SELECT * FROM stock_table WHERE user = ?", (username,)).fetchall()
	matching_records = linear_search(records, lookup_record, 0)

	# Save database
	conn.commit()

	
	# Add our data to the screen
	global count
	count = 0
	
	#for record in records:
	for record in matching_records:
		if count % 2 == 0:
			my_tree.insert(parent='', index='end', iid=count, text='', values=record, tags=('evenrow',))
		else:
			my_tree.insert(parent='', index='end', iid=count, text='', values=record, tags=('oddrow',))
		# increment counter	
		count += 1

def search_records_category():
	global username
	lookup_record = search_entry.get()
	# close search box
	search.destroy()
	# Clear the treeview
	for record in my_tree.get_children():
		my_tree.delete(record)
	
	records = c.execute("SELECT * FROM stock_table WHERE user = ?", (username,)).fetchall()
	matching_records = linear_search(records, lookup_record, 2)

	# Save database
	conn.commit()
	
	# Add our data to the screen
	global count
	count = 0
	
	#for record in records:


	for record in matching_records:
		if count % 2 == 0:
			my_tree.insert(parent='', index='end', iid=count, text='', values=record, tags=('evenrow',))
		else:
			my_tree.insert(parent='', index='end', iid=count, text='', values=record, tags=('oddrow',))
		# increment counter	
		count += 1

def linear_search(records, search_term, col):
	matching = []
 
	for i in range(len(records)):
		if str(records[i][col]).lower() == str(search_term).lower():
			matching.append(records[i])

	return matching

def lookup_records_name():
	global search_entry_name, search_name
	search_name = Toplevel(root)
	search_name.title("Lookup Records")
	search_name.geometry("400x200")
	

	# Create label frame
	search_frame = LabelFrame(search_name, text="Product Name")
	search_frame.pack(padx=10,pady=10)

	# Add entry box
	search_entry_name = Entry(search_frame, font=("Helvetica", 18))
	search_entry_name.pack(pady=20, padx=20)

	# Add button
	search_button = Button(search_name, text="Search Records", command = search_records_name)
	search_button.pack(padx=20, pady=20)

def lookup_records_id():
	global search_entry_id, search_id
	search_id = Toplevel(root)
	search_id.title("Lookup Records")
	search_id.geometry("400x200")
	# search.iconbitmap(XXXX)

	# Create label frame
	search_frame = LabelFrame(search_id, text="Product ID")
	search_frame.pack(padx=10,pady=10)

	# Add entry box
	search_entry_id = Entry(search_frame, font=("Helvetica", 18))
	search_entry_id.pack(pady=20, padx=20)

	# Add button
	search_button = Button(search_id, text="Search Records", command = search_records_id)
	search_button.pack(padx=20, pady=20)

def lookup_records_category():
	global search_entry, search
	search = Toplevel(root)
	search.title("Lookup Records")
	search.geometry("400x200")
	# search.iconbitmap(XXXX)

	# Create label frame
	search_frame = LabelFrame(search, text="Category")
	search_frame.pack(padx=10,pady=10)

	# Add entry box
	search_entry = Entry(search_frame, font=("Helvetica", 18))
	search_entry.pack(pady=20, padx=20)

	# Add button
	search_button = Button(search, text="Search Records", command = search_records_category)
	search_button.pack(padx=20, pady=20)

def primary_color():
	# Pick color
	primary_color = colorchooser.askcolor()[1]

	# Update treeview
	if primary_color:
		my_tree.tag_configure('evenrow', background=primary_color)

def secondary_color():
	# Pick color
	secondary_color = colorchooser.askcolor()[1]
	
	# Update treeview
	if secondary_color:
		my_tree.tag_configure('oddrow', background=secondary_color)
	
def highlight_color():
	# Pick color
	highlight_color = colorchooser.askcolor()[1]

	# Update treeview
	if highlight_color:
		# Change Selected Color
		style.map('Treeview',
			background=[('selected', highlight_color)])

#  Add menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Configure our menu
option_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Customisations", menu=option_menu)

# Drop down menu
option_menu.add_command(label="Change Primary Color", command=primary_color)
option_menu.add_command(label="Change Secondary Color", command=secondary_color)
option_menu.add_command(label="Change Highlight Color", command=highlight_color)
option_menu.add_separator()
option_menu.add_command(label="Exit", command ="root.quit")

# Search menu
search_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Search", menu=search_menu)

# Drop down menu
search_menu.add_command(label="Search Records by Product ID", command =lookup_records_id)
search_menu.add_command(label="Search Records by Product Name", command =lookup_records_name)
search_menu.add_command(label="Search Records by Category", command =lookup_records_category)
search_menu.add_separator()
search_menu.add_command(label="Reset", command =query_database)

# ----------------------------------------------------------------------------------------- #

# Create a database or connect to one that exists
conn = sqlite3.connect('tree_crm.db')

# Create a cursor instance
c = conn.cursor()

# Create Table
c.execute("""CREATE TABLE IF NOT EXISTS stock_table (
	product_id INTEGER NOT NULL UNIQUE,
	product_name VARCHAR(255) NOT NULL,
	category VARCHAR(60) NOT NULL,
	capacity INTEGER NOT NULL,
	stock INTEGER NOT NULL,
	product_price REAL NOT NULL,
	user VARCHAR(20) NOT NULL,
	FOREIGN KEY (user) REFERENCES users (username) 
	PRIMARY KEY (user, product_id)
)""")

# Save database
conn.commit()

# Add Some Style
style = ttk.Style()

# Pick A Theme
style.theme_use('default')

# Configure the Treeview Colors
style.configure("Treeview",
	background="#D3D3D3",
	foreground="black",
	rowheight=25,
	fieldbackground="#D3D3D3")

# Change Selected Color
style.map('Treeview',
	background=[('selected', "#347083")])

# Create a Treeview Frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# Configure the Scrollbar
tree_scroll.config(command=my_tree.yview)

# Define Our Columns
my_tree['columns'] = ("Product ID", "Product Name", "Category", "Capacity", "Stock", "Product Price")

# Format Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Product ID", anchor=W, width=140)
my_tree.column("Product Name", anchor=W, width=140)
my_tree.column("Category", anchor=CENTER, width=100)
my_tree.column("Capacity", anchor=CENTER, width=140)
my_tree.column("Stock", anchor=CENTER, width=140)
my_tree.column("Product Price", anchor=CENTER, width=140)

# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Product ID", text="Product ID", anchor=W)
my_tree.heading("Product Name", text="Product Name", anchor=W)
my_tree.heading("Category", text="Category", anchor=CENTER)
my_tree.heading("Capacity", text="Capacity", anchor=CENTER)
my_tree.heading("Stock", text= "Stock", anchor=CENTER)
my_tree.heading("Product Price", text="Product Price", anchor=CENTER)

# Create Striped Row Tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

# Add Record Entry Boxes
data_frame = LabelFrame(root, text="Record")
data_frame.pack(fill="x", expand="yes", padx=20)

product_id_label = Label(data_frame, text="Product ID")
product_id_label.grid(row=0, column=0, padx=10, pady=10)
product_id_entry = Entry(data_frame)
product_id_entry.grid(row=0, column=1, padx=10, pady=10)

product_name_label = Label(data_frame, text="Product Name")
product_name_label.grid(row=0, column=2, padx=10, pady=10)
product_name_entry = Entry(data_frame)
product_name_entry.grid(row=0, column=3, padx=10, pady=10)

category_label = Label(data_frame, text="Category")
category_label.grid(row=0, column=4, padx=10, pady=10)
category_entry = Entry(data_frame)
category_entry.grid(row=0, column=5, padx=10, pady=10)

capacity_label = Label(data_frame, text="Capacity")
capacity_label.grid(row=1, column=0, padx=10, pady=10)
capacity_entry = Entry(data_frame)
capacity_entry.grid(row=1, column=1, padx=10, pady=10)

stock_label = Label(data_frame, text="Stock")
stock_label.grid(row=1, column=2, padx=10, pady=10)
stock_entry = Entry(data_frame)
stock_entry.grid(row=1, column=3, padx=10, pady=10)

product_price_label = Label(data_frame, text="Product Price")
product_price_label.grid(row=1, column=4, padx=10, pady=10)
product_price_entry = Entry(data_frame)
product_price_entry.grid(row=1, column=5, padx=10, pady=10)

# Move Row Up
def up():
	rows = my_tree.selection()
	for row in rows:
		my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

# Move Rown Down
def down():
	rows = my_tree.selection()
	for row in reversed(rows):
		my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)




# Remove one record
def remove_one():
	global username
	currentlySelected = my_tree.selection()[0]

	productId = my_tree.item(currentlySelected)["values"][0]

	# Delete from database 
	c.execute("DELETE FROM stock_table WHERE product_id = '" + str(productId) + "'" )
	# Save database
	conn.commit()

	my_tree.delete(currentlySelected)

# Remove Many records
def remove_many():
# Message box
	response = messagebox.askyesno("POPUP","Are you sure that you want to delete everything selected from the table?")

	# Logic for messagebox
	if response == 1:
		x = my_tree.selection()

		#  Create list of ID's
		ids_to_delete = []
	
		# Add selection to ids_to_delete list
		for record in x:
			ids_to_delete.append(my_tree.item(record, 'values')[0])

		# Delete from treeview
		for record in x:
			my_tree.delete(record)

		#  Delete everything selected *******PROBLEM HERE*******
		params = [a for a in ids_to_delete]
		params.append(username)
		for item in ids_to_delete:
			c.execute("DELETE FROM stock_table WHERE product_id = ? AND user = ?", (item, username))

		# Commit changes
		conn.commit()

		# Clear entry boxes
		clear_entries() 



# Add record
def add_record():

	global username
	# Add New Record

	try:
		if c.execute("SELECT * FROM stock_table WHERE product_id = ? AND user = ? ", (product_id_entry.get(), username)).fetchone():
			print("Work")
		else:
			c.execute("INSERT INTO stock_table VALUES (:id, :name, :category, :capacity, :stock, :price, :user)",
				{
					'id': abs(int(product_id_entry.get())) or None,
					'name': product_name_entry.get() or None,
					'category': category_entry.get() or None,
					'capacity': abs(int(capacity_entry.get())) or None,
					'stock': abs(int(stock_entry.get())) or None,
					'price':abs(float(product_price_entry.get())) or None,
					'user': username or None
				})
	
	except sqlite3.IntegrityError as e:
		print("Integrity Error:", e)

	# error
	except ValueError:
		messagebox.showerror("Error", "Pleaase enter a number.")
	except OverflowError:
		messagebox.showerror("Error", "Your input is too big to be handled.")

		
	
	# Save database
	conn.commit()

	# Clear entry boxes
	product_name_entry.delete(0, END)
	product_id_entry.delete(0, END)
	category_entry.delete(0, END)
	capacity_entry.delete(0, END)
	stock_entry.delete(0, END)
	product_price_entry.delete(0, END)
	

	# Clear The Treeview Table
	my_tree.delete(*my_tree.get_children())

	# Run to pull data from database on start
	query_database()

# Remove all records
def remove_all():
	global username 
	# Message box
	response = messagebox.askyesno("POPUP","Are you sure that you want to delete everything from the table?")

	# Logic for messagebox
	if response == 1:
		# Clear the treeview
		for record in my_tree.get_children():
			my_tree.delete(record)

		# Delete eveything from the table
		c.execute("DELETE FROM stock_table WHERE user = ?", (username,)) 

		# Commit changes
		conn.commit()

		# Clear entry boxes
		clear_entries()

# Clear entry boxes
def clear_entries():
	# Clear entry boxes
	product_id_entry.delete(0, END)
	product_name_entry.delete(0, END)
	category_entry.delete(0, END)
	capacity_entry.delete(0, END)
	stock_entry.delete(0, END)
	product_price_entry.delete(0, END)

# Select Record
def select_record(e):
	# Clear entry boxes
	product_id_entry.delete(0, END)
	product_name_entry.delete(0, END)
	category_entry.delete(0, END)
	capacity_entry.delete(0, END)
	stock_entry.delete(0, END)
	product_price_entry.delete(0, END)
	# zipcode_entry.delete(0, END)

	# Grab record Number
	selected = my_tree.focus()
	# Grab record values
	values = my_tree.item(selected, 'values')

	if values:
		# outpus to entry boxes
		product_id_entry.insert(0, values[0])
		product_name_entry.insert(0, values[1])
		category_entry.insert(0, values[2])
		capacity_entry.insert(0, values[3])
		stock_entry.insert(0, values[4])
		product_price_entry.insert(0, values[5])

# Update record
def update_record():
	global username
	# Grab the record number
	selected = my_tree.focus()
	# Update record
	my_tree.item(selected, text="", values=(abs(int(product_id_entry.get())),product_name_entry.get(),category_entry.get(),abs(int(capacity_entry.get())),abs(int(stock_entry.get())),abs(float(product_price_entry.get()))))
	# Update the database
	c.execute("""UPDATE stock_table SET
		product_name = :name,
		product_id = :id,
		category = :category,
		capacity = :capacity,
		stock = :stock,
		product_price = :price 
	

		WHERE user = :username AND product_id = :id""",
		{
			'name': product_name_entry.get() or None,
			'id': abs(int(product_id_entry.get())) or None,
			'category': category_entry.get() or None,
			'capacity': abs(int(capacity_entry.get())) or None,
			'stock': abs(int(stock_entry.get())) or None,
			'price': abs(float(product_price_entry.get())) or None,
			'username': username or None
		})
	
	# Save database
	conn.commit()

	# Clear entry boxes
	product_id_entry.delete(0, END)
	product_name_entry.delete(0, END)
	category_entry.delete(0, END)
	capacity_entry.delete(0, END)
	stock_entry.delete(0, END)
	product_price_entry.delete(0, END)

# Add Buttons
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

update_button = Button(button_frame, text="Update Record", command=update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = Button(button_frame, text="Add Record", command=add_record)
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_all_button = Button(button_frame, text="Remove All Records", command=remove_all)
remove_all_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = Button(button_frame, text="Remove One Selected", command=remove_one)
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

remove_many_button = Button(button_frame, text="Remove Many Selected", command=remove_many)
remove_many_button.grid(row=0, column=4, padx=10, pady=10)

move_up_button = Button(button_frame, text="Move Up", command=up)
move_up_button.grid(row=0, column=5, padx=10, pady=10)

move_down_button = Button(button_frame, text="Move Down", command=down)
move_down_button.grid(row=0, column=6, padx=10, pady=10)

select_record_button = Button(button_frame, text="Clear Entry Boxes", command=clear_entries)
select_record_button.grid(row=0, column=7, padx=10, pady=10)

# Bind the treeview
my_tree.bind("<ButtonRelease-1>", select_record)

def main(uname):
	global username 
	username = uname
	# Run to pull data from database on start
	query_database()
	root.mainloop()





