import pyrebase
import tkinter as tk
from tkinter import ttk

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

# Declare tree globally
tree = None

def fetch_appointments():
    try:
        appointments = db.child("appointments").get().val()
        if appointments:
            return [
                {
                    'appointment_id': key,
                    'clinic_name': value.get('clinic_name', 'Unknown'),
                    'doctor_name': value.get('doctor_name', 'Unknown'),
                    'patient_name': value.get('patient_name', 'Unknown'),
                    'request_date': value.get('appointment_date', 'Unknown'),
                    'status': value.get('status', 'Pending')
                }
                for key, value in appointments.items()
            ]
        else:
            return []
    except Exception as e:
        print(f"Failed to fetch appointments: {e}")
        return []

def accept_request(event):
    selected_item = tree.focus()
    if selected_item:
        appointment_id = tree.item(selected_item, 'values')[0]
        for request in requests_data:
            if request['appointment_id'] == appointment_id:
                request['status'] = 'Accepted'
                db.child("appointments").child(appointment_id).update({"status": "Accepted"})
                break
        update_requests_table()

def reject_request(event):
    selected_item = tree.focus()
    if selected_item:
        appointment_id = tree.item(selected_item, 'values')[0]
        for request in requests_data:
            if request['appointment_id'] == appointment_id:
                request['status'] = 'Rejected'
                db.child("appointments").child(appointment_id).update({"status": "Rejected"})
                break
        update_requests_table()

def logout():
    root.destroy()

def update_requests_table():
    for row in tree.get_children():
        tree.delete(row)
    for request in requests_data:
        tree.insert('', 'end', values=(
            request['appointment_id'], request['patient_name'], request['clinic_name'], request['doctor_name'], request['request_date'], request['status']))

def main(token, user_email):
    global root, tree, requests_data

    requests_data = fetch_appointments()

    root = tk.Tk()
    root.title("Clinic Admin Dashboard")

    top_frame = tk.Frame(root)
    top_frame.pack(side=tk.TOP, fill=tk.X)

    title_label = ttk.Label(top_frame, text="Bobby Care Centre", font=("Helvetica", 20))
    title_label.pack(side=tk.LEFT, padx=10, pady=10)

    logout_button = ttk.Button(top_frame, text="Logout", command=logout)
    logout_button.pack(side=tk.RIGHT, padx=10, pady=10)

    tree = ttk.Treeview(root, columns=('Appointment ID', 'Patient Name', 'Clinic Name', 'Doctor Name', 'Request Date', 'Status'), show='headings')
    tree.heading('Appointment ID', text='Appointment ID')
    tree.heading('Patient Name', text='Patient Name')
    tree.heading('Clinic Name', text='Clinic Name')
    tree.heading('Doctor Name', text='Doctor Name')
    tree.heading('Request Date', text='Request Date')
    tree.heading('Status', text='Status')

    tree.column('Appointment ID', width=100, anchor='center')
    tree.column('Patient Name', width=120, anchor='center')
    tree.column('Clinic Name', width=120, anchor='center')
    tree.column('Doctor Name', width=120, anchor='center')
    tree.column('Request Date', width=100, anchor='center')
    tree.column('Status', width=80, anchor='center')

    update_requests_table()
    tree.pack(expand=tk.YES, fill=tk.BOTH, padx=10, pady=10)

    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.RIGHT, padx=10, pady=10)

    reject_button = ttk.Button(button_frame, text="Reject")
    accept_button = ttk.Button(button_frame, text="Accept")

    reject_button.pack(side=tk.RIGHT, padx=5)
    accept_button.pack(side=tk.RIGHT, padx=5)

    reject_button.bind("<Button-1>", reject_request)
    accept_button.bind("<Button-1>", accept_request)

    root.mainloop()

if __name__ == "__main__":
    main()
