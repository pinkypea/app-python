# Chữa checkpoint 1
# Câu 1: Một trang trại chăn nuôi có x con gà và y con bò. Viết chương trình đếm số lượng chân của các con vật trong trang trại Biết rằng trong trang trại gà đều có hai chân và bò đều có bốn chân.

x = int(input("Số gà trong trang trại: "))
y = int(input("Số bò trong trang trại: "))
print (x * 2 + y * 4)

# Câu 3: Viết chương trình tính tiền lương ngày của một công nhân khi biết thông tin về giờ bắt đầu ca, giờ kết thúc ca của người đó.
# Quy định về giờ làm việc và trả lương như sau:

# - Lương trả cho mỗi giờ trước 12h trưa là 6000đ, sau 12h trưa là 7500đ. 
# - Giờ bắt đầu ca sớm nhất là 6h sáng và giờ kết thúc ca trễ nhất là 18h. 

GBD = int(input("Giờ bắt đầu: "))
GKT = int(input("Giờ kết thúc: "))
if (GBD >= 6 and GBD < 12 and GKT < 12):
    print((GKT - GBD) * 6000)
elif (GBD >= 6 and GBD < 12 and GKT > 12 and GKT <= 18):
    print((12 - GBD) * 6000 + (GKT - 12) * 7500)
elif (GBD > 12 and GKT > 12 and GKT <= 18):
    print((GKT - GBD) * 7500)
elif (GBD < 6 or GKT > 18):
    print("Đi làm kiểu gì đấy? Làm gì có ca làm như thế!")

# Câu 2: Viết chương trình giải và biện luận phương trình: ax+b=0.
# Đầu vào: Đầu vào từ bàn phím hai số nguyên a và b.
# Đầu ra: Nếu phương trình có vô số nghiệm, in ra màn hình dòng chữ: "phuong trinh co vo so nghiem". Nếu phương trình vô nghiệm, in ra màn hình  dòng chữ: "phuong trinh vo nghiem".
# Các trường hợp còn lại, in ra màn hình nghiệm của phương trình. 

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
if (a == 0 and b == 0):
    print("phuong trinh co vo so nghiem")
elif (a == 0 and b != 0):
    print("phuong trinh vo nghiem")
else: print((-b)/a)

# for i in range (m, n, p):
#     m: start
#     n: stop
#     p: step
#     print(i)

# Nhập vào từ bàn phím số n. In ra màn hình tổng các số từ 1 đến n.
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i
print("Tổng các số từ 1 đến", n, "là", sum)

# Nhập vào từ bàn phím số n. In ra màn hình tích các số chẵn từ 1 đến n.

n = int(input("Nhập số n: "))
tich = 1
for i in range(2, n + 1, 2):
        tich *= i
print("Tích các số chẵn từ 1 đến", n, "là", tich)

for i in range(5, 0, -1):
    print(i)

# Viết chương trình nhập vào số nguyên n. In ra màn hình tổng các số lẻ từ 3 đến n.

n = int(input("Nhập số n: "))
sum = 0
for i in range(3, n + 1, 2):
    sum += i
print(sum)

# Viết chương trình nhập 2 số nguyên a và b. In ra màn hình tổng các số chẵn từ a đến b.

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
sum = 0
for i in range(a, b + 1):
    if (i % 2 == 0):
        sum += i
print(sum)

# In ra màn hình bảng cửu chương từ 2 đến 9

print("Bảng cửu chương")

for i in range(2, 10):
    for j in range(1, 11):
        result = i * j
        print(i, "x", j, "=", result)
    