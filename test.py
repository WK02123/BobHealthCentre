import tkinter as tk
from tkinter import messagebox
import pyrebase

# Configure Firebase
firebaseConfig = {
    "apiKey": "AIzaSyDh6tLW3lCovQ2j1YZ0dklbppIhHZXUEJE",
    "authDomain": "bobclinic-e2804.firebaseapp.com",
    "databaseURL": "https://bobclinic-e2804-default-rtdb.firebaseio.com",
    "projectId": "bobclinic-e2804",
    "storageBucket": "bobclinic-e2804.appspot.com",
    "messagingSenderId": "812876084670",
    "appId": "1:812876084670:web:8ebc63b1694b68f59d75ef",
    "measurementId": "G-9ZFHMKE2FK"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

def register_user():
    name = name_entry.get()
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    phone = phone_entry.get()

    # Set role to 1 for patient
    role = 1

    try:
        # Create user with email and password
        user = auth.create_user_with_email_and_password(email, password)
        user_id = user['localId']

        # Save additional user data to the database
        user_data = {
            'name': name,
            'username': username,
            'email': email,
            'phone': phone,
            'role': role
        }
        db.child('users').child(user_id).set(user_data)

        messagebox.showinfo("Success", "Registration successful!")
    except Exception as e:
        messagebox.showerror("Error", f"Registration failed: {e}")

# Create GUI
root = tk.Tk()
root.title("User Registration")

# Labels
tk.Label(root, text="Name:").grid(row=0, column=0)
tk.Label(root, text="Username:").grid(row=1, column=0)
tk.Label(root, text="Email:").grid(row=2, column=0)
tk.Label(root, text="Password:").grid(row=3, column=0)
tk.Label(root, text="Phone:").grid(row=4, column=0)

# Entries
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)
username_entry = tk.Entry(root)
username_entry.grid(row=1, column=1)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=3, column=1)
phone_entry = tk.Entry(root)
phone_entry.grid(row=4, column=1)

# Register Button
register_button = tk.Button(root, text="Register", command=register_user)
register_button.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()