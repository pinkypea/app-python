# Viết hàm nhập vào họ và tên rồi đưa lời chào ra màn hình
def greeting():
    full_name = input("Nhập họ và tên của bạn: ")
    print("Xin chào", full_name)

greeting()

# Viết hàm nhập vào 1 số nguyên, xuất ra màn hình giá trị tuyệt đối của số nguyên đó
def abs_number():
    number = int(input("Nhập vào 1 số nguyên: "))
    print(abs(number))
abs_number()

# Viết hàm nhập vào 1 số nguyên dương, tính tổng các số chẵn từ 1 đến n.

def sum_even_number():
    n = int(input("Nhập vào 1 số nguyên dương: "))
    sum = 0
    for i in range(2, n + 1, 2):
        sum += i
    print(sum)
sum_even_number()

# Viết chương trình nhập vào tên, tuổi và ngày sinh của bản thân, sử dụng hàm để in ra những thông tin đó
def information(name, age, dob):
    print("Thông tin cá nhân: ")
    print("Tên: ", name)
    print("Tuổi: ", age)
    print("Ngày sinh: ", dob)

ten = input("Nhập tên của bạn: ")
tuoi = input("Nhập tuổi của bạn: ")
ngay_sinh = input("Nhập ngày sinh của bạn: ")

information(ten, tuoi, ngay_sinh)

# Viết chương trình nhập vào 1 danh sách số nguyên, sử dụng hàm để xuất ra các phần tử của danh sách vừa nhập và tổng của danh sách đó

def in_danh_sach_va_tong_phan_tu(danh_sach):
    print("Danh sách các phần từ là: ")
    for i in danh_sach:
        print(i)
    tong = sum(danh_sach)
    print(tong)

danh_sach = []
n = int(input("Nhập số phần tử trong danh sách: "))
for i in range(n):
    so = int(input("Nhập phần tử: ".format(i + 1)))
    danh_sach.append(so)

in_danh_sach_va_tong_phan_tu(danh_sach)

# Viết chương trình nhập vào 1 số nguyên dương, khởi tạo 1 hàm để xuất ra màn hình tổng các số từ 1 đến n, tổng các số từ 1 đến n//2 và từ n//2 đến n

def tinh_tong(a, b):
    tong = 0
    for i in range (a, b + 1):
        tong += i
    print(tong)

n = int(input("Nhập vào 1 số nguyên dương: "))
tinh_tong(1, n)
tinh_tong(1, n//2)
tinh_tong(n//2, n)

# Biến cục bộ
def sum():
    a = 3
    b = 5
    print(a + b)
sum()

print(a + b)

# Biến toàn cục

a = 10
b = 2
def tinh_tong():
    print(a + b)
tinh_tong()
print(a + b)

# Viết chương trình cho phép người dùng chọn đăng nhập và đăng ký tài khoản. Dữ liệu sẽ được lưu trên danh sách, mỗi account là 1 phần tử lưu dưới dạng "username:password"

users = []
def register():
    username = input("Nhập tên đăng nhập: ")
    password = input("Nhập mật khẩu: ")
    check_register = True
    for user in users:
        stored_username, stored_password = user.split(":")
        if stored_username == username:
            check_register = False
    if check_register == True:
        users.append(username + ":" + password)
        print("Đăng ký thành công!")
    else:
        print("Tài khoản đã tồn tại!")

def login():
    username = input("Nhập tên đăng nhập: ")
    password = input("Nhập mật khẩu: ")
    check_login = False
    for user in users:
        stored_username, stored_password = user.split(":")
        if stored_username == username and stored_password == password:
            check_login = True
    
    if check_login == True:
        print("Đăng nhập thành công!")
    else:
        print("Đăng nhập không thành công!")

def main():
    while True:
        print("1. Đăng ký")
        print("2. Đăng nhập")
        print("3. Thoát")

        choice = int(input("Nhập lựa chọn của bạn: "))

        if choice == 1:
            register()
        elif choice == 2:
            login()
        elif choice == 3:
            break
        else:
            print("Lựa chọn của bạn không hợp lệ")

main()