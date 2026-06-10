"""
Tham số: các biến định nghĩa hàm (dạng tổng quát)
Đối số: giá trị thực tế ("Tung", 25, "PTIT")
"""

# Tham số thông thường
"""
Bắt buộc phải truyền đối số vào
"""
def get_student_1(name, age, school):
    print(f"{name} | {age} | {school}")
get_student_1("tung", 25, "PTIT")

# Tham số mặc định
"""
Nếu mà không có đối số => truyền mặc định giá trị khởi tạo tham số
Nếu mà có đối số => lấy giá trị đối số mới đó
"""
def get_student_2(name = "Tung", age = 18, school = "PTIT"):
    print(f"{name} | {age} | {school}")
get_student_2("Linh", 17, "VNU")

# Tham số từ khóa
def get_student_3(name, age, school):
    print(f"{name} | {age} | {school}")
get_student_3(age=17, school="PTIT", name="Tung")

# Tham số args
"""
Có thể truyền vô số các đối số trong hàm
"""
def get_all_information_in_company(name, age, room, *args):
    print(f"{name} | {age} | {room} | {args}")

## Trường hợp của nhân viên
get_all_information_in_company("Tung", 25, "IT")

## Trường hợp trưởng phòng
get_all_information_in_company("Bach", 30, "TechLead", 3, 7)