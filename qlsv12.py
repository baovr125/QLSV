from tkinter import *
from Database import *

# Thêm thông tin sinh viên
def add():
    line = id.get() + '-' + name.get() + '-' + year.get() 
    save(line)  # Lưu thông tin vào cơ sở dữ liệu
    show()  # Hiển thị danh sách sinh viên sau khi thêm

# Xuất danh sách sinh viên
def show():
    sv = read()  # Đọc dữ liệu từ cơ sở dữ liệu
    Listbox.delete(0, END)  # Xóa danh sách hiện tại trong Listbox
    for i in sv:
        Listbox.insert(END, i)  # Chèn thông tin sinh viên vào Listbox

# Tìm sinh viên theo Mã sinh viên
def find():
    student_id_to_find = id.get()
    sv = read()  # Đọc dữ liệu từ cơ sở dữ liệu
    found_students = [student for student in sv if student[0] == student_id_to_find]
    if found_students:
        Listbox.delete(0, END)
        for student in found_students:
            Listbox.insert(END, student)
    else:
        Listbox.delete(0, END)
        Listbox.insert(END, "Không tìm thấy sinh viên với Mã sinh viên này")

# Xoá sinh viên theo Mã sinh viên
def delete():
    student_id_to_delete = id.get()
    deleted = delete_student_by_id(student_id_to_delete)
    if deleted:
        show()
    else:
        Listbox.delete(0, END)
        Listbox.insert(END, "Không tìm thấy sinh viên để xoá với Mã sinh viên này")

# Sắp xếp danh sách sinh viên theo năm sinh
def sort():
    sv = read()  # Đọc dữ liệu từ cơ sở dữ liệu
    for i in range(len(sv)):
        for j in range(len(sv)):
            x, y = sv[i], sv[j]
            if x[2] < y[2]:  # So sánh năm sinh
                sv[i], sv[j] = y, x  # Hoán đổi vị trí nếu cần
    Listbox.delete(0, END)  # Xóa danh sách hiện tại trong Listbox
    for i in sv:
        Listbox.insert(END, i)  # Chèn thông tin sinh viên đã sắp xếp vào Listbox

# Tạo cửa sổ tkinter
root = Tk()
id = StringVar()  # Biến StringVar để lưu trữ MaSV
name = StringVar()  # Biến StringVar để lưu trữ Name
year = StringVar()  # Biến StringVar để lưu trữ Năm Sinh

# Tạo giao diện tkinter
root.title('Quản lý sinh viên')
root.minsize(height=500, width=500) 

# Tạo label và đặt nó vào cửa sổ
Label(root, text='Ứng Dụng Quản Lý Sinh Viên', fg='red', font=('cambria', 16), width=25).grid(row=0, column=0)

# Tạo một Listbox và đặt nó vào cửa sổ với khoảng trống xung quanh
Listbox = Listbox(root, height=20, width=80)
Listbox.grid(row=1, columnspan=2)

# Tạo một label "MaSV" và một Entry để nhập dữ liệu
Label(root, text='MaSV').grid(row=2, column=0)
Entry(root, width=30, textvariable=id).grid(row=2, column=1)

Label(root, text='Name').grid(row=3, column=0)
Entry(root, width=30, textvariable=name).grid(row=3, column=1)

Label(root, text='Năm Sinh').grid(row=4, column=0)
Entry(root, width=30, textvariable=year).grid(row=4, column=1)

button = Frame(root)

# Tạo các nút và liên kết với các hàm tương ứng
Button(button, text=' Thêm', command=add).pack(side=LEFT)
Button(button, text=' Xem', command=show).pack(side=LEFT)
Button(button, text='Tìm', command=find).pack(side=LEFT)
Button(button, text='Xoá', command=delete).pack(side=LEFT)
Button(button, text='Sắp xếp', command=sort).pack(side=LEFT)
Button(button, text=' Thoát', command=root.quit).pack(side=LEFT)

button.grid(row=5, column=1)

root.mainloop()
