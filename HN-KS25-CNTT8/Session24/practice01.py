"""
class: bản phác thảo
Object: đối tượng cụ thể mà cần phác tháo
"""
class MyObject:
    pass

"""
Thuộc tính là những vật tĩnh 
Phương thức là vật động (hành động, hành vi)
"""
# Căn nhà
class MyHome:
    pass
    """
    Cửa nhà, xe trong nhà, ....
    Phòng ăn, phòng ngủ, ...
    """

# Contructor
"""
Khi làm việc với OOP thì phải sử dụng "self"
"""
class SinhVien:
    # Hàm khởi tạo ban đầu
    """
    self.biến => thuộc tính
    """
    
    # ## Cách 1: Constructor mặc định
    # def __init__(self):
    #     self.name = "Tung"
    #     self.score = 9
    #     self.school = "PTIT"

    # Cách 2: Constructor tự khai báo
    def __init__(self, name, score, school):
        self.name = name
        self.score = score
        self.school = school

# Đối tượng đã khởi tạo cho Constructor mặc định
sv = SinhVien()
print(sv.score)

# Đối tượng đã khởi tạo cho Constructor tự khai báo
sv = SinhVien("Phong", 10, "PTIT")
print(sv.name)
print(sv.score)
print(sv.school)

"""
Constructor mặc định <=> tham số mặc định
Constructor tự khai báo <=> tham số thông thường
=> Liên kết tới kiến thức về function
"""