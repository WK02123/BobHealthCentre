import tkinter as tk
from tkinter import Text
from PIL import Image, ImageTk

class Ui_Form:
    def setupUi(self, Form):
        Form.title("Form")
        Form.geometry("1125x786")

        self.widget_2 = tk.Frame(Form, bg='#D0FDFF')
        self.widget_2.place(x=0, y=0, width=1131, height=811)
        self.widget_2.config(highlightbackground="black", highlightthickness=2)

        font = ("Academy Engraved LET", 12)

        self.widget_3 = tk.Frame(self.widget_2)
        self.widget_3.place(x=0, y=0, width=1131, height=131)

        # Load the image using Pillow
        self.image = Image.open("/Users/kean/Pyqt5_clinic/360_F_120571823_uUoCUfnSuxzEgOPj6FQ1nxCHNAw562Fq 2.jpg")  # Replace with your image path
        self.bg_image = ImageTk.PhotoImage(self.image)

        # Create a label and set the image
        self.bg_label = tk.Label(self.widget_3, image=self.bg_image)
        self.bg_label.pack()

        self.widget_4 = tk.Frame(self.widget_2, bg='#FFFFFF')
        self.widget_4.place(x=20, y=200, width=1081, height=581)

        self.b5 = tk.Button(self.widget_4, text="Make Appointment", bg='#FFBF10', fg='#873C00',
                            font=(".AppleSystemUIFont", 12, 'bold'), command=self.make_appointment)
        self.b5.place(x=900, y=10, width=151, height=61)

        self.b6 = tk.Button(self.widget_4, text="Clinic 1", bg='#78CBFF', fg='#873C00', command=self.clinic1)
        self.b6.place(x=50, y=40, width=100, height=32)

        self.b7 = tk.Button(self.widget_4, text="Clinic 2", bg='#78CBFF', fg='#873C00', command=self.clinic2)
        self.b7.place(x=200, y=40, width=100, height=32)

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
        self.textEdit.insert(tk.END,
                             "\nDoctor Lim Pek Hua\nSpecialty: Anesthesiology\nLanguages: English, Malay\nQualification: MBChb (Leeds University, UK), Master in Anesthesiology (UM), Fellowship in Intensive Care (MOH)")


        self.textEdit_2 = Text(self.widget_4, bg='#FFFFFF', font=("MS Shell Dlg 2", 10))
        self.textEdit_2.place(x=40, y=220, width=791, height=81)
        self.textEdit_2.insert(tk.END,
                               "\nDoctor Wong Jia Ming\nSpecialty: Cardiology & Internal Medicine\nLanguages: English, Malay, Chinese\nQualification: MBBS (Hons) (Aust), MRCP (UK), FRCP (Edin), FCCP (USA), FNHAM, AM (M'sia)")

        self.textEdit_3 = Text(self.widget_4, bg='#FFFFFF', font=("MS Shell Dlg 2", 10))
        self.textEdit_3.place(x=40, y=340, width=791, height=81)
        self.textEdit_3.insert(tk.END,
                               "\nDoctor Cannie Chong\nSpecialty: Paediatrics\nLanguages: English, Malay, Chinese, Hokkien\nQualification: MBBS (Manipal), MRCPCH (UK)")

        self.textEdit_4 = Text(self.widget_4, bg='#FFFFFF', font=("MS Shell Dlg 2", 10))
        self.textEdit_4.place(x=40, y=460, width=791, height=81)
        self.textEdit_4.insert(tk.END,
                               "\nDoctor Wong Jia Yao\nSpecialty: Dermatology\nLanguages: English, Malay, Chinese\nQualification: MBBS (Hons), MD (Dermatology)")

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



    def make_appointment(self):
        print("Make Appointment button clicked")

    def clinic1(self):
        print("Clinic 1 button clicked")

    def clinic2(self):
        print("Clinic 2 button clicked")

    def button1(self):
        print("Button 1 clicked")

    def button2(self):
        print("Button 2 clicked")

    def button3(self):
        print("Button 3 clicked")

    def button4(self):
        print("Button 4 clicked")

    def button5(self):
        print("Button 5 clicked")

    def button6(self):
        print("Button 6 clicked")

    def button7(self):
        print("Button 7 clicked")

    def button8(self):
        print("Button 8 clicked")




if __name__ == "__main__":
    root = tk.Tk()
    ui = Ui_Form()
    ui.setupUi(root)
    root.mainloop()


