# Viết chương trình nhập vào 1 số nguyên n và in ra tất cả các số từ n đến 100.
n = int(input("Nhập số n: "))
while n < 0:
    n = int(input("Nhập số n: "))
for i in range(n, 101, 1):
    print(i, end=" ")

n = int(input("Nhập số n: "))

# Nhập vào từ bàn phím số nguyên dương n. Tính tổng các chữ số của số n đó.
while n > 0:
    sum += n % 10
    n = n // 10
print(sum)

# Nhập vào từ bàn phím số nguyên dương n. Kiểm tra xem n có phải số hoàn hảo hay không. Biết rằng số hoàn hảo là số có tổng các ước nguyên dương không tính nó bằng chính nó.
n = int(input("Nhập số n: "))
sum = 0
while n <= 0:
    n = int(input("Nhập số n: "))
for i in range(1, n):
    if n % i == 0:
        sum += i
if (sum == n): print(n, "là số hoàn hảo")
else: print(n, "không là số hoàn hảo")

# Trò chơi Mysterious number
import random
mysterious_number = random.randint(0, 10)
print(mysterious_number)
n = int(input("Nhập số cần đoán: "))
while n != mysterious_number:
    print("Sai rồi!")
    if n > mysterious_number: 
        print(n, "lớn hơn số bí ẩn")
        n = int(input("Nhập số cần đoán: "))
    elif n < mysterious_number: 
        print(n, "bé hơn số bí ẩn")
        n = int(input("Nhập số cần đoán: "))
print("Chúc mừng")
