#  Tạo chương trình cho phép người dùng nhập thông tin cá nhân
print ("Tên: ", input("Vui lòng nhập tên của bạn: "))
print ("Tuổi: ", input("Vui lòng nhập tuổi của bạn: "))
print ("Lớp: ", input("Vui lòng nhập lớp của bạn: "))
print ("Sở thích: ", input("Vui lòng nhập sở thích của bạn: "))

# Ép kiểu dữ liệu int
age = int(input("Vui lòng nhập tuổi của bạn: "))
future_age = age + 10
print("Trong 10 năm nữa, bạn sẽ", future_age, " tuổi")

# Nhập vào từ bàn phím 2 số là Chiều dài và Chiều rộng của một hình chữ nhật. In ra màn hình Chu vi hình chữ nhật đó
cd = int(input("Chiều dài: "))
cr = int(input("Chiều rộng: "))
chu_vi = (cd + cr) * 2
print ("Chu vi =", chu_vi)

# Nhập vào từ bàn phím 3 số, in ra màn hình trung bình cộng của 3 số đó

a = int(input("Nhập số thứ nhất: " ))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))
tbc = int((a + b + c) / 3)
print("Trung bình cộng của 3 số là", tbc)

# Các phép toán trong python
a = 7
b = 3
print("a + b =", (a+b))
print("a - b =", (a-b))
print("a * b =", (a*b))
print("a / b =", (a/b))
print("a % b =", (a%b))
print("a // b =", (a//b))
print("a ** b =", (a**b))

# Quy đổi đô la sang tiền Việt
print("Xin chào, bạn muốn chuyển bao nhiêu tiền?")
dollar = int(input("Số tiền dollar muốn chuyển là: $"))
vnd = dollar * 23650
print("$" + str(dollar) + " = " + str(vnd) + " VND")

# Tính BMI
weight = int(input("Nhập cân nặng của bạn: "))
height = float(input("Nhập chiều cao của bạn: "))
BMI = weight/(height ** 2)
print("Chỉ số BMI của bạn là " + str(BMI))



