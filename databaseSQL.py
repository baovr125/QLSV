#import thu vien ket noi sqlserver
import pyodbc 
#ket noi sqlserver voi ten server, ten database, port(cong ket noi), userID, password
connectDB = pyodbc.connect('DRIVER={SQL Server};Server=van-bao;Database=test;Port=1433;User ID=python;Password=python')
#cursor de ket noi va de viet sql tren python
sqlCode = connectDB.cursor()
#thuc thi cau lenh sql
sqlCode.execute('select * from T')
#luu du lieu lay duoc tu sql vao 1 bien
data = sqlCode.fetchall()
#chay vong lap de hien thi du lieu da lay duoc
print('data')
for i in data:
    print(i)

                    