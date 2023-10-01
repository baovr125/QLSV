import pyodbc
connectdata = pyodbc.connect('DRIVER={SQL Server};Server=van-bao;Database=SQLTES;Port=143;User ID=python;Password=python')
sqldata = connectdata.cursor()
#Tạo 1 bảng sinh viên 
# sqldata.execute('''
#                  CREATE TABLE SinhVien (
#                         Masv int primary key,
#                         HoTen nvarchar(50)
     
#                         )
#                 ''')
# connectdata.commit()
#nhập dữ liệu bảng quoản lý sinh viên 
sqldata.execute('''
                INSERT INTO SinhVien (Masv, HoTen) VALUES
                        (3,N'Lương Văn Nam'),
                        (4,N'Ngô Đình Quyền')
                ''')
connectdata.commit()



