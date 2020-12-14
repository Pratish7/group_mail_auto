from tkinter import Tk, Frame, Label, Entry, GROOVE, Text, Button, ttk, CENTER

root = Tk()

main_frame_0 = Frame(root)

login_frame = Frame(main_frame_0, relief=GROOVE, border=1)      #login frame

email_label = Label(login_frame, text='email')
email_label.grid(row=0, column=0, sticky='W')

email_entry = Entry(login_frame)
email_entry.grid(row=1, column=0)

pass_label = Label(login_frame, text='password')
pass_label.grid(row=0, column=1, sticky='W')

pass_entry = Entry(login_frame)
pass_entry.grid(row=1, column=1)

login_frame.grid(row=0, column=0)


body_frame = Frame(main_frame_0, relief=GROOVE, border=1)        #body frame

subject_label = Label(body_frame, text='Subject')
subject_label.grid(row=0, column=0, sticky='N')

subject_entry = Entry(body_frame)
subject_entry.grid(row=0, column=1, sticky='nesw')

mail_label = Label(body_frame, text='Mail body')
mail_label.grid(row=1, column=0)

mail_entry = Text(body_frame, height=30)
mail_entry.grid(row=1, column=1)

body_frame.grid(row=1, column=0)

btn_frame = Frame(main_frame_0)                                #button frame

btn_send = Button(btn_frame, text='Send')
btn_send.grid(row=0, column=0, columnspan=3, sticky='nesw')

btn_reset_login = Button(btn_frame, text='Reset Login')
btn_reset_login.grid(row=1, column=0)

btn_reset_body = Button(btn_frame, text='Reset Body')
btn_reset_body.grid(row=1, column=1)

btn_rest_all = Button(btn_frame, text='Reset All')
btn_rest_all.grid(row=1, column=2)

btn_frame.grid(row=2, column=0)

main_frame_0.grid(row=0, column=0)


mailers_frame = Frame(root)

table = ttk.Treeview(mailers_frame)
table['show'] = 'headings'
table["columns"] = ("Mail", "Name")
table.column("Mail", stretch=False, width=90, anchor=CENTER)
table.column("Name", stretch=False, width=150, anchor=CENTER)
table.grid(column=0, row=0, rowspan=1)

mailers_frame.grid(row=0, column=1, sticky='nsew')

root.mainloop()