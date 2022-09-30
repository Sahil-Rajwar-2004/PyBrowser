import sys
from tkinter import *
import time
from tkinter import messagebox as msg
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction("Back",self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        next_btn = QAction("Forward",self)
        next_btn.triggered.connect(self.browser.forward)
        navbar.addAction(next_btn)

        refresh_btn = QAction("Reload",self)
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_btn)

        home_btn = QAction("Home",self)
        home_btn.triggered.connect(self.go_home)
        navbar.addAction(home_btn)

        shortcuts_btn = QAction("Shortcuts",self)
        shortcuts_btn.triggered.connect(self.shortcuts)
        navbar.addAction(shortcuts_btn)

        about_btn = QAction("About",self)
        about_btn.triggered.connect(self.about)
        navbar.addAction(about_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.go_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def shortcuts(self):
        short = Tk()
        short.geometry("700x280")
        short.title("About")
        short.resizable(False,False)
        short.config(bg = "gray")

        def add():
            ask = str(main_entry2.get())
            file = open("shortcuts.txt","a")
            file.write(ask+"\n")
            msg.showinfo("Info","URL Added! make sure you entered the correct URL")
            file.close()

        def open_():
            ask = str(main_entry1.get())
            file = open("shortcuts.txt","r")
            a = file.readlines()
            for i in range(0,len(a)):
                x = a[i][:-2].split(".")
                if ask in x:
                    self.browser.setUrl(QUrl(str(a[i][:-2])))            
            file.close()

        main_frame = Frame(short)
        main_frame.pack(fill = BOTH,padx = 5,pady = 5)
        main_label1 = Label(main_frame,text = "Open: ",font = ("cascadia code",13))
        main_label1.grid(row = 0, column = 0,pady = 5, padx = 5)
        var1 = StringVar()
        main_entry1 = Entry(main_frame,textvariable=var1,font = ("cascadia code",13))
        main_entry1.grid(row=0,column=1,padx=5,pady=5)
        open_btn = Button(main_frame,text = "OK",command=open_,width=10)
        open_btn.grid(row=0,column=2,ipady=5,ipadx=5, padx=5,pady=5)

        main_label2 = Label(main_frame,text = "Add (full-url): ",font = ("cascadia code",13))
        main_label2.grid(row = 1, column = 0,pady = 5, padx = 5)
        var2 = StringVar()
        main_entry2 = Entry(main_frame,textvariable=var2,font = ("cascadia code",13))
        main_entry2.grid(row=1,column=1,padx=5,pady=5)
        add_btn = Button(main_frame,text = "OK",command=add,width=10)
        add_btn.grid(row=1,column=2,ipady=5,ipadx=5, padx=5,pady=5)

        short.mainloop()

    def go_home(self):
        self.browser.setUrl(QUrl("https://www.google.com"))

    def go_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self,q):
        self.url_bar.setText(q.toString())
        file = open("history.txt","a")
        file.write(q.toString()+" -> "+time.ctime()+"\n")
        file.close()

    def about(self):
        win = Tk()
        win.geometry("600x280")
        win.title("About")
        win.resizable(False,False)
        win.config(bg = "gray")

        text = """
Creator: Sahil Rajwar
Date: 13th September 2022
HomePage: https://github.com/Sahil-Rajwar-2004/PyBrowser
version: 13.09.2022
Contact: justsahilrajwar2004@gmail.com
Purpose: Web Browser
Software: Open Source"""

        main_frame = Frame(win)
        main_frame.pack(padx = 5,pady = 5)

        def Quit():
            win.destroy()

        main_text = Text(main_frame, bg = "white", font = ("cascadia code",13),height = 10)
        main_text.insert(END,text)
        main_text.pack(fill = BOTH, padx = 5,pady = 5)
        main_text.configure(state = DISABLED)

        btn = Button(main_frame,text = "Exit", font=("cascadia code",9,"bold"), command = Quit)
        btn.pack(anchor=CENTER, ipadx = 5, ipady = 5, padx = 5, pady = 5)        

        win.mainloop()


app = QApplication(sys.argv)
QApplication.setApplicationName("PyBrowser")
window = MainWindow()

app.exec_()
