import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from datetime import datetime
import subprocess

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

class ClinicRegistrationForm(object):
    def setupUi(self, Form):
        self.main_window = Form
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

        self.labelClinicName = QLabel(self.widget)
        self.labelClinicName.setGeometry(QtCore.QRect(200, 250, 200, 40))
        self.labelClinicName.setText("Clinic Name:")
        self.labelClinicName.setStyleSheet("color: black; font-size: 14px;")

        self.clinic_name_edit = QLineEdit(self.widget)
        self.clinic_name_edit.setGeometry(QtCore.QRect(350, 250, 400, 40))
        self.clinic_name_edit.setStyleSheet("background-color: rgba(224, 224, 224); color: rgb(0, 0, 0);")

        self.labelContactNumber = QLabel(self.widget)
        self.labelContactNumber.setGeometry(QtCore.QRect(200, 320, 200, 40))
        self.labelContactNumber.setText("Contact Number:")
        self.labelContactNumber.setStyleSheet("color: black; font-size: 14px;")

        self.contact_number_edit = QLineEdit(self.widget)
        self.contact_number_edit.setGeometry(QtCore.QRect(350, 320, 400, 40))
        self.contact_number_edit.setStyleSheet("background-color: rgba(224, 224, 224); color: rgb(0, 0, 0);")

        self.labelAddress = QLabel(self.widget)
        self.labelAddress.setGeometry(QtCore.QRect(200, 390, 200, 40))
        self.labelAddress.setText("Address:")
        self.labelAddress.setStyleSheet("color: black; font-size: 14px;")

        self.address_text = QLineEdit(self.widget)
        self.address_text.setGeometry(QtCore.QRect(350, 390, 400, 40))
        self.address_text.setStyleSheet("background-color: rgba(224, 224, 224); color: rgb(0, 0, 0);")

        self.submit_button = QPushButton(self.widget)
        self.submit_button.setGeometry(QtCore.QRect(400, 460, 200, 50))
        self.submit_button.setText("Register Clinic")
        self.submit_button.setStyleSheet(
            "background-color: #FFBF10; color: #873C00; font-size: 12px; font-weight: bold;")

        self.submit_button.clicked.connect(self.register_clinic)


        self.submit_button3 = QPushButton(self.widget)
        self.submit_button3.setGeometry(QtCore.QRect(30, 150, 150, 50))
        self.submit_button3.setText("Go Back")
        self.submit_button3.setStyleSheet(
            "background-color: #FFBF10; color: #873C00; font-size: 12px; font-weight: bold;")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.submit_button3.clicked.connect(self.go_back)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Clinic Registration"))

    def go_back(self):
        try:
            self.main_window.close()
            # Get the path to the current Python interpreter
            python_executable = sys.executable

            # Execute register.py using subprocess with the same Python interpreter
        except Exception as e:
            print("Failed to open doctor register page:", e)

    def logout(self):
        print("Logging out...")
        QtWidgets.qApp.quit()

    def register_clinic(self):
        clinic_name = self.clinic_name_edit.text()
        contact_number = self.contact_number_edit.text()
        address = self.address_text.text()

        if not clinic_name or not contact_number or not address:
            self.show_message_box("Error", "Please fill in all fields.")
            return

        try:
            clinic_data = {
                "name": clinic_name,
                "contact_number": contact_number,
                "address": address
            }

            db.child("pending_clinic").push(clinic_data)

            self.show_message_box("Success", "Clinic registered successfully!")
        except Exception as e:
            self.show_message_box("Error", f"Failed to register clinic: {str(e)}")

    def show_message_box(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(title)
        msg.setInformativeText(message)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = ClinicRegistrationForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
