import pandas as pd
from tkinter import *
from tkinter import messagebox

# Đường dẫn đến file CSV
csv_path = 'D:/python/QLSV/QLsv.csv'

# Hàm chức năng
# Thêm thông tin sinh viên
def add():
    student_id = id.get()
    student_name = name.get()
    student_year = year.get()
    student_diemtb = Diemtb.get()

    # Kiểm tra xem điểm nhập vào có hợp lệ không
    try:
        student_diemtb = float(student_diemtb)
        if 0 <= student_diemtb <= 10:
            df = pd.read_csv(csv_path)
            new_row = {'MaSV': student_id, 'Name': student_name, 'NamSinh': student_year, 'DiemTB': student_diemtb}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            df.to_csv(csv_path, index=False)
            show()  # Hiển thị danh sách sinh viên sau khi thêm
        else:
            messagebox.showerror("Lỗi", "Điểm phải nằm trong khoảng từ 0 đến 10.")
    except ValueError:
        messagebox.showerror("Lỗi", "Điểm phải là một số")

    # Xóa giá trị trong các ô nhập liệu sau khi thêm
    id.set('')
    name.set('')
    year.set('')
    Diemtb.set()

# Xuất danh sách sinh viên
def show():
    df = pd.read_csv(csv_path)
    Listbox.delete(0, END)  # Xóa danh sách hiện tại trong Listbox
    for index, row in df.iterrows():
        student_info = f"{row['MaSV']} - {row['Name']} - {row['NamSinh']} - {row['DiemTB']}"
        Listbox.insert(END, student_info)

# Tìm sinh viên theo Mã sinh viên
def find():
    student_id_to_find = id.get()
    df = pd.read_csv(csv_path)
    found_students = df[df['MaSV'] == student_id_to_find]
    if not found_students.empty:
        Listbox.delete(0, END)
        for index, row in found_students.iterrows():
            student_info = f"{row['MaSV']} - {row['Name']} - {row['NamSinh']} - {row['DiemTB']}"
            Listbox.insert(END, student_info)
    else:
        Listbox.delete(0, END)
        Listbox.insert(END, "Không tìm thấy sinh viên với Mã sinh viên này")

# Xoá sinh viên theo Mã sinh viên
def delete_student_by_id(student_id):
    df = pd.read_csv(csv_path)
    df = df[df['MaSV'] != student_id]
    df.to_csv(csv_path, index=False)

def delete():
    student_id_to_delete = id.get()
    df = pd.read_csv(csv_path)
    if student_id_to_delete in df['MaSV'].values:
        delete_student_by_id(student_id_to_delete)
        show()
    else:
        Listbox.delete(0, END)
        Listbox.insert(END, "Không tìm thấy sinh viên để xoá với Mã sinh viên này")

# Sắp xếp danh sách sinh viên theo điểm
def sort():
    df = pd.read_csv(csv_path)
    df = df.sort_values(by='DiemTB', ascending=False)
    df.to_csv(csv_path, index=False)
    show()

# Hàm sinh viên qua môn
def students_pass():
    df = pd.read_csv(csv_path)
    pass_students = df[df['DiemTB'] >= 4.0]
    if not pass_students.empty:
        Listbox.delete(0, END)
        for index, row in pass_students.iterrows():
            student_info = f"{row['MaSV']} - {row['Name']} - {row['NamSinh']} - {row['DiemTB']}"
            Listbox.insert(END, student_info)
    else:
        Listbox.delete(0, END)
        Listbox.insert(END, "Không có sinh viên nào qua môn")

# Hàm sinh viên rớt môn
def students_fail():
    df = pd.read_csv(csv_path)
    fail_students = df[df['DiemTB'] < 4.0]
    if not fail_students.empty:
        Listbox.delete(0, END)
        for index, row in fail_students.iterrows():
            student_info = f"{row['MaSV']} - {row['Name']} - {row['NamSinh']} - {row['DiemTB']}"
            Listbox.insert(END, student_info)
    else:
        Listbox.delete(0, END)
        Listbox.insert(END, "Không có sinh viên nào học lại")


# Tạo giao diện
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

# Label Name
Label(root, text='Name').grid(row=3, column=0)
Entry(root, width=30, textvariable=name).grid(row=3, column=1)

# Label năm sinh
Label(root, text='Năm Sinh').grid(row=4, column=0)
Entry(root, width=30, textvariable=year).grid(row=4, column=1)

# Label điểm
Label(root, text='Điểm').grid(row=5, column=0)
Entry(root, width=30, textvariable=Diemtb).grid(row=5, column=1)

# Tạo các nút và liên kết với các hàm tương ứng
button = Frame(root)  # Tạo button trong root
Button(button, text=' Thêm', command=add).pack(side=LEFT)
Button(button, text=' Xem', command=show).pack(side=LEFT)
Button(button, text='Sinh viên qua môn', command=students_pass).pack(side=LEFT)
Button(button, text='Sinh viên học lại', command=students_fail).pack(side=LEFT)
Button(button, text='Tìm', command=find).pack(side=LEFT)
Button(button, text='Xoá', command=delete).pack(side=LEFT)
Button(button, text='Sắp xếp', command=sort).pack(side=LEFT)
Button(button, text=' Thoát', command=root.quit).pack(side=LEFT)
button.grid(row=6, column=1)

root.mainloop()
