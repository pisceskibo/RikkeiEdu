"""
# Tiêu chuẩn python => tên biến + tên function => snake_case
def name_function(tham số 1, tham số 2, ...):
    # Thực hiện logic như bình thường

# Cách gọi hàm
name_function(tham số 1, tham số 2, ...)

=> Function là khối đóng gói các chức năng
"""

student_list = ["Tung", "Linh", "Trung", "Anh"]
score_list = [8, 9, 10, 7]

# Thực trạng
for student in student_list:
    print(student)

for score in score_list:
    print(score)

# Giải pháp 
def get_all_list(information_list):
    """
    Nội dung, ý tưởng, mục đích, .....
    """
    for infor in information_list:
        print(infor)
get_all_list(score_list)

# Ví dụ
def get_student(name, age, school):
    print(f"{name} | {age} | {school}")

get_student("Tung", 25, "PTIT")
get_student("Nhung", 20, "VNU", 2001)   # Error