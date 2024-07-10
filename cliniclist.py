import pyrebase
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import subprocess

# Firebase configuration (your firebaseConfig)
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

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

# Declare tree globally
tree = None

def fetch_pending_clinics():
    try:
        clinics = db.child("pending_clinic").get().val()
        if clinics:
            return [
                {
                    'clinic_id': key,
                    'clinic_name': value.get('name', 'Unknown'),
                    'contact_number': value.get('contact_number', 'Unknown'),
                    'address': value.get('address', 'Unknown')
                }
                for key, value in clinics.items()
            ]
        else:
            return []
    except Exception as e:
        print(f"Failed to fetch pending clinics: {e}")
        return []

def update_clinics_table():
    global tree
    for row in tree.get_children():
        tree.delete(row)
    for clinic in clinics_data:
        tree.insert('', 'end', values=(
            clinic['clinic_id'], clinic['clinic_name'], clinic['contact_number'], clinic['address']))

def open_admindashboard_page(token, user_email):
    print("admin dashboard button clicked")
    root.destroy()
    python_executable = "C:/BobHealthCentre/.venv/Scripts/python.exe"
    admin_script_path = "C:/BobHealthCentre/.venv/admindashboard.py"
    subprocess.call([python_executable, admin_script_path, token, user_email])

def logout():
    root.destroy()

def main():
    global root, tree, clinics_data

    clinics_data = fetch_pending_clinics()

    root = tk.Tk()
    root.title("Pending Clinics")

    # Load and display header image (adjust path as necessary)
    header_image_path = "C:/BobHealthCentre/.venv/header.jpg"
    header_image = Image.open(header_image_path)
    header_image = header_image.resize((1000, 100))
    header_image = ImageTk.PhotoImage(header_image)
    header_label = ttk.Label(root, image=header_image)
    header_label.image = header_image  # Keep a reference
    header_label.pack(pady=10)

    top_frame = tk.Frame(root)
    top_frame.pack(side=tk.TOP, fill=tk.X)

    title_label = ttk.Label(top_frame, text="Pending Clinics", font=("Helvetica", 20))
    title_label.pack(side=tk.LEFT, padx=10, pady=10)

    # Adjusting button style
    logout_button = ttk.Button(top_frame, text="Logout", command=logout, style='FindDoctor.TButton')
    logout_button.pack(side=tk.RIGHT, padx=10, pady=10)

    # Define token and user_email here or wherever you get them from
    token = "your_token"
    user_email = "admin@example.com"

    another_button = ttk.Button(top_frame, text="Admin Dashboard",
                                command=lambda: open_admindashboard_page(token, user_email), style='FindDoctor.TButton')
    another_button.pack(side=tk.LEFT, padx=10, pady=10)

    tree = ttk.Treeview(root, columns=('Clinic ID', 'Clinic Name', 'Contact Number', 'Address'), show='headings')

    # Add headings
    tree.heading('Clinic ID', text='Clinic ID')
    tree.heading('Clinic Name', text='Clinic Name')
    tree.heading('Contact Number', text='Contact Number')
    tree.heading('Address', text='Address')

    # Treeview configuration continues...

    # Update clinics table initially
    update_clinics_table()
    tree.pack(expand=tk.YES, fill=tk.BOTH, padx=10, pady=10)

    # Custom style
    root.tk_setPalette(background='#D0FDFF')

    style = ttk.Style()
    style.configure('FindDoctor.TButton', background='#FFBF10', foreground='#873C00', font=(".AppleSystemUIFont", 12, 'bold'))

    root.mainloop()

if __name__ == "__main__":
    main()
