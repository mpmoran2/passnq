from tkinter import *
import bcrypt

def validate(password):
    hash = b'$2b$12$/WkkiDJjryEIzA62IrKc.u9M6Rtm3q5ccqHB5t.S6Rrx155gCL/cC'
    password = bytes(password, encoding='utf-8')
    if bcrypt.checkpw(password, hash):
        print('Thank you, login successful. Sheepy granted access.')
    else:
        print('We are sorry, access denied.')

root = Tk()

root.geometry("250x75")

label = Label(root,text="Please enter password")
label.pack()
userpass = Entry(root)
userpass.pack()


button = Button(text="Validate",command=lambda:validate(userpass.get()))
button.pack()

root.mainloop()