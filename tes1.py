from tkinter import *
from Database import *

# Hàm chức năng
# Thêm thông tin sinh viên
def add():
    line = id.get() + '-' + name.get() + '-' + year.get() + '-' + Diemtb.get()
    save(line)  # Lưu thông tin vào cơ sở dữ liệu
    show()  # Hiển thị danh sách sinh viên sau khi thêm

# Xuất danh sách sinh viên
def show():
    sv = read()  # Đọc dữ liệu từ cơ sở dữ liệu
    Listbox.delete(0, END)  # Xóa danh sách hiện tại trong Listbox
    for i in sv:
        formatted_student_info = "               ".join(i)  # Tạo chuỗi thông tin sinh viên với khoảng cách 5 khoảng trắng
        Listbox.insert(END, formatted_student_info)  # Chèn thông tin sinh viên đã được định dạng vào Listbox

# Tìm sinh viên theo Mã sinh viên
def find():
    student_id_to_find = id.get()  # Lấy giá trị id trong ô nhập liệu
    sv = read()  # Đọc dữ liệu từ cơ sở dữ liệu
    found_students = [student for student in sv if student[0] == student_id_to_find]  # Tạo 1 danh sách chứa tất cả các sinh viên có mã sinh viên cần tìm
    if found_students:
        Listbox.delete(0, END)
        for student in found_students:
            formatted_student_info = "               ".join(student)
            Listbox.insert(END, formatted_student_info)
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

# Cập nhật hàm delete_student_by_id trong cơ sở dữ liệu:
def delete_student_by_id(student_id):
    sv = read()
    found_student = None
    for student in sv:
        if student[0] == student_id:
            found_student = student
            break
    if found_student:
        sv.remove(found_student)
        with open(path, 'w', encoding='utf8') as file:
            for student in sv:
                file.write('-'.join(student) + '\n')
        return True
    else:
        return False

# Sắp xếp danh sách sinh viên theo điểm
def sort():
    sv = read()
    for i in range(len(sv)):
        for j in range(len(sv)):
            x, y = sv[i], sv[j]
            if float(x[3]) > float(y[3]):  # So sánh điểm (ép kiểu sang float để so sánh)
                sv[i], sv[j] = y, x  # Hoán đổi vị trí nếu cần
    Listbox.delete(0, END)  # Xóa danh sách hiện tại trong Listbox
    for i in sv:
        formatted_student_info = "               ".join(i)
        Listbox.insert(END, formatted_student_info)

# Tạo giao diện
# Tạo cửa sổ tkinter
root = Tk()
Diemtb = StringVar()
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

# lable Name
Label(root, text='Name').grid(row=3, column=0)
Entry(root, width=30, textvariable=name).grid(row=3, column=1)

# lable năm sinh
Label(root, text='Năm Sinh').grid(row=4, column=0)
Entry(root, width=30, textvariable=year).grid(row=4, column=1)

# lable điểm
Label(root, text='Điểm').grid(row=5, column=0)
Entry(root, width=30, textvariable=Diemtb).grid(row=5, column=1)

# Tạo các nút và liên kết với các hàm tương ứng
button = Frame(root)  # Tạo button trong root
Button(button, text=' Thêm', command=add).pack(side=LEFT)
Button(button, text=' Xem', command=show).pack(side=LEFT)
Button(button, text='Tìm', command=find).pack(side=LEFT)
Button(button, text='Xoá', command=delete).pack(side=LEFT)
Button(button, text='Sắp xếp', command=sort).pack(side=LEFT)
Button(button, text=' Thoát', command=root.quit).pack(side=LEFT)
button.grid(row=6, column=1)

root.mainloop()
