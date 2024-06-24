import pyrebase
from PyQt5 import QtCore, QtGui, QtWidgets
from login import Ui_Form as LoginUi_Form

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
auth = firebase.auth()
db = firebase.database()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1138, 696)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1171, 711))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setBold(False)
        self.widget.setFont(font)
        self.widget.setStyleSheet("\n"
                                  "background-color: rgb(88, 161, 255);\n"
                                  "border-radius:20px;")
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(350, 160, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(47,49,52,200);\n"
                                    "color:rgb(255,255,255);\n"
                                    "border-radius:2px;\n"
                                    "padding-left:10px;\n"
                                    "border:1px solid rgba(0,0,0,0);\n"
                                    "border-bottom-color:rgba(46,82,101,255);\n"
                                    "padding-bottom:3px;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 250, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(47,49,52,200);\n"
                                      "color:rgb(255,255,255);\n"
                                      "border-radius:2px;\n"
                                      "padding-left:10px;\n"
                                      "border:1px solid rgba(0,0,0,0);\n"
                                      "border-bottom-color:rgba(46,82,101,255);\n"
                                      "padding-bottom:3px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)  # Set echo mode to Password
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.b1 = QtWidgets.QPushButton(self.widget)
        self.b1.setGeometry(QtCore.QRect(470, 610, 161, 41))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setBold(True)
        self.b1.setFont(font)
        self.b1.setStyleSheet("QPushButton#b1{\n"
                              "background-color:rgb(255,191,16);\n"
                              "color:rgb(135,60,0);\n"
                              "border-radius:5px;\n"
                              "}\n"
                              "\n"
                              "QPushButton#b1:pressed{\n"
                              "background-color:rgb(255,255,16);\n"
                              "}\n"
                              "")
        self.b1.setObjectName("b1")

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(530, 50, 101, 81))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(66)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(470, 580, 161, 21))
        self.label_2.setStyleSheet("color:rgb(255,191,16)")
        self.label_2.setObjectName("label_2")

        self.b2 = QtWidgets.QPushButton(self.widget)
        self.b2.setGeometry(QtCore.QRect(470, 520, 161, 41))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setBold(True)
        self.b2.setFont(font)
        self.b2.setStyleSheet("QPushButton#b2{\n"
                              "background-color:rgb(255,191,16);\n"
                              "color:rgb(135,60,0);\n"
                              "border-radius:5px;\n"
                              "}\n"
                              "\n"
                              "QPushButton#b2:pressed{\n"
                              "background-color:rgb(255,255,16);\n"
                              "}\n"
                              "")
        self.b2.setObjectName("b2")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_3.setGeometry(QtCore.QRect(350, 340, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color:rgba(47,49,52,200);\n"
                                      "color:rgb(255,255,255);\n"
                                      "border-radius:2px;\n"
                                      "padding-left:10px;\n"
                                      "border:1px solid rgba(0,0,0,0);\n"
                                      "border-bottom-color:rgba(46,82,101,255);\n"
                                      "padding-bottom:3px;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setGeometry(QtCore.QRect(350, 430, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color:rgba(47,49,52,200);\n"
                                      "color:rgb(255,255,255);\n"
                                      "border-radius:2px;\n"
                                      "padding-left:10px;\n"
                                      "border:1px solid rgba(0,0,0,0);\n"
                                      "border-bottom-color:rgba(46,82,101,255);\n"
                                      "padding-bottom:3px;")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)  # Set echo mode to Password
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.register_button = QtWidgets.QPushButton(Form)
        self.register_button.setObjectName("register_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Connect the register button to the register function
        self.b2.clicked.connect(self.register_user)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Enter Username"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Enter Password"))
        self.b1.setText(_translate("Form", "L o g i n   "))
        self.label.setText(_translate("Form", "🧑‍🧒"))
        self.label_2.setText(_translate("Form", "Already Registered Login!!!!"))
        self.b2.setText(_translate("Form", "R E G I S T E R"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Enter Email"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Enter Phone Number"))

    def register_user(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        email = self.lineEdit_3.text()
        phone = self.lineEdit_4.text()

        try:
            # Register user with Firebase authentication
            user = auth.create_user_with_email_and_password(email, password)

            # Store additional user data in Firebase database
            data = {
                "username": username,
                "email": email,
                "phone": phone,
                "password": password,
                "role":"1"
            }
            db.child("users").child(user['localId']).set(data)

            # Show success message
            self.show_message_box("Registration Successful", f"Welcome, {username}!")
            # After successful registration, navigate to login page
            self.goto_login_page()
        except Exception as e:
            # Handle errors
            self.show_message_box("Error", str(e))

    def goto_login_page(self):
        # Create an instance of the login page
        self.login_page = QtWidgets.QWidget()
        self.login_ui = LoginUi_Form()
        self.login_ui.setupUi(self.login_page)
        self.login_page.show()
        # Close the current registration page
        Form.close()

    def show_message_box(self, title, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(title)
        msg.setInformativeText(message)
        msg.setWindowTitle("Status")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())