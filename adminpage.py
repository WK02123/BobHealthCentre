import tkinter as tk
from tkinter import ttk

# Mock data (replace with actual database implementation)
requests_data = [
    {'patient_id': 1, 'clinic_name': 'Health Clinic', 'doctor_name': 'Dr. Smith', 'patient_name': 'John Doe',
     'request_date': '2024-06-19', 'status': 'Pending'},
    {'patient_id': 2, 'clinic_name': 'Medical Center', 'doctor_name': 'Dr. Brown', 'patient_name': 'Jane Smith',
     'request_date': '2024-06-20', 'status': 'Pending'}
]

class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.title("Appointment Page")
        MainWindow.geometry("1127x868")

        self.centralwidget = ttk.Frame(MainWindow)
        self.centralwidget.place(x=0, y=0, width=1127, height=868)

        # Header section with image
        self.label_header = tk.Label(self.centralwidget)
        self.label_header.place(x=0, y=0)
        self.label_header.img = tk.PhotoImage(file="header.png")
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

    def profile_clicked(self):
        print("Profile button clicked")

    def find_doctor_clicked(self):
        print("Find Doctor button clicked")

    def appointment_clicked(self):
        print("Appointment button clicked")

    def save_profile_clicked(self):
        print("Log Out button clicked")
        MainWindow.destroy()


# Declare tree globally
tree = None

def accept_request(event):
    # Get the item selected in the treeview
    selected_item = tree.focus()
    if selected_item:
        # Retrieve the patient ID from the item
        patient_id = int(tree.item(selected_item, 'values')[0])

        # Update the request status to 'Accepted' in the data
        for request in requests_data:
            if request['patient_id'] == patient_id:
                request['status'] = 'Accepted'
                break

        # Update the treeview display
        update_requests_table()


def reject_request(event):
    # Get the item selected in the treeview
    selected_item = tree.focus()
    if selected_item:
        # Retrieve the patient ID from the item
        patient_id = int(tree.item(selected_item, 'values')[0])

        # Update the request status to 'Rejected' in the data
        for request in requests_data:
            if request['patient_id'] == patient_id:
                request['status'] = 'Rejected'
                break

        # Update the treeview display
        update_requests_table()


def update_requests_table():
    # Clear existing table rows
    for row in tree.get_children():
        tree.delete(row)

    # Insert updated data into table
    for request in requests_data:
        tree.insert('', 'end', values=(
        request['patient_id'], request['patient_name'], request['clinic_name'], request['doctor_name'],
        request['request_date']))


def main():
    global root, tree  # Declare root and tree as global variables

    root = tk.Tk()
    app = Ui_MainWindow()
    app.setupUi(root)

    # Frame for title and logout button
    top_frame = tk.Frame(root)
    top_frame.place(x=0, y=app.label_header.img.height(), width=1127)

    # Title label at the top-left
    title_label = ttk.Label(top_frame, text="Bobby Care Centre", font=("Helvetica", 20))
    title_label.pack(side=tk.LEFT, padx=10, pady=10)

    # Create a treeview widget to display requests
    tree = ttk.Treeview(root, columns=('Patient ID', 'Patient Name', 'Clinic Name', 'Doctor Name', 'Request Date'),
                        show='headings')
    tree.heading('Patient ID', text='Patient ID')
    tree.heading('Patient Name', text='Patient Name')
    tree.heading('Clinic Name', text='Clinic Name')
    tree.heading('Doctor Name', text='Doctor Name')
    tree.heading('Request Date', text='Request Date')

    tree.column('Patient ID', width=50, anchor='center')
    tree.column('Patient Name', width=120, anchor='center')
    tree.column('Clinic Name', width=120, anchor='center')
    tree.column('Doctor Name', width=120, anchor='center')
    tree.column('Request Date', width=100, anchor='center')

    # Insert data into the treeview
    for request in requests_data:
        tree.insert('', 'end', values=(
        request['patient_id'], request['patient_name'], request['clinic_name'], request['doctor_name'],
        request['request_date']))

    tree.place(x=10, y=app.label_header.img.height() + 100, width=1107, height=300)

    # Frame to contain buttons and align them to the right
    button_frame = tk.Frame(root)
    button_frame.place(x=950, y=app.label_header.img.height() + 410, width=150, height=50)

    # Buttons for Accept and Reject actions
    reject_button = ttk.Button(button_frame, text="Reject")
    accept_button = ttk.Button(button_frame, text="Accept")

    # Place buttons in the frame
    reject_button.pack(side=tk.RIGHT, padx=5)
    accept_button.pack(side=tk.RIGHT, padx=5)

    # Bind button clicks to functions
    reject_button.bind("<Button-1>", reject_request)
    accept_button.bind("<Button-1>", accept_request)

    root.mainloop()


if __name__ == "__main__":
    main()
