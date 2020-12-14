from tkinter import Tk, Frame, Label, Entry, GROOVE, Text, Button, ttk, CENTER, END, filedialog
import csv

def clear_login():
    email_entry.delete(0, END)
    pass_entry.delete(0, END)

def clear_body():
    subject_entry.delete(0, END)
    mail_entry.delete(1.0, END)
    sendto_entry.delete(0, END)

def clear_all():
    email_entry.delete(0, END)
    pass_entry.delete(0, END)
    subject_entry.delete(0, END)
    mail_entry.delete(1.0, END)
    sendto_entry.delete(0, END)

def load_csv():
    mailers_list = []
    file = filedialog.askopenfilename()
    with open(file) as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            mailers_list.append(row['email'])
            table.insert('',0, values=(row['email'], row['name']))
    

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

sendto_label = Label(body_frame, text='Send to')
sendto_label.grid(row=0, column=0, sticky='W')

sendto_entry = Entry(body_frame, width=30)
sendto_entry.grid(row=0, column=1, sticky='W')

load_csv_btn = Button(body_frame, text='Load CSV/XLSX', command=load_csv)
load_csv_btn.grid(row=0, column=1, sticky='E')

subject_label = Label(body_frame, text='Subject')
subject_label.grid(row=1, column=0, sticky='N')

subject_entry = Entry(body_frame)
subject_entry.grid(row=1, column=1, sticky='nesw')

mail_label = Label(body_frame, text='Mail body')
mail_label.grid(row=2, column=0)

mail_entry = Text(body_frame, height=30)
mail_entry.grid(row=2, column=1)

body_frame.grid(row=1, column=0)

btn_frame = Frame(main_frame_0)                                #button frame

btn_send = Button(btn_frame, text='Send')
btn_send.grid(row=0, column=0, columnspan=3, sticky='nesw')

btn_reset_login = Button(btn_frame, text='Reset Login', command=clear_login)
btn_reset_login.grid(row=1, column=0)

btn_reset_body = Button(btn_frame, text='Reset Body', command=clear_body)
btn_reset_body.grid(row=1, column=1)

btn_rest_all = Button(btn_frame, text='Reset All', command=clear_all)
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

mailers_frame.grid(row=0, column=1)

root.mainloop()