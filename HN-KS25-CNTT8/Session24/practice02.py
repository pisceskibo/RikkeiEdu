# Phương thức là các hành vi của đối tượng
class SinhVien:
    # Constructor mặc định
    def __init__(self):
        self.name = "Tung"
        self.score = 9
        self.school = "PTIT"
    
    # Định nghĩa phương thức
    def get_information_of_student(self):
        print(f"Tên tôi là {self.name} được {self.score} tại trường {self.school}")

# Đối tượng đã khởi tạo cho Constructor mặc định
sv = SinhVien()
print(sv.score)
sv.get_information_of_student()

"""
Thuộc tính <=> biến
Phương thức <=> hàm function(self)
"""