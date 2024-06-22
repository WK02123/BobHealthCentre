
import pyrebase
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

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
        Form.resize(968, 640)
        Form.setStyleSheet("")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 971, 800))
        self.widget.setStyleSheet("background-color:rgb(88, 161, 255);")
        self.widget.setObjectName("widget")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setGeometry(QtCore.QRect(270, 330, 421, 61))
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
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.b2 = QtWidgets.QPushButton(self.widget)
        self.b2.setGeometry(QtCore.QRect(390, 570, 161, 41))
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
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 250, 421, 61))
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
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 170, 421, 61))
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

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(450, 20, 101, 81))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(66)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(270, 90, 421, 61))
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

        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_5.setGeometry(QtCore.QRect(270, 410, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color:rgba(47,49,52,200);\n"
                                      "color:rgb(255,255,255);\n"
                                      "border-radius:2px;\n"
                                      "padding-left:10px;\n"
                                      "border:1px solid rgba(0,0,0,0);\n"
                                      "border-bottom-color:rgba(46,82,101,255);\n"
                                      "padding-bottom:3px;")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_5.setObjectName("lineEdit_5")

        # Add a ComboBox for selecting the clinic
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(270, 490, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color:rgba(47,49,52,200);\n"
                                    "color:rgb(255,255,255);\n"
                                    "border-radius:2px;\n"
                                    "padding-left:10px;\n"
                                    "border:1px solid rgba(0,0,0,0);\n"
                                    "border-bottom-color:rgba(46,82,101,255);\n"
                                    "padding-bottom:3px;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Select Clinic")
        self.comboBox.addItem("Clinic1")
        self.comboBox.addItem("Clinic2")

        self.b4 = QtWidgets.QPushButton(self.widget)
        self.b4.setGeometry(QtCore.QRect(390, 630, 161, 41))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setBold(True)
        self.b4.setFont(font)
        self.b4.setStyleSheet("QPushButton#b4{\n"
                              "background-color:rgb(255,191,16);\n"
                              "color:rgb(135,60,0);\n"
                              "border-radius:5px;\n"
                              "}\n"
                              "\n"
                              "QPushButton#b4:pressed{\n"
                              "background-color:rgb(255,255,16);\n"
                              "}\n"
                              "")
        self.b4.setObjectName("b4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Connect the register button to the registration function
        self.b2.clicked.connect(self.register)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Language"))
        self.b2.setText(_translate("Form", "R E G I S T E R"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Specialty"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Enter Password"))
        self.label.setText(_translate("Form", "🧑‍🧒"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Enter Username"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "Email"))
        self.b4.setText(_translate("Form", "L O G I N"))

    def register(self):
        username = self.lineEdit.text().strip()
        password = self.lineEdit_2.text()
        specialty = self.lineEdit_3.text().strip()
        language = self.lineEdit_4.text().strip()
        email = self.lineEdit_5.text().strip()
        clinic = self.comboBox.currentText().strip()

        # Basic validation
        if not (email and password and specialty and language and username and clinic != "Select Clinic"):
            self.show_message("Please fill in all fields.")
            return

        try:
            # Create user with email and password (you may adjust this according to your Firebase authentication method)
            user = auth.create_user_with_email_and_password(email, password)

            # If successful, store additional doctor details in the database
            doctor_data = {
                "email": email,
                "username": username,
                "specialty": specialty,
                "language": language,
                "clinic": clinic,
                "role": "2"
            }

            # Push user data to Firebase Realtime Database under "doctors" path
            db.child("doctors").child(user['localId']).set(doctor_data)

            # Show success message
            self.show_success_message()

        except Exception as e:
            error_message = str(e)
            self.show_message(error_message)

    def show_success_message(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Registration Successful!")
        msg.setWindowTitle("Success")
        msg.exec_()

    def show_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)

    Form.show()
    sys.exit(app.exec_())
message.txt
11
KB