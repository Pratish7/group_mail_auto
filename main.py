from tkinter import Tk, Frame, Label, Entry, GROOVE, Text, Button

root = Tk()

login_frame = Frame(root, relief=GROOVE, border=1)      #login frame

email_label = Label(login_frame, text='email')
email_label.grid(row=0, column=0, sticky='W')

email_entry = Entry(login_frame)
email_entry.grid(row=1, column=0)

pass_label = Label(login_frame, text='password')
pass_label.grid(row=0, column=1, sticky='W')

pass_entry = Entry(login_frame)
pass_entry.grid(row=1, column=1)

login_frame.grid(row=0, column=0)


body_frame = Frame(root, relief=GROOVE, border=1)        #body frame

subject_label = Label(body_frame, text='Subject')
subject_label.grid(row=0, column=0, sticky='N')

subject_entry = Entry(body_frame)
subject_entry.grid(row=0, column=1)

mail_label = Label(body_frame, text='Mail body')
mail_label.grid(row=1, column=0)

mail_entry = Text(body_frame, height=30)
mail_entry.grid(row=1, column=1)

body_frame.grid(row=1, column=0)

btn_frame = Frame(root)                                #button frame

btn_send = Button(btn_frame, text='Send')
btn_send.grid(row=0, column=0, columnspan=3, sticky='nesw')

btn_reset_login = Button(btn_frame, text='Reset Login')
btn_reset_login.grid(row=1, column=0)

btn_reset_body = Button(btn_frame, text='Reset Body')
btn_reset_body.grid(row=1, column=1)

btn_rest_all = Button(btn_frame, text='Reset All')
btn_rest_all.grid(row=1, column=2)

btn_frame.grid(row=2, column=0)

root.mainloop()