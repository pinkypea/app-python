# Toán tử in

fruits = ['banana', 'apple', 'orange', 'duran', 'melon', 'water melon']
if 'car' in fruits:
    print('yes')
else: print('no')

# Câu lệnh thêm phần tử vào trong danh sách

number = [1, 2, 3]
number.append(10)
print(number)

# Câu lệnh insert

number = [1, 2, 3]
number.insert(1, 4)
print(number)

# Viết chương trình nhập vào danh sách số nguyên cho đến khi người dùng nhập -1 thì kết thúc danh sách. Sau đó in danh sách đã nhập ra màn hình

numbers = []
num = int(input("Vui lòng nhập số: "))
while num != -1:
    numbers.append(num)
    num = int(input("Vui lòng nhập số: "))
print(numbers)

# Lệnh xóa phần tử khỏi danh sách: remove, pop, clear


car = ['volvo', 'mercedes', 'lexus', 'lambo', 'honda']
# car.remove('volvo') #remove: xóa bằng giá trị phần từ
# car.pop(3) # pop: xóa bằng chỉ số phần tử
car.clear() # clear: xóa hết mảng
print(car)

# Viết chương trình để tăng tất cả các giá trị của phần tử thêm 1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(numbers)):
    numbers[i] += 1
print(numbers)

# Sắp xếp mảng bằng sort

numbers = [3, 1, 4, 5, 2]
numbers.sort()
numbers.sort(reverse = True)
print(numbers)

numbers = [1, 2, 3]
# new_numbers = numbers + [4, 5]
numbers.extend([4, 5])
print(numbers)

# Viết chương trình sắp xếp một danh sách theo thứ tự tăng dần, xóa phần tử có giá trị lớn nhất sau đó xuất mảng ra màn hình

numbers = [1, 5, 7, 6, 3, 2, 10, 9 ,8]
numbers.sort()
numbers.pop(len(numbers) -1)
print(numbers)

# Tiếp tục hoàn thiện shopping cart từ buổi 8

MindX_shop = ['áo phông', 'quần đùi', 'chuột', 'bàn phím', 'tai nghe', 'ba lô', 'lót chuột']
shopping_cart = []
while True:
    print("==========MENU=========")
    print("Ấn phím 1 để xem danh sách cửa hàng")
    print("Ấn phím 2 để xem giỏ hàng")
    print("Ấn phím 3 để thêm sản phẩm vào giỏ hàng")
    print("Ấn phím 4 để xóa sản phẩm trong giỏ hàng")
    print("Ấn phím 5 để thoát chương trình")
    choice = int(input("Nhập số mà bạn muốn: "))
    if choice == 1:
        for index, items in enumerate(MindX_shop):
            print(f"{index + 1}. {items}")
        print("========================")
    elif choice == 2:
        if not shopping_cart:
            print("Giỏ hàng của bạn đang trống.")
        else:
            print("Các mặt hàng trong giỏ hàng của bạn: ")
            for index, items in enumerate(shopping_cart):
                print(f"{index + 1}. {items}")
    elif choice == 3:
        print("Danh sách sản phẩm: ")
        for index, items in enumerate(MindX_shop):
            print(f"{index + 1}. {items}")
        print("========================")
        item_index = int(input("Nhập chỉ mục của sản phẩm bạn muốn thêm vào giỏ hàng: "))
        if item_index >= 0 and item_index < len(MindX_shop):
            shopping_cart.append(MindX_shop[item_index])
            print(f"{MindX_shop[item_index]} đã được thêm vào giỏ hàng của bạn")
        else:
            print("Chỉ mục sản phẩm không hợp lệ.")
    elif choice == 4:
        if not shopping_cart:
            print("Giỏ hàng của ban đang trống.")
        else:
            print("Danh sách sản phẩm trong giỏ hàng của bạn: ")
            for index, item in enumerate(shopping_cart):
                print(f"{index + 1}. {item}")
            item_index = int(input("Nhập chỉ mục của sản phẩm bạn muốn xóa: "))
            if item_index >= 0 and item_index < len(shopping_cart):
                delete_product = shopping_cart.pop(item_index)
                print(f"{delete_product} đã được xóa khỏi giỏ hàng của bạn")
            else:
                print("Chỉ mục sản phẩm không hợp lệ.")
    elif choice == 5:
        break