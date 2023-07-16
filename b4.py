# CHỮA BÀI TẬP VỀ NHÀ
n = int(input("Nhập số kẹo: "))
m = int(input("Nhập số học sinh: "))
so_keo_cho_nu = n % m
so_keo_cho_hoc_sinh = (n - so_keo_cho_nu) / m
print("Mỗi học sinh được chia " + str(so_keo_cho_hoc_sinh) + " viên kẹo")
print("Số kẹo dành riêng cho các bạn nữ là " + str(so_keo_cho_nu))

# x, y, z = 10, 6, 8. Kiem tra a, b, c
x = 10
y = 6
z = 8
a = x < 12 and z > 6
b = x > 15 or y < 8
c = not b
print (a, b, c)
print(type(a), type(b), type(c))

# Nhập vào từ bàn phím 1 số, kiểm tra nếu n là sỗ chẵn thì xuất ra màn hình câu n là số chẵn

# Nhập vào từ bàn phím 1 số điểm, nếu điểm lớn hơn 8 thì xuất ra màn hình câu bạn là học sinh giỏi, nếu điểm lớn hơn 6.5 thì in câu bạn là học sinh khá, nếu điểm lớn hơn 5 thì in câu bạn là học sinh trung bình, còn lại in câu bạn là học sinh kém

mark = float(input("Nhập điểm của bạn: "))
if (mark >= 8):
    print("Bạn là học sinh giỏi")
elif(mark < 8 and mark >= 6.5):
    print("Bạn là học sinh khá")
elif(mark < 6.5 and mark >= 5):
    print("Bạn là học sinh trung bình")
else:
    print("Bạn là học sinh kém")

# Xây dựng ứng dụng Math Quiz
print("Chào mừng bạn đến với trò chơi Math Quizz")
print("-----------------------------")

# Khởi tạo câu hỏi và câu trả lời
question1 = "1. Bình phương của 7 là bao nhiêu?"
answer1 = 49
question2 = "2. Căn bậc ba của 27 là bao nhiêu?"
answer2 = 3
question3 = "3. 1 có phải số nguyên tố hay không? Ấn Y là có, ấn N là không"
answer3 = "N"

# Tạo điểm cho trò chơi
score = 0

print(question1)
user_answer1 = int(input("Nhập câu trả lời câu hỏi 1: "))
if (user_answer1 == answer1):
    print("Chính xác!")
    score = score + 1
else: print("Chưa chính xác")

print(question2)
user_answer2 = int(input("Nhập câu trả lời câu hỏi 2: "))
if (user_answer2 == answer2):
    print("Chính xác!")
    score = score + 1
else: print("Chưa chính xác")

print(question3)
user_answer3 = input("Nhập câu trả lời câu hỏi 3: ")
if (user_answer3 == answer3):
    print("Chính xác!")
    score = score + 1
else: print("Chưa chính xác")

print("Bạn có", score, "điểm")