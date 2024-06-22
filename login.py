from PyQt5 import QtCore, QtGui, QtWidgets
import pyrebase
from profilepage import Ui_ProfilePage

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
        Form.resize(955, 672)
        font = QtGui.QFont()
        font.setBold(False)
        Form.setFont(font)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, -10, 971, 691))
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
        self.lineEdit.setGeometry(QtCore.QRect(190, 160, 611, 81))
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
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 270, 611, 81))
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
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.b1 = QtWidgets.QPushButton(self.widget)
        self.b1.setGeometry(QtCore.QRect(400, 380, 201, 61))
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
        self.label.setGeometry(QtCore.QRect(450, 50, 101, 81))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(77)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(440, 470, 131, 41))
        self.label_2.setStyleSheet("color:rgb(255,191,16)")
        self.label_2.setObjectName("label_2")
        self.b2 = QtWidgets.QPushButton(self.widget)
        self.b2.setGeometry(QtCore.QRect(400, 510, 201, 61))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
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
        self.b3 = QtWidgets.QPushButton(self.widget)
        self.b3.setGeometry(QtCore.QRect(400, 580, 201, 61))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        self.b3.setFont(font)
        self.b3.setStyleSheet("QPushButton#b3{\n"
                              "background-color:rgb(255,191,16);\n"
                              "color:rgb(135,60,0);\n"
                              "border-radius:5px;\n"
                              "}\n"
                              "\n"
                              "QPushButton#b3:pressed{\n"
                              "background-color:rgb(255,255,16);\n"
                              "}\n"
                              "")
        self.b3.setObjectName("b3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.b1.clicked.connect(self.login)  # Connect login button to login function

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Enter your email"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Enter Password"))
        self.b1.setText(_translate("Form", "L O G I  N"))
        self.label.setText(_translate("Form", "⚿"))
        self.label_2.setText(_translate("Form", "New User Sign Up!!!"))
        self.b2.setText(_translate("Form", "R e g i s t e r     N o w"))
        self.b3.setText(_translate("Form", "D o c t o r"))

    def login(self):
        email = self.lineEdit.text()
        password = self.lineEdit_2.text()

        try:
            user = auth.sign_in_with_email_and_password(email, password)
            print("Successfully logged in:", user['localId'])
            # Open the profile page and pass user token
            self.open_profile_page(user['idToken'], email)  # Pass user email here
        except Exception as e:
            print("Login failed:", e)

    def open_profile_page(self, token, user_email):
        try:
            # Create an instance of QtWidgets.QMainWindow
            self.profile_page = QtWidgets.QMainWindow()
            # Set the window title
            self.profile_page.setWindowTitle("Profile Page")
            # Create an instance of the UI layout
            ui = Ui_ProfilePage()
            # Setup the UI on the main window
            ui.setupUi(self.profile_page, user_email)  # Pass user email
            # Show the profile page
            self.profile_page.show()
        except Exception as e:
            print("Error opening profile page:", e)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())