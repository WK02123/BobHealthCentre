import tkinter as tk

class Ui_MainWindow:
    def __init__(self, MainWindow):
        MainWindow.title("MainWindow")
        MainWindow.geometry("1120x827")
        MainWindow.configure(bg="#D0FDFF")

        self.centralwidget = tk.Frame(MainWindow, bg="#D0FDFF")
        self.centralwidget.pack(fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.centralwidget)
        self.label.place(x=0, y=0, width=1121, height=151)
        self.label_img = tk.PhotoImage(file="hearder.png")
        self.label.configure(image=self.label_img)

        self.b4 = tk.Button(self.centralwidget, text="BACK", font=("Arial", 12, "bold"), bg="#FFBF10", fg="#873C00", relief=tk.RAISED, bd=0)
        self.b4.place(x=10, y=170, width=131, height=41)

        self.label_2 = tk.Label(self.centralwidget, bg="white")
        self.label_2.place(x=330, y=160, width=451, height=631)

        self.textEdit_6 = tk.Text(self.centralwidget, bg="white", font=("MS Shell Dlg 2", 12), wrap=tk.WORD)
        self.textEdit_6.place(x=350, y=460, width=391, height=41)
        self.textEdit_6.insert(tk.END, "Time:")

        self.lineEdit = tk.Entry(self.centralwidget, bg="white", font=("MS Shell Dlg 2", 12))
        self.lineEdit.place(x=350, y=260, width=391, height=51)
        self.lineEdit.insert(tk.END, "Name:")

        self.lineEdit_2 = tk.Entry(self.centralwidget, bg="white", font=("MS Shell Dlg 2", 12))
        self.lineEdit_2.place(x=350, y=320, width=391, height=51)
        self.lineEdit_2.insert(tk.END, "Clinic:")

        self.lineEdit_3 = tk.Entry(self.centralwidget, bg="white", font=("MS Shell Dlg 2", 12))
        self.lineEdit_3.place(x=350, y=380, width=391, height=51)
        self.lineEdit_3.insert(tk.END, "Doctor:")

        self.textEdit = tk.Text(self.centralwidget, bg="white", font=("MS Shell Dlg 2", 14), wrap=tk.WORD)
        self.textEdit.place(x=400, y=180, width=311, height=41)
        self.textEdit.insert(tk.END, "Confirmation Page")

        self.textEdit_5 = tk.Text(self.centralwidget, bg="white", font=("MS Shell Dlg 2", 12), wrap=tk.WORD)
        self.textEdit_5.place(x=350, y=530, width=381, height=41)
        self.textEdit_5.insert("1.0", "Description:")
        self.lineEdit_4 = tk.Entry(self.centralwidget, bg="white", font=("MS Shell Dlg 2", 8))
        self.lineEdit_4.place(x=350, y=570, width=381, height=131)

        self.b5 = tk.Button(self.centralwidget, text="CONFIRM", font=("Arial", 12, "bold"), bg="#FFAA00", fg="#873C00",
                            relief=tk.RAISED, bd=0)
        self.b5.place(x=500, y=730, width=131, height=41)
        self.statusbar = tk.Label(MainWindow, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.statusbar.pack(side=tk.BOTTOM, fill=tk.X)

        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        pass  # Translation of text would go here

if __name__ == "__main__":
    root = tk.Tk()
    ui = Ui_MainWindow(root)
    root.mainloop()
