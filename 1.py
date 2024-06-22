f = open('E:/homework11/1.txt', 'a')
x = input("Nhập nội dung vào file txt. Nhấn Enter hai lần để kết thúc.\n: ")
while x:
    f.write(x+'\n')
    x = input()
    if x == '\n':
        break
f.close()
f = open('E:/homework11/1.txt', 'r')
print(f.read())