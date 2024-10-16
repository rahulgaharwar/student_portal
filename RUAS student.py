from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector

def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('','end', values=i)

def search():
    q2= q.get()
    query = "SELECT * from students WHERE student_id LIKE '%"+q2+"%' OR name LIKE '%"+q2+"%' OR dob LIKE '%"+q2+"%' OR contact_number LIKE '%"+q2+"%' OR address LIKE '%"+q2+"%' OR gender LIKE '%"+q2+"%' OR branch_code LIKE '%"+q2+"%' OR result_status LIKE '%"+q2+"%' OR fee_status LIKE '%"+q2+"%' "
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)

def clear():
    query="SELECT * FROM students"
    cursor.execute(query)
    rows= cursor.fetchall()
    update(rows)

def getrow(event):
    rowid=trv.identify_row(event.y)
    item = trv.item(trv.focus())
    t1.set(item['values'][0])
    t2.set(item['values'][1])
    t3.set(item['values'][2])
    t4.set(item['values'][3])
    t5.set(item['values'][4])
    t6.set(item['values'][5])
    t7.set(item['values'][6])
    t8.set(item['values'][7])
    t9.set(item['values'][8])

def update_student():
    student_id = t1.get()
    name = t2.get()
    dob = t3.get()
    contact_number = t4.get()
    address = t5.get()
    gender = t6.get()
    result_status = t7.get()
    branch_code = t8.get()
    fee_status = t9.get()
    if messagebox.askyesno("Confirm Please", "Are you sure you want to update these details?"):
        query = "UPDATE students SET name=%s, dob=%s, contact_number=%s,address=%s, gender=%s, result_status=%s, branch_code=%s, fee_status=%s WHERE student_id=%s"
        cursor.execute(query,(name,dob,contact_number,address,gender,result_status,branch_code,fee_status,student_id))
        mydb.commit()
        clear()
    else:
        return True

def add_new():
    student_id = t1.get()
    name = t2.get()
    dob = t3.get()
    contact_number = t4.get()
    address = t5.get()
    gender = t6.get()
    result_status = t7.get()
    branch_code = t8.get()
    fee_status = t9.get()
    if messagebox.askyesno("Confirm Please", "Are you sure you want to enter these details?"):
        query = "INSERT INTO students(student_id,name,dob,contact_number,address,gender,result_status,branch_code,fee_status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,(student_id,name,dob,contact_number, address,gender,result_status,branch_code,fee_status))
        mydb.commit()
        clear()
    else:
        return True

def delete_student():
    student_id = t1.get()
    if messagebox.askyesno("Confirm Delete","Are you sure you want to delete this student?"):
        query = "DELETE FROM students where student_id ="+student_id
        cursor.execute(query)
        mydb.commit()
        clear()
    else:
        return True


mydb = mysql.connector.connect(host="localhost", user="root", passwd="Loveyou@123.", database="bhoomi",auth_plugin="mysql_native_password")
cursor=mydb.cursor()

root= Tk()
q=StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
t6 = StringVar()
t7 = StringVar()
t8 = StringVar()
t9 = StringVar()


img = Image.open("C:\\Users\\rahul\\OneDrive\\Desktop\\bhumi\\Student Portal\\MSRUAS.png")
img = img.resize((400,150))
my=ImageTk.PhotoImage(img)

title_label = tk.Label(root,border=12,relief=tk.GROOVE,image=my)
wrapper1 = LabelFrame(root, text="Students Details")
wrapper2 = LabelFrame(root, text="Search")
wrapper3 = LabelFrame(root, text="Students Data")

title_label.pack(side=tk.TOP,fill=tk.X)
wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

trv= ttk.Treeview(wrapper1, columns=(1,2,3,4,5,6,7,8,9), show="headings", height='6')
trv.pack()


trv.heading(1, text="Student ID")
trv.heading(2, text="Name")
trv.heading(3, text="DOB")
trv.heading(4, text="Contact No.")
trv.heading(5, text="Address")
trv.heading(6, text="Gender")
trv.heading(7, text="Result Status")
trv.heading(8, text="Branch Code")
trv.heading(9, text="Fee Status")

trv.bind('<Double 1>',getrow)


query = "SELECT * from students"
cursor.execute(query)
rows = cursor.fetchall()
update(rows)

#====================search section=====================#
lbl = Label(wrapper2, text = "Search")
lbl.pack(side=tk.LEFT,padx = 10)
ent = Entry(wrapper2, textvariable=q)
ent.pack(side=tk.LEFT,padx=6)
btn=Button(wrapper2, text="Search",command=search)
btn.pack(side=tk.LEFT,padx=6)
cbtn = Button(wrapper2, text="Clear",command=clear)
cbtn.pack(side=tk.LEFT,padx=6)
#========================================================#

#============user data section================#
lbl1= Label(wrapper3, text='Student ID')
lbl1.grid(row=0,column=0,padx=5,pady=3)
ent1 = Entry(wrapper3, textvariable=t1)
ent1.grid(row=0,column=1,padx=5,pady=5)

lbl2= Label(wrapper3, text='Name')
lbl2.grid(row=1,column=0,padx=5,pady=3)
ent2 = Entry(wrapper3, textvariable=t2)
ent2.grid(row=1,column=1,padx=5,pady=5)

lbl3= Label(wrapper3, text='DOB')
lbl3.grid(row=2,column=0,padx=5,pady=3)
ent3 = Entry(wrapper3, textvariable=t3)
ent3.grid(row=2,column=1,padx=5,pady=5)

lbl4= Label(wrapper3, text='Contact No.')
lbl4.grid(row=3,column=0,padx=5,pady=3)
ent4 = Entry(wrapper3, textvariable=t4)
ent4.grid(row=3,column=1,padx=5,pady=5)

lbl5= Label(wrapper3, text='Address')
lbl5.grid(row=4,column=0,padx=5,pady=3)
ent5 = Entry(wrapper3, textvariable=t5)
ent5.grid(row=4,column=1,padx=5,pady=5)

lbl6= Label(wrapper3, text='Gender')
lbl6.grid(row=5,column=0,padx=5,pady=3)
ent6 = Entry(wrapper3, textvariable=t6)
ent6.grid(row=5,column=1,padx=5,pady=5)

lbl6= Label(wrapper3, text='Result Status')
lbl6.grid(row=6,column=0,padx=5,pady=3)
ent6 = Entry(wrapper3, textvariable=t7)
ent6.grid(row=6,column=1,padx=5,pady=5)

lbl6= Label(wrapper3, text='Branch Code')
lbl6.grid(row=7,column=0,padx=5,pady=3)
ent6 = Entry(wrapper3, textvariable=t8)
ent6.grid(row=7,column=1,padx=5,pady=5)

lbl6= Label(wrapper3, text='Fee Status')
lbl6.grid(row=8,column=0,padx=5,pady=3)
ent6 = Entry(wrapper3, textvariable=t9)
ent6.grid(row=8,column=1,padx=5,pady=5)
#=====================================================#


#============add,update,delete button================================#
up_btn = Button(wrapper3,text='Update',command=update_student)
add_btn = Button(wrapper3,text='Add New',command=add_new)
delete_btn = Button(wrapper3,text='Delete',command=delete_student)

add_btn.grid(row=9,column=0,padx=5,pady=3)
up_btn.grid(row=9,column=1,padx=5,pady=3)
delete_btn.grid(row=9,column=2,padx=5,pady=3)
#====================================================================#
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = screen_width
window_height = screen_height



root.title("RUAS Portal")
root.geometry(f"{window_width}x{window_height}")
root.mainloop()