import tkinter as tk
from tkinter import *
from tkinter import ttk
import pyodbc

# Kết nối với database
db = pyodbc.connect('DRIVER={SQL Server};Server=van-bao;Database=SQLTES;Port=143;User ID=python;Password=python')
#tạo cửa sổ giao diện 
r = tk.Tk()
r.title('Quoản Lý Sinh Viên ')
r.geometry('600x300')
r.resizable(False,False)
#tạo cái fame 
frm=Frame(r)
frm.pack(side=tk.LEFT)

#Load table 
query = ' select * from SinhVien'
q_show = db.cursor()
q_show.execute(query)
rows = q_show.fetchall()

# Sử dụng Treeview để xuất 
#Tạo các ô để điền thông tin 
tree=ttk.Treeview(frm,columns=(1,2,3),show='headings',height='8')
tree.heading(1,text='ID')
tree.heading(2,text='Name')
tree.heading(3,text='Year')

#Loát dữ liệu lên để
for i in rows:
    tree.insert('','end',iid = i[0],values=i)
tree.pack()
#Delete row
def delete():
    selected = tree.selection()[0]
    query='delete from SinhVien where id=%s'
    #data phaỉ là 1 tuple mới xoá được 
    data=(selected,)
    q_del = db.cursor()
    q_del.execute(query,data)
    db.commit()
    tree.delete(selected)

#insert button
b1 =tk.Button(frm,text='Delete',bg='red',width=20,command=delete)
b1.pack()

r.mainloop()
 
