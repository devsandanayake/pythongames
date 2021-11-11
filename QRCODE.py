from os import close
from tkinter import *
from tkinter import font
import qrcode
from tkinter import messagebox
from PIL import Image ,ImageTk

#create gui
win = Tk()
win.geometry("450x450")
win.title("QR Generator")
win.configure(bg="#AAFF22")
#entery box
entery = Entry(win,width=40,font=("times",20,"italic"))
entery.pack(padx=5,pady=5)

entery1 = Entry(win,width=25,font=("times",10,"bold"))
entery1.pack(padx=10,pady=15)


#qr code gen
def qr():
    data = entery.get()
    save = entery1.get()
    img = qrcode.make(data)
    img.save(save)
    #picture inster
    img =ImageTk.PhotoImage(Image.open(save))
    lable  =  Label(win,image=img,bg="#AAFF22").pack(padx=10,pady=10)
    #massage box
    messagebox.showinfo('QRcode Generator', f'succsseful' )
    

    
#button
btn = Button(win,text="Genarate",font=("Times",15,"bold italic"),width=20,command=qr).pack()


win.mainloop()