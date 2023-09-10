# Sự khác biệt của array và string
A = ["a", "b", "c", "d", "e"]
A[0] = "f"
print(A)

B = "abcde"
B[0] = "f"
print(B)

# Lệnh duyệt ký tự của xâu

A = 'MindX School'
for i in range(len(A)):
    print(A[i])

# Viết chương trình xuất ra màn hình các ký tự của xâu ngoại trừ các khoảng trắng
s = input("Nhập chuỗi: ")
for i in range(len(s)):
    if s[i] != " ":
        print(s[i])

Sử dụng in để kiểm tra xâu con

xau1 = "Hello"
xau2 = "Hello, world"
if xau1 in xau2:
    print("Xâu 1 nằm trong xâu 2")
else: 
    print("Xâu 1 không nằm trong xâu 2")

# Sử dụng find() để tìm xâu con

s = "abcd123"
a = "abc"
b = "d12"
c = "1234"
print(s.find(a))
print(s.find(b))
print(s.find(c))

# Cú pháp đầy đủ của find()

string = "Hello world"
index = string.find("o", 3, 8)
print(index)

# Viết chương trình nhập vào một câu, yêu cầu người dùng nhập một từ cần tìm kiếm trong câu đó. Hãy kiểm tra từ cần tìm kiếm có xuất hiện trong câu hay không.

string = input("Nhập vào 1 câu: ")
index = input("Nhập từ cần tìm kiếm: ")
if index in string:
    print("Từ đó có trong câu")
else:
    print("Từ đó không có trong câu")

# Viết chương trình nhập vào Họ và Tên vào 2 biến khác nhau. Sau đó xuất ra màn hình Họ và Tên đầy đủ mà mình vừa nhập

ho = input("Họ: ")
ten = input("Tên: ")
hoVaTen = ho + " " + ten
print("Họ và tên đầy đủ: ", hoVaTen)

# Sử dụng replace để thay thế ký tự trong xâu

txt = "one one was a race horse, two two has one two"
x = txt.replace("one", "three", 2)
print(x)

# Viết chương trình nhập vào 1 chuỗi là 'Họ và tên' của bản thân. Xuất ra màn hình mỗi từ một dòng

# Nhập chuỗi từ người dùng
ho_ten = input("Nhập Họ và tên của bạn: ")

# Tách chuỗi thành các từ bằng dấu khoảng trắng
tu_khoa = ho_ten.split()

# Xuất mỗi từ trên một dòng
for i in range (len(tu_khoa)):
    print(tu_khoa[i])

# Viết chương trình nhập vào họ và tên của một người. Hãy sử dụng lệnh find, duyệt và xuất ra màn hình họ của người đó.

hoVaTen = input("Nhập họ và tên: ")
khoang_trang_dau_tien = hoVaTen.find(" ")
ho = ''
for i in range(khoang_trang_dau_tien):
    ho += hoVaTen[i]
print(ho)

# Viết chương trình kiểm tra tên đăng nhập mà mật khẩu đăng nhâp

thong_tin_dang_nhap = "MindX:12345"
username, password = thong_tin_dang_nhap.split(":")
input_username = input("Nhập username: ")
input_password = input("Nhập password: ")
while input_username != username or input_password != password:
    print("Thông tin đăng nhập không chính xác, vui lòng nhập lại!")
    input_username = input("Nhập username: ")
    input_password = input("Nhập password: ")
print("Đăng nhập thành công")