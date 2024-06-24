import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QComboBox, QDateEdit, QTextEdit, QLabel
from PyQt5.QtGui import QPixmap

# Firebase initialization with Pyrebase for Realtime Database
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

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

class Ui_Form(object):
    def setupUi(self, Form, user_id, token, user_email):
        Form.setObjectName("Form")
        Form.resize(1000, 700)

        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1000, 700))
        self.widget.setStyleSheet("background-color: rgb(204, 255, 255);")

        # Load and set the header image
        self.image = QPixmap("C:/BobHealthCentre/.venv/header.jpg")
        self.bg_label = QLabel(self.widget)
        self.bg_label.setGeometry(QtCore.QRect(0, 0, 1000, 130))  # Adjust the size and position as needed
        self.bg_label.setPixmap(self.image)
        self.bg_label.setScaledContents(True)

        self.labelClinic = QtWidgets.QLabel(self.widget)
        self.labelClinic.setGeometry(QtCore.QRect(200, 250, 200, 40))  # Adjusted the position
        self.labelClinic.setText("Clinic:")
        self.labelClinic.setStyleSheet("color: black; font-size: 14px;")

        self.clinic_combo = QComboBox(self.widget)
        self.clinic_combo.setGeometry(QtCore.QRect(250, 250, 500, 40))  # Adjusted the position
        self.clinic_combo.setStyleSheet("background-color:rgba(224, 224, 224); color:rgb(255,255,255);")

        self.labelDoctor = QtWidgets.QLabel(self.widget)
        self.labelDoctor.setGeometry(QtCore.QRect(187, 320, 200, 40))  # Adjusted the position
        self.labelDoctor.setText("Doctor:")
        self.labelDoctor.setStyleSheet("color: black; font-size: 14px;")

        self.doctor_combo = QComboBox(self.widget)
        self.doctor_combo.setGeometry(QtCore.QRect(250, 320, 500, 40))  # Adjusted the position
        self.doctor_combo.setStyleSheet("background-color:rgba(224, 224, 224); color:rgb(255,255,255);")

        self.labelDate = QtWidgets.QLabel(self.widget)
        self.labelDate.setGeometry(QtCore.QRect(200, 380, 200, 40))  # Adjusted the position
        self.labelDate.setText("Date:")
        self.labelDate.setStyleSheet("color: black; font-size: 14px;")

        self.date_edit = QDateEdit(self.widget)
        self.date_edit.setGeometry(QtCore.QRect(250, 380, 500, 40))  # Adjusted the position
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setStyleSheet("background-color:rgba(224, 224, 224); color:rgb(255,255,255);")

        self.labelDescription = QtWidgets.QLabel(self.widget)
        self.labelDescription.setGeometry(QtCore.QRect(165, 475, 200, 40))  # Adjusted the position
        self.labelDescription.setText("Description:")
        self.labelDescription.setStyleSheet("color: black; font-size: 14px;")

        self.description_text = QTextEdit(self.widget)
        self.description_text.setGeometry(QtCore.QRect(250, 450, 500, 100))  # Adjusted the position
        self.description_text.setStyleSheet("background-color:rgba(224, 224, 224); color:rgb(255,255,255);")

        self.submit_button = QtWidgets.QPushButton(self.widget)
        self.submit_button.setGeometry(QtCore.QRect(400, 600, 200, 50))  # Adjusted the position
        self.submit_button.setText("Set Appointment")
        self.submit_button.setStyleSheet(
            "background-color: #FFBF10; color: #873C00; font-size: 12px; font-weight: bold;")

        self.submit_button.clicked.connect(self.set_appointment)  # Connect button click to set_appointment method

        self.submit_button2 = QtWidgets.QPushButton(self.widget)
        self.submit_button2.setGeometry(QtCore.QRect(800, 150, 150, 50))  # Adjusted the position
        self.submit_button2.setText("Log Out")
        self.submit_button2.setStyleSheet(
            "background-color: #FFBF10; color: #873C00; font-size: 12px; font-weight: bold;")

        self.submit_button3 = QtWidgets.QPushButton(self.widget)
        self.submit_button3.setGeometry(QtCore.QRect(30, 150, 150, 50))  # Adjusted the position
        self.submit_button3.setText("HomePage")
        self.submit_button3.setStyleSheet(
            "background-color: #FFBF10; color: #873C00; font-size: 12px; font-weight: bold;")

        self.submit_button4 = QtWidgets.QPushButton(self.widget)
        self.submit_button4.setGeometry(QtCore.QRect(215, 150, 150, 50))  # Adjusted the position
        self.submit_button4.setText("find Doctor")
        self.submit_button4.setStyleSheet(
            "background-color: #FFBF10; color: #873C00; font-size: 12px; font-weight: bold;")

        self.submit_button5 = QtWidgets.QPushButton(self.widget)
        self.submit_button5.setGeometry(QtCore.QRect(400, 150, 150, 50))  # Adjusted the position
        self.submit_button5.setText("Profile")
        self.submit_button5.setStyleSheet(
            "background-color: #FFBF10; color: #873C00; font-size: 12px; font-weight: bold;")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Call load_clinics to populate the clinic combo box
        self.load_clinics()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Set Appointment"))

    def load_clinics(self):
        try:
            clinics = db.child("clinics").get().val()
            if clinics:
                for clinic_id, clinic_data in clinics.items():
                    self.clinic_combo.addItem(clinic_data['name'], clinic_id)
                self.clinic_combo.currentIndexChanged.connect(self.load_doctors)
                self.load_doctors()  # Load doctors for the first clinic
            else:
                self.show_message_box("Error", "No clinics found in the database.")
        except Exception as e:
            self.show_message_box("Error", f"Failed to load clinics: {str(e)}")

    def load_doctors(self):
        self.doctor_combo.clear()
        selected_clinic_id = self.clinic_combo.currentData()
        try:
            if selected_clinic_id:
                doctors = db.child("doctors").order_by_child("clinic_id").equal_to(selected_clinic_id).get().val()
                if doctors:
                    for doctor_id, doctor_data in doctors.items():
                        self.doctor_combo.addItem(doctor_data['username'], doctor_id)
                else:
                    self.show_message_box("Error", "No doctors found for the selected clinic.")
            else:
                self.show_message_box("Error", "No clinic selected.")
        except Exception as e:
            self.show_message_box("Error", f"Failed to load doctors: {str(e)}")

    def set_appointment(self):
        clinic_id = self.clinic_combo.currentData()
        doctor_id = self.doctor_combo.currentData()
        clinic_name = self.clinic_combo.currentText()
        doctor_name = self.doctor_combo.currentText()
        appointment_date = self.date_edit.date().toString("yyyy-MM-dd")
        description = self.description_text.toPlainText()

        if not clinic_id or not doctor_id or not appointment_date or not description.strip():
            self.show_message_box("Error", "Please fill in all fields.")
            return

        try:
            # Fetch username from user_id (Assuming user details are stored in 'users' node)
            user_data = db.child("users").child(user_id).get().val()
            if user_data:
                username = user_data.get('username', 'Unknown')
            else:
                username = 'Unknown'

            # Example of storing data directly to Realtime Database
            appointment_data = {
                "clinic_id": clinic_id,
                "clinic_name": clinic_name,
                "doctor_id": doctor_id,
                "doctor_name": doctor_name,
                "appointment_date": appointment_date,
                "description": description,
                "status": "pending",
                "username": username  # Adding username to appointment data
            }

            db.child("appointments").push(appointment_data)

            self.show_message_box("Success", "Appointment set successfully!")
        except Exception as e:
            self.show_message_box("Error", f"Failed to set appointment: {str(e)}")

    def show_message_box(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(title)
        msg.setInformativeText(message)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

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

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form, user_id, token, user_email)
    Form.show()
    sys.exit(app.exec_())

