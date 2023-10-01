from tkinter import * 
from Database import*
# Thêm thông tin sinh viên 
def add():
    line = id.get() +'-'+ name.get() +'-'+ year.get() 
    save(line)
    show()
#Xuất các sinh viên đang có 
def show():
    sv = read()
    Listbox.delete(0,END)
    for i in sv:
        Listbox.insert(END,i)

def sort():
    sv = read()
    for i in range(len(sv)):
        for j in range(len(sv)):
            x,y = sv[i],sv[j]
            if x[2] < y[2]:
                sv[i],sv[j] = y,x
    Listbox.delete(0,END)
    for i in sv:
        Listbox.insert(END,i)

root = Tk()
id = StringVar()
name = StringVar()
year = StringVar()
root.title('Quản lý sinh viên')
root.minsize(height=500, width=500) 
# Tạo 1 label và đặt nó vào cửa sổ
Label(root, text='Ứng Dụng Quản Lý Sinh Viên', fg='red', font=('cambria', 16), width=25).grid(row=0, column=0)
# Tạo một Listbox và đặt nó vào cửa sổ với khoảng trống xung quanh
Listbox=Listbox(root, height=20, width=80)
Listbox.grid(row=1, columnspan=2)
# Tạo một label "MaSV" và một Entry để nhập dữ liệu
Label(root, text='MaSV').grid(row=2, column=0)
Entry(root, width=30,textvariable= id).grid(row=2, column=1)
Label(root, text='Name').grid(row=3, column=0)
Entry(root, width=30,textvariable=name).grid(row=3, column=1)
Label(root, text='Năm Sinh').grid(row=4, column=0)
Entry(root, width=30,textvariable=year).grid(row=4, column=1)
button = Frame(root)
Button(button,text = ' Thêm',command=add).pack(side =LEFT)
Button(button,text = ' Xem').pack(side =LEFT)
Button(button,text = 'Xoá').pack(side =LEFT)
Button(button,text = 'Sắp xếp',command=sort).pack(side =LEFT)
Button(button,text = ' Thoát',command=root.quit).pack(side =LEFT)
button.grid(row = 5,column=1)


root.mainloop()
