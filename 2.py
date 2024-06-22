import datetime
f = open('E:/homework11/2.txt', 'a')
x = input("Nhập nội dung vào file txt. Nhấn Enter hai lần để kết thúc.\n: ")
while x:
    
    current_time = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    f.write(f"{current_time} {x}\n")
    f.write(x+'\n')
    x = input()
    if x == '\n':
        break
f.close()
f = open('E:/homework11/2.txt', 'r')
print(f.read())