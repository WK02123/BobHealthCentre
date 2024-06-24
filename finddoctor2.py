import tkinter as tk
from tkinter import Text
from PIL import Image, ImageTk
import subprocess
class Ui_Form:
    def setupUi(self, Form):
        self.Form = Form
        Form.title("Form")
        Form.geometry("1125x786")

        self.widget_2 = tk.Frame(Form, bg='#D0FDFF')
        self.widget_2.place(x=0, y=0, width=1131, height=811)
        self.widget_2.config(highlightbackground="black", highlightthickness=2)

        font = ("Academy Engraved LET", 12)

        self.widget_3 = tk.Frame(self.widget_2)
        self.widget_3.place(x=0, y=0, width=1131, height=131)

        # Load the image using Pillow (adjust path accordingly)
        self.image = Image.open("/Users/kean/Pyqt5_clinic/360_F_120571823_uUoCUfnSuxzEgOPj6FQ1nxCHNAw562Fq 2.jpg")
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
        self.textEdit.place(x=40, y=105, width=791, height=81)

        self.textEdit_2 = Text(self.widget_4, bg='#FFFFFF', font=("MS Shell Dlg 2", 10))
        self.textEdit_2.place(x=40, y=225, width=791, height=81)

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

        self.b6 = tk.Button(self.widget_2, text="select", bg='#FFBF10', fg='#873C00',
                            font=(".AppleSystemUIFont", 12, 'bold'), command=self.button5)
        self.b6.place(x=900, y=330, width=141, height=41)

        self.b7 = tk.Button(self.widget_2, text="select", bg='#FFBF10', fg='#873C00',
                            font=(".AppleSystemUIFont", 12, 'bold'), command=self.button6)
        self.b7.place(x=900, y=450, width=141, height=41)

        self.b8 = tk.Button(self.widget_2, text="select", bg='#FFBF10', fg='#873C00',
                            font=(".AppleSystemUIFont", 12, 'bold'), command=self.button7)
        self.b8.place(x=900, y=565, width=141, height=41)

        self.b9 = tk.Button(self.widget_2, text="select", bg='#FFBF10', fg='#873C00',
                            font=(".AppleSystemUIFont", 12, 'bold'), command=self.button8)
        self.b9.place(x=900, y=685, width=141, height=41)

        self.selected_doctors = []


    def make_appointment(self):
        print("Make Appointment button clicked")

    def clinic1(self):
        print("Clinic 1 button clicked")

    def open_find_doc1(self):
        self.Form.withdraw()  # Hide the current form
        python_executable = "C:/BobHealthCentre/.venv/Scripts/python.exe"  # Adjust the path to your virtual environment's Python executable
        subprocess.call([python_executable, "C:/BobHealthCentre/.venv/finddoctor.py"])  # Open finddoctor2.py

    def button1(self):
        print("Button 1 clicked")

    def button2(self):
        print("Button 2 clicked")

    def button3(self):
        print("Button 3 clicked")

    def button4(self):
        print("Button 4 clicked")

    def button5(self):
        doctor_info = self.textEdit.get("1.0", tk.END).strip()
        self.selected_doctors.append(doctor_info)
        print(f"Doctor selected: {doctor_info}")

    def button6(self):
        doctor_info = self.textEdit_2.get("1.0", tk.END).strip()
        self.selected_doctors.append(doctor_info)
        print(f"Doctor selected: {doctor_info}")

    def button7(self):
        doctor_info = self.textEdit_3.get("1.0", tk.END).strip()
        self.selected_doctors.append(doctor_info)
        print(f"Doctor selected: {doctor_info}")

    def button8(self):
        doctor_info = self.textEdit_4.get("1.0", tk.END).strip()
        self.selected_doctors.append(doctor_info)
        print(f"Doctor selected: {doctor_info}")


if __name__ == "__main__":
    root = tk.Tk()
    ui = Ui_Form()
    ui.setupUi(root)
    root.mainloop()
