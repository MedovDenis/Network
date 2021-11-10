from tkinter import * 
from ftp_client import ftp

HOST = "91.222.128.11"
LOGIN = "testftp_guest"
PASSWR = "12345"

def btnclick():
    host = tbHost.get()
    login = tbLogin.get()
    passwd = tbPasswd.get()

    session = ftp(host)
    session.connect(login, passwd)

    lbResult["text"] =  "Size all file: {}b".format(session.size_all_file())

    lbxFile.delete(0, END)
    lbxPath.delete(0, END)

    for item in session.get_file():
        lbxFile.insert(0, "{} ({}b)".format(item["file"], item["size"]))

    for item in session.get_path():
        lbxPath.insert(0, item)

    session.disconect()

form = Tk()  
form.title("FTP")  
# form.geometry('400x250')  

lbHost = Label(form, text="Host")
lbLogin = Label(form, text="Login")
lbPasswd = Label(form, text="Password") 

tbHost = Entry(form)
tbLogin = Entry(form)
tbPasswd = Entry(form)

lbResult = Label(form)

lbPath = Label(form, text="Path")
lbFile = Label(form, text="File")

lbxPath = Listbox(form, width=20, height=30)
lbxFile = Listbox(form, width=45, height=30)

btnRun = Button(form, text="Start", command=btnclick)
btnQuit = Button(form, text="Exit", command=form.destroy)  

lbHost.grid(column=0, row=0)
lbLogin.grid(column=0, row=1)  
lbPasswd.grid(column=0, row=2)  

tbHost.grid(column=1, row=0)
tbLogin.grid(column=1, row=1)  
tbPasswd.grid(column=1, row=2)  

lbResult.grid(columnspan=2, column=0, row=3)

lbPath.grid(column=0, row=4)
lbFile.grid(columnspan=2, column=1, row=4)

lbxPath.grid(column=0, row=5)
lbxFile.grid(columnspan=2, column=1, row=5)  

btnRun.grid(column=0, row=6)
btnQuit.grid(column=1, row=6)

tbHost.insert(0, HOST)
tbLogin.insert(0, LOGIN)
tbPasswd.insert(0, PASSWR)

form.mainloop()

