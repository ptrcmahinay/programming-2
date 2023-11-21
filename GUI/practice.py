# GUI 
import sqlite3
import tkinter as tk

# Create a connection to the database
conn = sqlite3.connect('sample.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table for the records
cursor.execute('''CREATE TABLE IF NOT EXISTS records
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   age INTEGER,
                   email TEXT)''')

# Function to add a new record to the database
def add_record(name, age, email):
    cursor.execute('''INSERT INTO records (name, age, email)
                      VALUES (?, ?, ?)''', (name, age, email))
    conn.commit()

# Function to edit a record in the database
def edit_record(id, name, age, email):
    cursor.execute('''UPDATE records
                      SET name=?, age=?, email=?
                      WHERE id=?''', (name, age, email, id))
    conn.commit()

# Function to delete a record from the database
def delete_record(id):
    cursor.execute('''DELETE FROM records
                      WHERE id=?''', (id,))
    conn.commit()

# Function to display the records in the database
def display_records():
    cursor.execute('SELECT * FROM records')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Function to handle the "Add" button click
def add_button_click():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    add_record(name, age, email)
    display_records()

# Function to handle the "Edit" button click
def edit_button_click():
    id = id_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    edit_record(id, name, age, email)
    display_records()

# Function to handle the "Delete" button click
def delete_button_click():
    id = id_entry.get()
    delete_record(id)
    display_records()

# Create the main window
window = tk.Tk()

# Create the widgets
id_label = tk.Label(window, text="ID")
name_label = tk.Label(window, text="Name")
age_label = tk.Label(window, text="Age")
email_label = tk.Label(window, text="Email")

id_entry = tk.Entry(window)
name_entry = tk.Entry(window)
age_entry = tk.Entry(window)
email_entry = tk.Entry(window)

add_button = tk.Button(window, text="Add", command=add_button_click)
edit_button = tk.Button(window, text="Edit", command=edit_button_click)
delete_button = tk.Button(window, text="Delete", command=delete_button_click)

# Place the widgets in the window
id_label.grid(row=0, column=0)
name_label.grid(row=1, column=0)
age_label.grid(row=2, column=0)
email_label.grid(row=3, column=0)

id_entry.grid(row=0, column=1)
name_entry.grid(row=1, column=1)
age_entry.grid(row=2, column=1)
email_entry.grid(row=3, column=1)

add_button.grid(row=4, column=0)
edit_button.grid(row=4, column=1)
delete_button.grid(row=4, column=2)

# Start the event loop
window.mainloop()

# Close the connection to the database
conn.close()
