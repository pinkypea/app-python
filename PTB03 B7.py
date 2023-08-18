# Chữa bài tập về nhà
# Xây dựng chương trình nhập vào một số nguyên dương n. Hãy tính tổng các số chẵn từ 1 đến n bằng cách sử dụng vòng lặp for và in kết quả ra màn hình.
n = int(input("Nhập số nguyên dương n: "))
sum = 0
for i in range(2, n + 1, 2):
    sum += i
print("Tổng các số chẵn từ 1 đến", n, "là", sum)

# Xây dựng chương trình nhập vào một số nguyên dương n. Hãy xử lý và in ra màn hinh các số chẵn từ 1 đến n.

n = int(input("Nhập vào số nguyên dương n: "))
for i in range(2, n + 1, 2):
    print(i , end=" ")

# Viết chương trình nhập vào số x, biết 0 <= x <= 100. Nếu người dùng nhập x ngoài khoảng [0, 100] thì bắt người dùng nhập lại, nếu nhập đúng thì in ra màn hình x%
x = int(input("Nhập số x: "))
while x < 0 or x > 100:
    x = int(input("Nhập lại x: "))
print(x, "%")

# Viết chương trình xác nhận mật khẩu.

password = input("Nhập mật khẩu: ")
confirm_password = input("Xác nhận lại mật khẩu: ")

while confirm_password != password:
    confirm_password = input("Xác nhận lại mật khẩu: ")
print("Xác nhận mật khẩu thành công!")


# Nhập vào từ bàn phím số nguyên dương n. In ra màn hình tổng các chữ số của n.

n = int(input("Nhập số nguyên dương n: "))
sum = 0
while n > 0:
    sum += n % 10
    n = n // 10
print(sum)

# Viết chương trình nhập vào số nguyên dương n. Kiểm tra xem n có phải số hoàn hảo hay không? Biết rằng số hoàn hảo là số có tổng các ước không tính nó bằng chính nó.

n = int(input("Nhập số n: "))
sum = 0
while n <= 0:
    n = int(input("Nhập số n: "))
# for i in range(1, n):
#     if n % i == 0:
#         sum += i

i = 1
while i < n:
    if n % i == 0:
        sum += i
    i += 1
if (sum == n): print(n, "là số hoàn hảo")
else: print(n, "không là số hoàn hảo")