import pandas as pd
from tkinter import *
from tkinter import messagebox
# Tạo giao diện tkinter
root = Tk()
Diemtb = StringVar()
id = StringVar()  # Biến StringVar để lưu trữ MaSV
name = StringVar()  # Biến StringVar để lưu trữ Name
year = StringVar()  # Biến StringVar để lưu trữ Năm Sinh

root.title('Quản lý sinh viên')
root.minsize(height=500, width=500) 
# Tạo label và đặt nó vào cửa sổ
Label(root, text='Ứng Dụng Quản Lý Sinh Viên', fg='red', font=('cambria', 16), width=25).grid(row=0, column=0)
# Tạo một Listbox(Lưới xuất thông tin)
Listbox = Listbox(root, height=20, width=120)
Listbox.grid(row= 1, columnspan=2)

# Tạo một label "MaSV" và một Entry để nhập dữ liệu
Label(root, text='MaSV').grid(row=2, column=0)
Entry(root, width=30, textvariable=id).grid(row=2, column=1)
# Label Name
Label(root, text='Name').grid(row=3, column=0)
Entry(root, width=30, textvariable=name).grid(row=3, column=1)
# Label năm sinh
Label(root, text='Năm Sinh').grid(row=4, column=0)
Entry(root, width=30, textvariable=year).grid(row=4, column=1)
# Label điểm
Label(root, text='Điểm').grid(row=5, column=0)
Entry(root, width=30, textvariable=Diemtb).grid(row=5, column=1)


root.mainloop()
