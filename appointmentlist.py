import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pyrebase
from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
from profilepage import Ui_ProfilePage

# Firebase configuration
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
db = firebase.database()

class AppointmentList(object):
    def __init__(self, root, user_id, user_email, token, username):
        self.root = root
        self.user_id = user_id
        self.user_email = user_email
        self.token = token
        self.username = username
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Appointment List")
        self.root.geometry("1125x786")

        # Load and display the header image (replace with your path)
        self.header_image = Image.open("C:/BobHealthCentre/.venv/header.jpg")
        self.bg_header_image = ImageTk.PhotoImage(self.header_image)

        self.widget_2 = tk.Frame(self.root, bg='#D0FDFF')
        self.widget_2.place(x=0, y=0, width=1131, height=811)
        self.widget_2.config(highlightbackground="black", highlightthickness=2)

        self.widget_3 = tk.Frame(self.widget_2)
        self.widget_3.place(x=0, y=0, width=1131, height=131)

        self.bg_label = tk.Label(self.widget_3, image=self.bg_header_image)
        self.bg_label.pack()

        self.widget_4 = tk.Frame(self.widget_2, bg='#FFFFFF')
        self.widget_4.place(x=20, y=200, width=1081, height=581)

        self.b2 = tk.Button(self.widget_2, text="Go Back", bg='#FFBF10', fg='#873C00',
                            font=(".AppleSystemUIFont", 12, 'bold'),
                            command=lambda: self.open_profile_page(self.user_id, self.token, self.user_email))
        self.b2.place(x=40, y=150, width=141, height=41)

        self.b4 = tk.Button(self.widget_2, text="Log out", bg='#FFBF10', fg='#873C00',
                            font=(".AppleSystemUIFont", 12, 'bold'), command=self.logout)
        self.b4.place(x=940, y=140, width=141, height=41)

        self.scrollable_frame = ttk.Frame(self.widget_4, style="My.TFrame")
        self.scrollable_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.scrollbar = ttk.Scrollbar(self.scrollable_frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas = tk.Canvas(self.scrollable_frame, bg='#FFFFFF', yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar.config(command=self.canvas.yview)

        self.inner_frame = tk.Frame(self.canvas, bg='#FFFFFF')
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor='nw')

        self.inner_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)

        self.display_appointments()

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_mouse_wheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def display_appointments(self):
        # Retrieve the user's appointments from Firebase
        appointments = db.child("appointments").order_by_child("username").equal_to(self.username).get().val()
        if appointments:
            for widget in self.inner_frame.winfo_children():
                widget.destroy()

            for appointment_id, appointment_info in appointments.items():
                appointment_details = (
                    f"Appointment Date: {appointment_info['appointment_date']}\n"
                    f"Clinic: {appointment_info['clinic_name']}\n"
                    f"Description: {appointment_info['description']}\n"
                    f"Doctor: {appointment_info['doctor_name']}\n"
                    f"Status: {appointment_info['status']}\n\n"
                )

                frame = tk.Frame(self.inner_frame, bg='#FFFFFF', relief='solid', bd=2)
                frame.pack(fill=tk.X, padx=10, pady=10)

                label = tk.Label(frame, text=appointment_details, bg='#FFFFFF', font=("Arial", 14))
                label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

                # Add Prescription button
                btn_prescription = tk.Button(frame, text="Prescription", bg='#FFBF10', fg='#873C00',
                                             font=(".AppleSystemUIFont", 12, 'bold'),
                                             command=lambda appointment_id=appointment_id: self.show_prescription(appointment_id))
                btn_prescription.pack(side=tk.RIGHT)

        else:
            no_appointments_label = tk.Label(self.inner_frame, text="No appointments found.", bg='#FFFFFF', font=("Arial", 14), relief='solid', bd=2)
            no_appointments_label.pack(pady=20)

    def show_prescription(self, appointment_id):
        # Retrieve prescription details from Firebase based on appointment_id
        appointment_info = db.child("appointments").child(appointment_id).get().val()
        if appointment_info:
            prescription = appointment_info.get('prescription', 'No prescription available.')
            messagebox.showinfo("Prescription", prescription)
        else:
            messagebox.showinfo("Prescription", "No prescription available.")

    def open_profile_page(self, user_id, token, user_email):
        print("Opening Profile Page...")
        try:
            user_info = db.child("users").child(user_id).get(token).val()
            if user_info:
                username = user_info.get("username")
                print(f"Username retrieved: {username}")

                # Close the Tkinter root window
                self.root.destroy()

                # Initialize QApplication
                app = QtWidgets.QApplication(sys.argv)

                # Create and setup the profile page window
                self.profile_page_window = QtWidgets.QMainWindow()
                self.profile_page = Ui_ProfilePage(user_id, token, user_email, username)
                self.profile_page.setupUi(self.profile_page_window)

                # Set the window size
                self.profile_page_window.resize(1120, 750)

                # Show the profile page window
                self.profile_page_window.show()

                # Start the PyQt5 application event loop
                sys.exit(app.exec_())
            else:
                print("User info not found.")
        except Exception as e:
            print("Failed to open profile page:", e)

    def logout(self):
        self.root.destroy()

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 5:
        print("Usage: appointment_list.py <user_id> <user_email> <token> <username>")
        sys.exit(1)

    user_id = sys.argv[1]
    user_email = sys.argv[2]
    token = sys.argv[3]
    username = sys.argv[4]

    root = tk.Tk()
    ui = AppointmentList(root, user_id, user_email, token, username)
    root.mainloop()
