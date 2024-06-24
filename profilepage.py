import sys
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
import pyrebase
from functools import partial
from PyQt5.QtGui import QPixmap


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
auth = firebase.auth()  # Initialize auth object
db = firebase.database()

class Ui_ProfilePage(object):
    def __init__(self, user_id, token, user_email):
        self.user_id = user_id
        self.token = token
        self.user_email = user_email

    def setupUi(self, ProfilePage):
        self.ProfilePage = ProfilePage  # Store ProfilePage instance
        self.centralwidget = QtWidgets.QWidget(ProfilePage)
        self.centralwidget.setObjectName("centralwidget")

        # Header section
        self.header_label = QtWidgets.QLabel(self.centralwidget)
        self.header_label.setGeometry(QtCore.QRect(0, 0, 1127, 110))
        self.header_label.setStyleSheet("background-color: #097969; color: white;")
        self.header_label.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.header_label.setFont(font)
        self.header_label.setText("BobHealthCare")
        self.menu_button1 = QtWidgets.QPushButton(self.centralwidget)
        self.menu_button1.setGeometry(QtCore.QRect(20, 80, 120, 30))
        self.menu_button1.setText("Appointment List")  # Changed label to "Appointment List"
        self.menu_button1.clicked.connect(partial(self.menu_clicked, "Appointment List"))  # Changed signal handler parameter

        self.menu_button2 = QtWidgets.QPushButton(self.centralwidget)
        self.menu_button2.setGeometry(QtCore.QRect(150, 80, 120, 30))
        self.menu_button2.setText("Find Doctor")  # Changed label to "Find Doctor"
        self.menu_button2.clicked.connect(self.open_find_doctor)  # Changed signal handler to open_find_doctor

        self.logout_button = QtWidgets.QPushButton(self.centralwidget)
        self.logout_button.setGeometry(QtCore.QRect(1000, 80, 100, 30))
        self.logout_button.setText("Logout")
        self.logout_button.clicked.connect(self.menu_clicked)

        # Profile Information Section
        self.profile_label = QtWidgets.QLabel(self.centralwidget)
        self.profile_label.setGeometry(QtCore.QRect(0, 110, 1131, 661))
        self.profile_label.setStyleSheet("background-color: #AFE1AF;")

        self.profile_title_label = QtWidgets.QLabel(self.centralwidget)
        self.profile_title_label.setGeometry(QtCore.QRect(368, 110, 391, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.profile_title_label.setFont(font)
        self.profile_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.profile_title_label.setText("My Profile")

        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(20, 200, 301, 41))
        self.name_label.setText("Username:")
        self.name_input = QtWidgets.QLineEdit(self.centralwidget)
        self.name_input.setGeometry(QtCore.QRect(20, 250, 1081, 51))

        self.phone_label = QtWidgets.QLabel(self.centralwidget)
        self.phone_label.setGeometry(QtCore.QRect(20, 310, 301, 41))
        self.phone_label.setText("Phone Number:")
        self.phone_input = QtWidgets.QLineEdit(self.centralwidget)
        self.phone_input.setGeometry(QtCore.QRect(20, 360, 1081, 51))

        self.email_label = QtWidgets.QLabel(self.centralwidget)
        self.email_label.setGeometry(QtCore.QRect(20, 420, 301, 41))
        self.email_label.setText("Email-Address:")
        self.email_input = QtWidgets.QLineEdit(self.centralwidget)
        self.email_input.setGeometry(QtCore.QRect(20, 470, 1081, 51))
        self.email_input.setReadOnly(True)

        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(20, 530, 301, 41))
        self.password_label.setText("Password:")
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(20, 580, 1081, 51))
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)

        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(500, 650, 121, 41))
        self.submit_button.setText("Submit")
        self.submit_button.clicked.connect(self.update_user_data)

        ProfilePage.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProfilePage)
        QtCore.QMetaObject.connectSlotsByName(ProfilePage)

        self.fetch_user_details()

    def retranslateUi(self, ProfilePage):
        _translate = QtCore.QCoreApplication.translate
        ProfilePage.setWindowTitle(_translate("ProfilePage", "Profile Page"))

    def fetch_user_details(self):
        try:
            user_data = db.child("users").order_by_child("email").equal_to(self.user_email).get()
            for user in user_data.each():
                self.user_key = user.key()
                email = user.val().get("email")
                if email == self.user_email:
                    username = user.val().get("username")
                    phone = user.val().get("phone")
                    password = user.val().get("password")
                    displayed_password = '*' * len(password) if password else ''
                    self.name_input.setText(username)
                    self.phone_input.setText(phone)
                    self.email_input.setText(email)
                    self.password_input.setText(displayed_password)
                    break
        except Exception as e:
            print("Error fetching user details:", e)

    def update_user_data(self):
        try:
            username = self.name_input.text()
            phone = self.phone_input.text()
            password = self.password_input.text()

            if self.user_key:
                db.child("users").child(self.user_key).update({
                    "username": username,
                    "phone": phone,
                    "password": password
                })
                print("User data updated successfully.")
            else:
                print("User key not found. Cannot update user data.")
        except Exception as e:
            print("Error updating user data:", e)

    def open_find_doctor_page(self):
        try:
            user_email = self.user_email
            print(f"Opening finddoctor.py for user with email: {user_email}")

            user = auth.current_user
            if not user:
                print("User is not authenticated. Performing logout.")
                self.logout_user()
                return

            self.ProfilePage.hide()

            python_executable = "C:/BobHealthCentre/.venv/Scripts/python.exe"
            script_path = "C:/BobHealthCentre/.venv/finddoctor.py"

            subprocess.call([python_executable, script_path, user_email])
            QtWidgets.qApp.quit()
        except Exception as e:
            print(f"Exception occurred while opening finddoctor.py: {e}")

    def logout_user(self):
        try:
            firebase.auth().sign_out()
            print("User logged out.")
        except Exception as e:
            print("Error logging out user:", e)

    def menu_clicked(self, menu_name):
        print("Menu clicked:", menu_name)

    def open_find_doctor(self):
        try:
            # Call finddoctor.py and pass the user details as arguments
            subprocess.Popen([sys.executable, "finddoctor.py", self.user_id, self.token, self.user_email])
        except Exception as e:
            print(f"Error opening Find Doctor page: {e}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ProfilePage = QtWidgets.QMainWindow()
    ui = Ui_ProfilePage("user_id", "token", "user_email")
    ui.setupUi(ProfilePage)

    ProfilePage.setStyleSheet("QLabel { background-color: #355E3B; color: white; }"
                              "QLineEdit { border: 3px solid black; font: bold 12px; }"
                              "QPushButton { background-color: #088F8F; color: white; font: bold 14px; }"
                              "QPushButton:hover { background-color: #355E3B; }")

    ProfilePage.show()
    sys.exit(app.exec_())

