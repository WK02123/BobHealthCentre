from PyQt5 import QtWidgets
from Login_form import Ui_Form as Ui_Login_Form
from Register import Ui_Form as Ui_Register_Form
from Doctor_reg import Ui_Form as Ui_Doctor_Form



class FormController:
    def __init__(self):
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.ui_login = Ui_Login_Form()
        self.ui_register = Ui_Register_Form()
        self.ui_doctor = Ui_Doctor_Form()

        # Setup UI for each form
        self.ui_login.setupUi(self.stacked_widget)
        self.ui_register.setupUi(self.stacked_widget)
        self.ui_doctor.setupUi(self.stacked_widget)

        # Set fixed size for all forms (adjust as needed)
        self.ui_login.widget.setFixedSize(1000, 700)  # Example size
        self.ui_register.widget.setFixedSize(1000, 700)  # Example size
        self.ui_doctor.widget.setFixedSize(1000, 700)  # Example size

        # Add forms to stacked widget
        self.stacked_widget.addWidget(self.ui_login.widget)
        self.stacked_widget.addWidget(self.ui_register.widget)
        self.stacked_widget.addWidget(self.ui_doctor.widget)

        # Connect signals for navigation
        self.ui_login.b2.clicked.connect(self.show_register_form)
        self.ui_login.b3.clicked.connect(self.show_doctor_form)
        self.ui_register.b1.clicked.connect(self.show_login_form)
        self.ui_doctor.b4.clicked.connect(self.show_login_form)

    def show_login_form(self):
        self.stacked_widget.setCurrentWidget(self.ui_login.widget)

    def show_register_form(self):
        self.stacked_widget.setCurrentWidget(self.ui_register.widget)

    def show_doctor_form(self):
        self.stacked_widget.setCurrentWidget(self.ui_doctor.widget)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    controller = FormController()
    controller.show_login_form()
    controller.stacked_widget.show()  # Show the stacked widget containing all forms
    sys.exit(app.exec_())




