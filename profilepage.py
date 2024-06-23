import sys
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
db = firebase.database()

class Ui_ProfilePage(object):
    def setupUi(self, ProfilePage, user_email):
        self.user_email = user_email
        self.user_key = None  # Initialize user key
        ProfilePage.setObjectName("ProfilePage")
        ProfilePage.resize(1127, 868)

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
        self.menu_button2.clicked.connect(partial(self.menu_clicked, "Find Doctor"))  # Changed signal handler parameter

        self.logout_button = QtWidgets.QPushButton(self.centralwidget)
        self.logout_button.setGeometry(QtCore.QRect(1000,80, 100, 30))  # Adjust the position as needed
        self.logout_button.setText("Logout")
        self.logout_button.clicked.connect(self.menu_clicked)  # Connect the button click signal

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
        self.email_input.setReadOnly(True)  # Email cannot be edited

        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(20, 530, 301, 41))
        self.password_label.setText("Password:")
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(20, 580, 1081, 51))
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)  # Mask the input for password

        # Submit Button
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(500, 650, 121, 41))
        self.submit_button.setText("Submit")
        self.submit_button.clicked.connect(self.update_user_data)  # Connect the button click signal

        ProfilePage.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProfilePage)
        QtCore.QMetaObject.connectSlotsByName(ProfilePage)

        # Fetch user details from the database and populate the fields
        self.fetch_user_details()

    def retranslateUi(self, ProfilePage):
        _translate = QtCore.QCoreApplication.translate
        ProfilePage.setWindowTitle(_translate("ProfilePage", "Profile Page"))

    def fetch_user_details(self):
        try:
            user_data = db.child("users").order_by_child("email").equal_to(self.user_email).get()
            for user in user_data.each():
                self.user_key = user.key()  # Store user key
                email = user.val().get("email")
                if email == self.user_email:
                    username = user.val().get("username")
                    phone = user.val().get("phone")
                    password = user.val().get("password")  # Assuming password is stored in the database
                    # Assuming the password is hashed and needs to be displayed as asterisks
                    displayed_password = '*' * len(password) if password else ''  # Masking the password
                    self.name_input.setText(username)
                    self.phone_input.setText(phone)
                    self.email_input.setText(email)
                    self.password_input.setText(displayed_password)  # Displayed masked password
                    break  # Stop iteration after finding the correct user
        except Exception as e:
            print("Error fetching user details:", e)

    def update_user_data(self):
        try:
            # Get the updated values from the input fields
            username = self.name_input.text()
            phone = self.phone_input.text()
            password = self.password_input.text()  # Assuming you allow the user to change the password

            if self.user_key:
                # Update the user's data in the database
                db.child("users").child(self.user_key).update({
                    "username": username,
                    "phone": phone,
                    "password": password  # Update the password as well if allowed
                })
                print("User data updated successfully.")
            else:
                print("User key not found. Cannot update user data.")
        except Exception as e:
            print("Error updating user data:", e)

    def menu_clicked(self, menu_name):
        print("Menu clicked:", menu_name)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ProfilePage = QtWidgets.QMainWindow()
    ui = Ui_ProfilePage()
    ui.setupUi(ProfilePage, "user@example.com")  # Pass the user's email as an argument

    # Apply custom styles
    ProfilePage.setStyleSheet("QLabel { background-color: #355E3B; color: white; }"
                              "QLineEdit { border: 3px solid black; font: bold 12px; }"
                              "QPushButton { background-color: #088F8F; color: white; font: bold 14px; }"
                              "QPushButton:hover { background-color: #355E3B; }")

    ProfilePage.show()
    sys.exit(app.exec_())
