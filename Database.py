
path = 'D:\python\QLSV\QLsv.text'
def save(line):
     try:
               f = open(path, 'a',encoding='utf8') #  a ghi thêm , utf8 làm việc với cơ sở dữ liệu có tiếng việt
               f.writelines(line)  # ghi dòng line này vào
               f.writelines('\n')
               f.close()
     except:
          pass
def read():
     sv = []
     try: # Thử làm cái trong này nếu có file thì làm không thì bỏ qua
          f = open(path, 'r',encoding='utf8')
          for i in f:
               data = i.strip()
               arr = data.split('-')
               sv.append(arr)
          f.close()
     except:
          pass
     return sv