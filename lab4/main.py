from tkinter import * 
from tkinter import filedialog as fd
from smtp import mail

def openfile():
    
    filetypes = (('text files', '*.txt'), ('All files', '*.*'))

    filenames = fd.askopenfilenames(title='Open files', initialdir='/', filetypes=filetypes)
    if filenames:
        tbFile.delete(0, END)
        tbFile.insert(0, filenames[0])
    
def btnclick():
    host =  tbHost.get()
    port =  tbPort.get()

    from_addr = tbFromAddr.get()
    passwd = tbPasswd.get()
    to_addr = tbToAddr.get()

    subj = tbSubj.get()
    message = tbMessage.get()

    file = tbFile.get()

    session = mail(host, int(port))
    session.connect(from_addr, passwd)
    session.send_message(to_addr, subj, message, file)
    session.disconnect()

form = Tk()  
form.title("SMTP")  
# form.geometry('400x250')  

lbHost = Label(form, text="Host:")
lbPort = Label(form, text="Port:")
lbFromAddr = Label(form, text="From addres:")
lbPasswd = Label(form, text="Password:")
lbToAddr = Label(form, text="To addfer:")
lbSubj = Label(form, text="Subject:")  
lbMessage = Label(form, text="Message:") 
lbFile = Label(form, text="File:") 

tbHost = Entry(form, width=50)
tbPort = Entry(form, width=50)
tbFromAddr = Entry(form, width=50)
tbPasswd = Entry(form, show='*', width=50)
tbToAddr = Entry(form, width=50)
tbSubj = Entry(form, width=50)
tbMessage = Entry(form, width=50)
tbFile = Entry(form, width=50) 

btnFile = Button(form, text="OpenFile", command=openfile)
btnRun = Button(form, text="Send", command=btnclick)
btnQuit = Button(form, text="Exit", command=form.destroy)  

lbHost.grid(column=0, row=0)
lbPort.grid(column=0, row=1)
lbFromAddr.grid(column=0, row=2)
lbPasswd.grid(column=0, row=3)
lbToAddr.grid(column=0, row=4)
lbSubj.grid(column=0, row=5)
lbMessage.grid(column=0, row=6)
lbFile.grid(column=0, row=7)

tbHost.grid(column=1, row=0)
tbPort.grid(column=1, row=1)
tbFromAddr.grid(column=1, row=2)
tbPasswd.grid(column=1, row=3)
tbToAddr.grid(column=1, row=4)
tbSubj.grid(column=1, row=5)
tbMessage.grid(column=1, row=6)
tbFile.grid(column=1, row=7)

btnFile.grid(column=0, row=8)
btnRun.grid(column=0, row=9)
btnQuit.grid(column=1, row=9)

tbHost.insert(0, "smtp.yandex.ru")
tbPort.insert(0, "587")
tbFromAddr.insert(0, "medovdennis@yandex.ru")
tbPasswd.insert(0, "**********") # пароль от почты
tbToAddr.insert(0, "medovdennis@yandex.ru")
tbFile.insert(0, "file.txt")
form.mainloop()