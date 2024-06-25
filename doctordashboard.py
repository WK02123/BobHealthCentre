import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
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

class DoctorDashboard:
    def __init__(self, root, doctor_id):
        self.root = root
        self.doctor_id = doctor_id
        self.root.title("Doctor Dashboard")
        self.root.geometry("1125x786")

        self.header_image = Image.open("C:/BobHealthCentre/.venv/header.jpg")
        self.bg_header_image = ImageTk.PhotoImage(self.header_image)

        self.widget_2 = tk.Frame(root, bg='#D0FDFF')
        self.widget_2.place(x=0, y=0, width=1131, height=811)
        self.widget_2.config(highlightbackground="black", highlightthickness=2)

        self.widget_3 = tk.Frame(self.widget_2)
        self.widget_3.place(x=0, y=0, width=1131, height=131)

        self.bg_label = tk.Label(self.widget_3, image=self.bg_header_image)
        self.bg_label.pack()

        self.widget_4 = tk.Frame(self.widget_2, bg='#FFFFFF')
        self.widget_4.place(x=20, y=200, width=1081, height=581)

        self.b2 = tk.Button(self.widget_2, text="Appointment List", bg='#FFBF10', fg='#873C00',
                            font=(".AppleSystemUIFont", 12, 'bold'), command=self.update_appointments_from_firebase)
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

        self.update_appointments_from_firebase()

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_mouse_wheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def update_appointments_from_firebase(self):
        appointments_data = db.child("appointments").order_by_child("status").equal_to("Accepted").get().val()

        for widget in self.inner_frame.winfo_children():
            widget.destroy()

        if appointments_data:
            displayed_appointments_count = 0
            for appointment_id, appointment_info in appointments_data.items():
                if appointment_info.get("doctor_id") == self.doctor_id:
                    patient_name = appointment_info.get("username", "Unknown")
                    appointment_date = appointment_info.get("appointment_date", "Unknown")
                    clinic = appointment_info.get("clinic_name", "Unknown")
                    details_text = f"Patient Name: {patient_name}\nAppointment Date: {appointment_date}\nClinic: {clinic}\n"

                    frame = tk.Frame(self.inner_frame, bg='#FFFFFF', relief='solid', bd=2)
                    frame.pack(fill=tk.X, padx=10, pady=10)

                    label = tk.Label(frame, text=details_text, bg='#FFFFFF', font=("Arial", 14))
                    label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

                    view_button = tk.Button(frame, text="View", command=lambda id=appointment_id: self.view_description(id))
                    view_button.pack(pady=10)

                    prescribe_button = tk.Button(frame, text="Prescription", command=lambda id=appointment_id: self.prescribe_medication(id))
                    prescribe_button.pack(padx=5, pady=10)

                    displayed_appointments_count += 1

            if displayed_appointments_count == 0:
                no_appointments_label = tk.Label(self.inner_frame, text="No accepted appointments found.", bg='#FFFFFF', font=("Arial", 14), relief='solid', bd=2)
                no_appointments_label.pack(pady=20)

        else:
            no_appointments_label = tk.Label(self.inner_frame, text="No accepted appointments found.", bg='#FFFFFF', font=("Arial", 14), relief='solid', bd=2)
            no_appointments_label.pack(pady=20)

    def view_description(self, appointment_id):
        description = db.child("appointments").child(appointment_id).child("description").get().val()
        if description:
            description_window = tk.Toplevel(self.root)
            description_window.title("Appointment Description")
            description_window.geometry("400x300")

            description_text = tk.Text(description_window, wrap=tk.WORD)
            description_text.pack(expand=True, fill=tk.BOTH)
            description_text.insert(tk.END, description)
            description_text.config(state=tk.DISABLED)
        else:
            messagebox.showinfo("Info", "No description available for this appointment.")

    def prescribe_medication(self, appointment_id):
        prescription_window = tk.Toplevel(self.root)
        prescription_window.title("Prescription")
        prescription_window.geometry("400x300")

        label = tk.Label(prescription_window, text="Prescription Details", font=("Arial", 16))
        label.pack(pady=10)

        prescription_text = tk.Text(prescription_window, wrap=tk.WORD, height=10)
        prescription_text.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)

        def submit_prescription_for_id():
            self.submit_prescription(appointment_id, prescription_text.get("1.0", tk.END))

        submit_button = tk.Button(prescription_window, text="Submit Prescription", command=submit_prescription_for_id)
        submit_button.pack(pady=10)

    def submit_prescription(self, appointment_id, prescription_details):
        if prescription_details:
            try:
                db.child("appointments").child(appointment_id).update({"prescription": prescription_details.strip()})
                messagebox.showinfo("Success", "Prescription added successfully.")
                self.update_appointments_from_firebase()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to update prescription: {str(e)}")
        else:
            messagebox.showwarning("Warning", "Prescription details cannot be empty.")

    def logout(self):
        self.root.destroy()

def authenticate_user(email, password):
    try:
        user = firebase.auth().sign_in_with_email_and_password(email, password)
        return user
    except Exception as e:
        messagebox.showerror("Login Error", str(e))
        return None

if __name__ == "__main__":
    email = "drtest1@gmail.com"
    password = "testing"

    user = authenticate_user(email, password)

    if user:
        authenticated_uid = user['localId']
        doctor_data = db.child("doctors").order_by_key().equal_to(authenticated_uid).get().val()

        if doctor_data:
            doctor_id = list(doctor_data.keys())[0]
            root = tk.Tk()
            app = DoctorDashboard(root, doctor_id)
            root.mainloop()
        else:
            messagebox.showerror("Error", "Doctor data not found.")
