from tkinter import Tk, Frame, Label, Entry, GROOVE, Text, Button, ttk, CENTER, END, filedialog, messagebox
import csv
from mail import mail

csv_list=[]

def clear_login():
    email_addr_entry.delete(0, END)
    pass_entry.delete(0, END)
    name_entry.delete(0, END)

def clear_body():
    subject_entry.delete(0, END)
    mail_entry.delete(1.0, END)
    sendto_entry.delete(0, END)

def clear_all():
    email_addr_entry.delete(0, END)
    pass_entry.delete(0, END)
    name_entry.delete(0, END)
    subject_entry.delete(0, END)
    mail_entry.delete(1.0, END)
    sendto_entry.delete(0, END)

def load_csv():
    csv_list.clear()
    file = filedialog.askopenfilename()
    with open(file) as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            csv_list.append(row['email'])
            table.insert('',0, values=(row['email'], row['name']))

    sendto_entry.insert(0, 'CSV loaded')
    sendto_entry.config(state='disabled')

def load_mailers():
    if len(email_addr_entry.get())==0 or '@' not in (email_addr_entry.get()) or (len(email_addr_entry.get()))<5:
        messagebox.showerror('Error', 'Invalid email address')
        return

    if len(pass_entry.get())==0:
        messagebox.showerror('Error', 'Please enter password')
        return

    # if len(name_entry.get())==0:
    #     messagebox.showerror('Error', 'Please enter your name')
    #     return

    if sendto_entry.cget('state') == 'disabled':
        pass
    elif len(sendto_entry.get())==0 or '@' not in (sendto_entry.get()) or (len(sendto_entry.get()))<5:
        messagebox.showerror('Error', 'Invalid reciever\'s mail address')
        return

    if len(subject_entry.get())==0:
        messagebox.showerror('Error', 'Empty subject')
        return

    if len(mail_entry.get('1.0', END))==1:
        messagebox.showerror('Error', 'Empty mail body')
        return

    if len(csv_list)>0:
        mailers_list = csv_list
    else:
        mailers_list =  sendto_entry.get().split(';')

    mail(email_addr_entry.get(), pass_entry.get(), email_addr_entry.get(), subject_entry.get(), mail_entry.get(1.0, END), mailers_list)    

def show_pass():
    if pass_entry.cget('show') == '*':
        pass_entry.config(show='')
        show_pass_btn.config(text='Hide')
    elif pass_entry.cget('show') == '':
        pass_entry.config(show='*')
        show_pass_btn.config(text='Show')
    

root = Tk()
root.title('Bulk Mailer')

main_frame_0 = Frame(root)

login_frame = Frame(main_frame_0, relief=GROOVE, border=1)      #login frame

email_addr_label = Label(login_frame, text='Email')
email_addr_label.grid(row=0, column=0, sticky='W')

email_addr_entry = Entry(login_frame)
email_addr_entry.grid(row=1, column=0, sticky='W')

pass_label = Label(login_frame, text='Password')
pass_label.grid(row=0, column=1, sticky='W')

pass_entry = Entry(login_frame, show="*")
pass_entry.grid(row=1, column=1, sticky='W')

show_pass_btn = Button(login_frame, text='show', command=show_pass, width=2)
show_pass_btn.grid(row=1, column=2)

name_label = Label(login_frame, text='Your name (will be shown in "From" in the mail)')
# name_label.grid(row=0, column=3, sticky='W')

name_entry = Entry(login_frame)
#name_entry.grid(row=1, column=3, sticky='WE')

login_frame.grid(row=0, column=0, sticky='WE')


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

btn_send = Button(btn_frame, text='Send', command=load_mailers)
btn_send.grid(row=0, column=0, columnspan=3, sticky='nesw')

btn_reset_login = Button(btn_frame, text='Reset Login', command=clear_login)
btn_reset_login.grid(row=1, column=0)

btn_reset_body = Button(btn_frame, text='Reset Body', command=clear_body)
btn_reset_body.grid(row=1, column=1)

btn_rest_all = Button(btn_frame, text='Reset All', command=clear_all)
btn_rest_all.grid(row=1, column=2)

btn_frame.grid(row=2, column=0)

main_frame_0.grid(row=0, column=0)


mailers_frame = Frame(root, relief=GROOVE, border=2)         #table frame

table = ttk.Treeview(mailers_frame)
table['show'] = 'headings'
table["columns"] = ("Mail", "Name")
table.column("Mail", stretch=False, width=300, anchor=CENTER)
table.column("Name", stretch=False, width=250, anchor=CENTER)
table.heading('Mail', text='Mail')
table.heading('Name', text='Name')
table.pack(expand=True, fill='both')

mailers_frame.grid(row=0, column=1, sticky='NS')

root.mainloop()