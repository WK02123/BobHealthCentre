import tkinter as tk
from tkinter import messagebox, ttk
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
        self.root.geometry("800x600")

        # Header
        self.header_frame = tk.Frame(self.root, bg='#D0FDFF', height=100)
        self.header_frame.pack(fill=tk.X)

        self.header_label = tk.Label(self.header_frame, text="Doctor Dashboard", font=("Arial", 24), bg='#D0FDFF',
                                     fg='#000000')
        self.header_label.pack(pady=20)

        # Main content frame for appointments
        self.appointments_frame = tk.Frame(self.root, bg='#FFFFFF')
        self.appointments_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Scrollbar for appointments frame
        scrollbar = ttk.Scrollbar(self.appointments_frame, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Canvas for scrollable area
        self.canvas = tk.Canvas(self.appointments_frame, bg='#FFFFFF', yscrollcommand=scrollbar.set)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Configure scrollbar to scroll canvas
        scrollbar.config(command=self.canvas.yview)

        # Frame to contain the scrollable content
        self.scrollable_frame = tk.Frame(self.canvas, bg='#FFFFFF')
        self.scrollable_frame.pack(fill=tk.BOTH, expand=True)

        # Update appointments from Firebase
        self.update_appointments_from_firebase()

        # Bind canvas scrolling to mousewheel
        self.canvas.bind_all("<MouseWheel>",
                             lambda event: self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))

    def update_appointments_from_firebase(self):
        # Retrieve appointment details from Firebase where doctor_id matches and status is Accepted
        appointments_data = db.child("appointments").order_by_child("status").equal_to("Accepted").get().val()

        if appointments_data:
            print("Appointments Data Retrieved:")
            print(appointments_data)  # Print all retrieved appointments for debug

            # Clear existing widgets in scrollable_frame
            for widget in self.scrollable_frame.winfo_children():
                widget.destroy()

            # Filter and display appointments for the logged-in doctor
            displayed_appointments_count = 0
            for appointment_id, appointment_info in appointments_data.items():
                if appointment_info.get("doctor_id") == self.doctor_id:
                    patient_name = appointment_info.get("username", "Unknown")
                    appointment_date = appointment_info.get("appointment_date", "Unknown")
                    clinic = appointment_info.get("clinic_name", "Unknown")
                    details_text = f"Patient Name: {patient_name}\nAppointment Date: {appointment_date}\nClinic: {clinic}\n"

                    print(f"Appointment ID: {appointment_id}")
                    print(f"Details: {details_text}")

                    frame = tk.Frame(self.scrollable_frame, bg='#FFFFFF', relief='solid', bd=2)
                    frame.pack(fill=tk.X, padx=10, pady=10)

                    label = tk.Label(frame, text=details_text, bg='#FFFFFF', font=("Arial", 14))
                    label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

                    # Use a bound lambda to correctly capture appointment_id
                    view_button = tk.Button(frame, text="View",
                                            command=lambda id=appointment_id: self.view_description(id))
                    view_button.pack(pady=10)

                    prescribe_button = tk.Button(frame, text="Prescription",
                                                 command=lambda id=appointment_id: self.prescribe_medication(id))
                    prescribe_button.pack(padx=5, pady=10)

                    displayed_appointments_count += 1

            if displayed_appointments_count == 0:
                no_appointments_label = tk.Label(self.scrollable_frame, text="No accepted appointments found.",
                                                 bg='#FFFFFF', font=("Arial", 14), relief='solid', bd=2)
                no_appointments_label.pack(pady=20)

        else:
            print("No Appointments Data Found")
            # Clear existing widgets in scrollable_frame
            for widget in self.scrollable_frame.winfo_children():
                widget.destroy()

            no_appointments_label = tk.Label(self.scrollable_frame, text="No accepted appointments found.",
                                             bg='#FFFFFF', font=("Arial", 14), relief='solid', bd=2)
            no_appointments_label.pack(pady=20)

        # Attach scrollable_frame to canvas
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

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

        # Define a function that captures the correct appointment_id and prescription_text
        def submit_prescription_for_id():
            self.submit_prescription(appointment_id, prescription_text.get("1.0", tk.END))

        submit_button = tk.Button(prescription_window, text="Submit Prescription", command=submit_prescription_for_id)
        submit_button.pack(pady=10)

    def submit_prescription(self, appointment_id, prescription_details):
        if prescription_details:
            try:
                # Update the prescription field for the specified appointment_id in Firebase
                db.child("appointments").child(appointment_id).update({
                    "prescription": prescription_details.strip()  # Strip any leading/trailing whitespace
                })

                messagebox.showinfo("Success", "Prescription added successfully.")
                # After updating, you might want to refresh the appointments displayed
                self.update_appointments_from_firebase()

            except Exception as e:
                messagebox.showerror("Error", f"Failed to update prescription: {str(e)}")
        else:
            messagebox.showwarning("Warning", "Prescription details cannot be empty.")


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
            doctor_id = list(doctor_data.keys())[0]  # Assuming only one doctor is retrieved
            root = tk.Tk()
            app = DoctorDashboard(root, doctor_id)
            root.mainloop()
        else:
            messagebox.showerror("Error", "Doctor data not found.")
