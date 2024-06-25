import sys
import tkinter as tk
from tkinter import Text
from PIL import Image, ImageTk
import subprocess
import pyrebase

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

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

class Ui_Form:
    def setupUi(self, Form, user_id, token, user_email):
        self.Form = Form
        self.user_id = user_id
        self.token = token
        self.user_email = user_email

        Form.title("Form")
        Form.geometry("1125x786")

        self.widget_2 = tk.Frame(Form, bg='#D0FDFF')
        self.widget_2.place(x=0, y=0, width=1131, height=811)
        self.widget_2.config(highlightbackground="black", highlightthickness=2)

        font = ("Academy Engraved LET", 12)

        self.widget_3 = tk.Frame(self.widget_2)
        self.widget_3.place(x=0, y=0, width=1131, height=131)

        # Load the image using Pillow (adjust path accordingly)
        self.image = Image.open("C:/BobHealthCentre/.venv/header.jpg")
        self.bg_image = ImageTk.PhotoImage(self.image)

        # Create a label and set the image
        self.bg_label = tk.Label(self.widget_3, image=self.bg_image)
        self.bg_label.pack()

        self.widget_4 = tk.Frame(self.widget_2, bg='#FFFFFF')
        self.widget_4.place(x=20, y=200, width=1081, height=581)

        clinic_label = tk.Label(self.widget_3, text="Clinic 2", font=("Arial", 24), bg='#D0FDFF', fg='#000000')
        clinic_label.place(x=65, y=95, width=100, height=32)

        self.b5 = tk.Button(self.widget_4, text="Make Appointment", bg='#FFBF10', fg='#873C00',
                            font=(".AppleSystemUIFont", 12, 'bold'), command=self.make_appointment)
        self.b5.place(x=880, y=10, width=151, height=61)

        self.b6 = tk.Button(self.widget_4, text="Clinic 1", bg='#78CBFF', fg='#873C00', command=self.open_find_doc1)
        self.b6.place(x=50, y=10, width=100, height=32)

        self.b7 = tk.Button(self.widget_4, text="Clinic 2", bg='#78CBFF', fg='#873C00', command=self.clinic1)
        self.b7.place(x=200, y=10, width=100, height=32)

        self.label = tk.Label(self.widget_4, bg='#FFFFFF', font=("MS Shell Dlg 2", 10, 'bold'), relief='solid', bd=2)
        self.label.place(x=20, y=90, width=1031, height=111)

        self.label_2 = tk.Label(self.widget_4, bg='#FFFFFF', font=("MS Shell Dlg 2", 10, 'bold'), relief='solid', bd=2)
        self.label_2.place(x=20, y=210, width=1031, height=111)

        self.label_3 = tk.Label(self.widget_4, bg='#FFFFFF', font=("MS Shell Dlg 2", 10, 'bold'), relief='solid', bd=2)
        self.label_3.place(x=20, y=330, width=1031, height=111)

        self.label_4 = tk.Label(self.widget_4, bg='#FFFFFF', font=("MS Shell Dlg 2", 10, 'bold'), relief='solid', bd=2)
        self.label_4.place(x=20, y=450, width=1031, height=111)

        self.textEdit = Text(self.widget_4, bg='#FFFFFF', font=("MS Shell Dlg 2", 10))
        self.textEdit.place(x=40, y=105, width=980, height=81)

        self.textEdit_2 = Text(self.widget_4, bg='#FFFFFF', font=("MS Shell Dlg 2", 10))
        self.textEdit_2.place(x=40, y=225, width=980, height=81)

        self.b2 = tk.Button(self.widget_2, text="Appointment List", bg='#FFBF10', fg='#873C00',
                            font=(".AppleSystemUIFont", 12, 'bold'), command=self.button2)
        self.b2.place(x=40, y=150, width=141, height=41)

        self.b3 = tk.Button(self.widget_2, text="find Doctor", bg='#FFBF10', fg='#873C00',
                            font=(".AppleSystemUIFont", 12, 'bold'), command=self.button3)
        self.b3.place(x=210, y=150, width=141, height=41)

        self.b1 = tk.Button(self.widget_2, text="Profile", bg='#FFBF10', fg='#873C00',
                            font=(".AppleSystemUIFont", 12, 'bold'), command=self.button1)
        self.b1.place(x=380, y=150, width=141, height=41)

        self.b4 = tk.Button(self.widget_2, text="Log out", bg='#FFBF10', fg='#873C00',
                            font=(".AppleSystemUIFont", 12, 'bold'), command=self.button4)
        self.b4.place(x=940, y=140, width=141, height=41)

        self.selected_doctors = []

        # Retrieve and display doctors in Clinic 2
        self.display_doctors_in_clinic2()

    def make_appointment(self):
        print("Make Appointment button clicked")

    def clinic1(self):
        print("Clinic 1 button clicked")

    def open_find_doc1(self):
        self.Form.withdraw()  # Hide the current form
        python_executable = "C:/BobHealthCentre/.venv/Scripts/python.exe"  # Adjust the path to your virtual environment's Python executable
        subprocess.call([python_executable, "C:/BobHealthCentre/.venv/finddoctor.py", self.user_id, self.token,
                         self.user_email])  # Open finddoctor.py

    def button1(self):
        print("Button 1 clicked")

    def button2(self):
        print("Button 2 clicked")

    def button3(self):
        print("Button 3 clicked")

    def button4(self):
        print("Button 4 clicked")

    def display_doctors_in_clinic2(self):
        # Retrieve doctors in Clinic 2 from the database
        clinic2_doctors = db.child("doctors").get().val()
        clinic2_doctor_details = []
        if clinic2_doctors:
            for doctor_id, doctor_info in clinic2_doctors.items():
                if doctor_info.get("clinic_id") == "clinic2":
                    doctor_details = f"Name: {doctor_info['username']}\nSpecialty: {doctor_info['specialty']}\nLanguage: {doctor_info['language']}\n\n"
                    clinic2_doctor_details.append(doctor_details)

            # Display doctor details in text widget
            for i, details in enumerate(clinic2_doctor_details):
                if i == 0:
                    self.textEdit.insert(tk.END, details)
                elif i == 1:
                    self.textEdit_2.insert(tk.END, details)
                elif i == 2:
                    self.textEdit_3.insert(tk.END, details)
                elif i == 3:
                    self.textEdit_4.insert(tk.END, details)
        else:
            print("No doctors found in Clinic 2.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: finddoctor.py <user_id> <token> <user_email>")
        sys.exit(1)

    user_id = sys.argv[1]
    token = sys.argv[2]
    user_email = sys.argv[3]

    # For debugging: print the arguments to verify
    print(f"user_id: {user_id}")
    print(f"token: {token}")
    print(f"user_email: {user_email}")

    root = tk.Tk()
    ui = Ui_Form()
    ui.setupUi(root, user_id, token, user_email)
    root.mainloop()
