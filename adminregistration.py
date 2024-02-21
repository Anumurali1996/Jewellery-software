import tkinter as tk
from tkinter import messagebox
import mysql.connector

def register_admin(username, password):
    try:
        # Connect to MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Anu@17151431",
            database="jewellery"
        )
        cursor = db.cursor()

        # Check if the admin already exists
        check_query = "SELECT * FROM users WHERE username = %s AND user_type = 'admin'"
        cursor.execute(check_query, (username,))
        if cursor.fetchone():
            messagebox.showerror("Error", "Admin already exists.")
            return

        # Insert admin data into the database
        insert_query = "INSERT INTO users (username, password, user_type) VALUES (%s, %s, 'admin')"
        cursor.execute(insert_query, (username, password))
        db.commit()

        messagebox.showinfo("Success", "Admin registration successful.")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")
    finally:
        cursor.close()
        db.close()

def register_admin_form():
    # Create the main window
    root = tk.Tk()
    root.title("Admin Registration")

    # Create widgets
    username_label = tk.Label(root, text="Username:")
    username_entry = tk.Entry(root)

    password_label = tk.Label(root, text="Password:")
    password_entry = tk.Entry(root, show="*")

    register_button = tk.Button(root, text="Register", command=lambda: register_admin(username_entry.get(), password_entry.get()))

    # Place widgets on the grid
    username_label.grid(row=0, column=0, padx=10, pady=10)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    password_label.grid(row=1, column=0, padx=10, pady=10)
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    register_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Start the Tkinter event loop
    root.mainloop()

# Run the registration form
register_admin_form()
