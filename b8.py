
# Trả về độ dài của mảng: Sử dụng len()
# number = [1, 2, 3, 4, 5]
# print(len(number))

# Duyệt phần tử
# n = int(input())
# a = [n]
# for i in range(n):
#     int(input(a[i]))
# for i in range(n):
#    print(a[i])

# Cho mảng A. In ra các số chẵn của mảng A:
# A = [1 ,2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in range(len(A)):
#     if (A[i] % 2 == 0):
#         print(A[i])

# Cho danh sách A và B. In ra màn hình các số mà danh sách A và B đều có:
# A = [1, 2, 3, 4]
# B = [1, 2, 3]

# for i in range(len(A)):
#     for j in range(len(B)):
#         if (A[i] == B[j]):
#             print(A[i])

# A = [3, 4, 2]
# B = [7, 8, 9]

# sum_A = (A[0] + A[1]+ A[2]) % 10
# sum_B = (B[0] + B[1] + B[2]) % 10

# if (sum_A > sum_B){}

cart = ['áo phông', 'quần đùi', 'chuột', 'bàn phím', 'tai nghe', 'mũ bảo hiểm', 'lót chuột']

while True:
    print("==========MENU=========")
    print("Ấn phím 1 để xem giỏ hàng")
    print("Ấn phím 2 để ...")
    print("Ấn phím 3 để ...")
    print("Ấn phím 4 để ...")
    print("Ấn phím 5 để thoát chương trình")
    choice = int(input("Nhập số mà bạn muốn: "))
    if choice == 1:
        for index, items in enumerate(cart):
            print(f"{index + 1}. {items}")
        print("========================")
    elif choice == 5:
        break