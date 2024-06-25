from PyQt5 import QtCore, QtGui, QtWidgets
from login import Ui_Form as HomepageUi_form    # Import your login window

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1102, 777)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 1131, 811))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setBold(False)
        self.widget_2.setFont(font)
        self.widget_2.setStyleSheet("background-color: rgb(208, 253, 255);\n"
                                    "border-radius:20px;")
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setGeometry(QtCore.QRect(-20, 0, 1151, 131))
        self.widget_3.setStyleSheet("background-image: url(:/newPrefix/360_F_120571823_uUoCUfnSuxzEgOPj6FQ1nxCHNAw562Fq 2.jpg);")
        self.widget_3.setObjectName("widget_3")
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setGeometry(QtCore.QRect(20, 200, 1081, 581))
        self.widget_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_4.setObjectName("widget_4")
        self.widget = QtWidgets.QWidget(self.widget_4)
        self.widget.setGeometry(QtCore.QRect(640, 300, 281, 231))
        self.widget.setStyleSheet("background-image: url(:/newPrefix/health-care-landing-page-vector-template-diagnostics-clinic-hospital-website-homepage-ui-layout-with-isometric-illustration-healthcare-industry-medical-service-web-banner-webpage-3d-concept-2c7rrjy 2.jpg);")
        self.widget.setObjectName("widget")
        self.textEdit_3 = QtWidgets.QTextEdit(self.widget_4)
        self.textEdit_3.setGeometry(QtCore.QRect(90, 250, 361, 61))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit = QtWidgets.QTextEdit(self.widget_4)
        self.textEdit.setGeometry(QtCore.QRect(30, 320, 101, 231))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_4 = QtWidgets.QTextEdit(self.widget_4)
        self.textEdit_4.setGeometry(QtCore.QRect(200, 320, 141, 181))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self.widget_4)
        self.textEdit_5.setGeometry(QtCore.QRect(410, 320, 111, 181))
        self.textEdit_5.setObjectName("textEdit_5")
        self.widget_5 = QtWidgets.QWidget(self.widget_4)
        self.widget_5.setGeometry(QtCore.QRect(630, 90, 281, 191))
        self.widget_5.setStyleSheet("background-image: url(:/newPrefix/images-2.jpeg);")
        self.widget_5.setObjectName("widget_5")
        self.textEdit_6 = QtWidgets.QTextEdit(self.widget_4)
        self.textEdit_6.setGeometry(QtCore.QRect(120, 30, 321, 51))
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_7 = QtWidgets.QTextEdit(self.widget_4)
        self.textEdit_7.setGeometry(QtCore.QRect(20, 110, 561, 131))
        self.textEdit_7.setObjectName("textEdit_7")
        self.b4 = QtWidgets.QPushButton(self.widget_2)
        self.b4.setGeometry(QtCore.QRect(920, 150, 141, 41))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
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
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget_2)
        self.textEdit_2.setGeometry(QtCore.QRect(380, 140, 361, 61))
        self.textEdit_2.setObjectName("textEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Connect the Sign Up button to open login page
        self.b4.clicked.connect(self.open_login_page)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textEdit_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "hr { height: 1px; border-width: 0; }\n"
                                              "li.unchecked::marker { content: \"\\2610\"; }\n"
                                              "li.checked::marker { content: \"\\2612\"; }\n"
                                              "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:700; text-decoration: underline; color:#b2cdf9;\">Health Care</span></p></body></html>"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "hr { height: 1px; border-width: 0; }\n"
                                          "li.unchecked::marker { content: \"\\2610\"; }\n"
                                          "li.checked::marker { content: \"\\2612\"; }\n"
                                          "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">We always Put Our Patients First We treat patients from all walks of life, with quality and affordable treatment options for everyone</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "hr { height: 1px; border-width: 0; }\n"
                                        "li.unchecked::marker { content: \"\\2610\"; }\n"
                                        "li.checked::marker { content: \"\\2612\"; }\n"
                                        "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Our doctors have been practicing medicine for over 10 years, with vast knowledge and experience in dermatology, ophthalmology, gynaecology, and aesthetic medicine.</span></p></body></html>"))
        self.textEdit_5.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "hr { height: 1px; border-width: 0; }\n"
                                        "li.unchecked::marker { content: \"\\2610\"; }\n"
                                        "li.checked::marker { content: \"\\2612\"; }\n"
                                        "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Dr. A Clinic has all sort of health plans and payment methods available. Talk to our friendly consultants for more information!</span></p></body></html>"))
        self.textEdit_6.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "hr { height: 1px; border-width: 0; }\n"
                                        "li.unchecked::marker { content: \"\\2610\"; }\n"
                                        "li.checked::marker { content: \"\\2612\"; }\n"
                                        "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:700; color:#000000;\">WELCOME</span></p></body></html>"))
        self.textEdit_7.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "hr { height: 1px; border-width: 0; }\n"
                                        "li.unchecked::marker { content: \"\\2610\"; }\n"
                                        "li.checked::marker { content: \"\\2612\"; }\n"
                                        "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'VisbyCf\',\'sans-serif\'; font-size:16px; font-weight:700; color:#008080; background-color:#ffffff;\">A Klinik Signature is an Aesthetic Clinic in Penang.</span></p>\n"
                                        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'VisbyCf\',\'sans-serif\'; font-size:16px; font-weight:700; color:#008080; background-color:#ffffff;\">We offer a range of aesthetic services to help you achieve your desired look.</span></p>\n"
                                        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'VisbyCf\',\'sans-serif\'; font-size:16px; font-weight:700; color:#008080; background-color:#ffffff;\">Our clinic provides aesthetic services to help improve your skin and enhance your appearance</span></p>\n"
                                        "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:700;\"><br /></p></body></html>"))
        self.b4.setText(_translate("Form", "Sign Up"))
        self.textEdit_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "hr { height: 1px; border-width: 0; }\n"
                                        "li.unchecked::marker { content: \"\\2610\"; }\n"
                                        "li.checked::marker { content: \"\\2612\"; }\n"
                                        "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:700; font-style:italic; text-decoration: underline;\">BobHealthCentre</span></p></body></html>"))
import pic3_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
