import sys
import PySide6.Qtwidgets as Qtwidgets
from PySide6.Qtwidgets import QDialog, QApplication, QMessagebox
from PySide6.uic import loadUi
import mysql.connector as con

class LoginApp(QDialog):
	def __init__(self):
		super(LoginApp,self).__init__()
		loadUi("Login_form.ui",self)

class RegApp(QDialog):
	def __init__(self):
		super(RegApp,self).__init__()
		loadUi("Register.ui",self)

app = QApplication(sys.argv)
widget = Qtwidgets.QstackedWidget()

loginform = LoginApp()
registrationform = RegApp()
widget.addwidget(loginform)
widget.addwidget(registrationform)
widget.setCurrentIndex(1)
widget.show()

app.exec_()


