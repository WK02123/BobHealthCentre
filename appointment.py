import tkinter as tk
from tkinter import ttk

class Ui_MainWindow:

    def setupUi(self, MainWindow):
        MainWindow.title("Appointment Page")
        MainWindow.geometry("1127x868")

        self.centralwidget = ttk.Frame(MainWindow)
        self.centralwidget.place(x=0, y=0, width=1127, height=868)

        # Header section with image
        self.label_header = tk.Label(self.centralwidget)
        self.label_header.place(x=0, y=0)
        self.label_header.img = tk.PhotoImage(file="hearder.png")
        self.label_header.config(image=self.label_header.img)

        # Resize label to fit the image dimensions
        image_width = self.label_header.img.width()
        image_height = self.label_header.img.height()
        self.label_header.config(width=1127, height=image_height)

        # Buttons
        button_y_offset = 200  # Adjust this value as needed
        self.toolButton_2 = ttk.Button(self.centralwidget, text="Profile", style="App.TButton", command=self.profile_clicked)
        self.toolButton_2.place(x=440, y=55 + button_y_offset, width=111, height=51)

        self.toolButton_4 = ttk.Button(self.centralwidget, text="Find Doctor", style="App.TButton", command=self.find_doctor_clicked)
        self.toolButton_4.place(x=20, y=55 + button_y_offset, width=121, height=51)

        self.toolButton_5 = ttk.Button(self.centralwidget, text="Appointment", style="App.TButton", command=self.appointment_clicked)
        self.toolButton_5.place(x=210, y=55 + button_y_offset, width=141, height=51)

        self.pushButton = ttk.Button(self.centralwidget, text="Log Out", style="App.TButton", command=self.save_profile_clicked)
        self.pushButton.place(x=980, y=55 + button_y_offset, width=91, height=55)

        # Appointment Form Section
        appointment_y_offset = 200  # Adjust this value as needed
        self.label = ttk.Label(self.centralwidget, background="#D0FDFF")
        self.label.place(x=0, y=110 + appointment_y_offset, width=1127, height=661)

        self.create_appointment_form(300, 120 + appointment_y_offset, "Upcomming Appointment")

        MainWindow.config(menu=self.centralwidget)

        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.title("Appointment Page")

    def create_appointment_form(self, x, y, title):
        frame = ttk.LabelFrame(self.centralwidget, text=title, relief="solid")
        frame.place(x=x, y=y, width=550, height=450)

        tk.Label(frame, text="Clinic:", font=("Helvetica", 20)).grid(row=0, column=0, padx=20, pady=10, sticky="w")
        ttk.Entry(frame, font=("Helvetica", 20)).grid(row=0, column=1, padx=10, pady=10, sticky="w")

        tk.Label(frame, text="Doctor:", font=("Helvetica", 20)).grid(row=1, column=0, padx=20, pady=10, sticky="w")
        ttk.Entry(frame, font=("Helvetica", 20)).grid(row=1, column=1, padx=10, pady=5, sticky="w")

        tk.Label(frame, text="Date:", font=("Helvetica", 20)).grid(row=2, column=0, padx=20, pady=10, sticky="w")
        ttk.Entry(frame, font=("Helvetica", 20)).grid(row=2, column=1, padx=10, pady=5, sticky="w")

        tk.Label(frame, text="Status:", font=("Helvetica", 20)).grid(row=3, column=0, padx=20, pady=10, sticky="w")
        ttk.Entry(frame, font=("Helvetica", 20)).grid(row=3, column=1, padx=10, pady=5, sticky="w")

    def profile_clicked(self):
        self.show_message("Profile button clicked.")

    def find_doctor_clicked(self):
        self.show_message("Find Doctor button clicked.")

    def appointment_clicked(self):
        self.show_message("Appointment button clicked.")

    def save_profile_clicked(self):
        self.show_message("Save Profile button clicked.")

    def show_message(self, message):
        # Function to display a message (can be replaced with actual functionality)
        print(message)

if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.configure("App.TButton", font=('Helvetica', 12), foreground="black", background="#FFFFFF", borderwidth=0, padding=5)
    style.map("App.TButton", background=[("active", "#1C86EE")])
    ui = Ui_MainWindow()
    ui.setupUi(root)
    root.mainloop()
