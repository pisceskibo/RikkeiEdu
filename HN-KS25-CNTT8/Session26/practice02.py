# Một số loại kế thừa
"""
A -> B : kế thừa đơn
A, B -> C: đa kế thừa
A -> B -> C: kế thừa nhiều cấp
A -> B, C: kế thừa phân cấp
"""

## Kế thừa đơn
class Parent:
    def __init__(self):
        self.home = "Parent Home"
        self.room = "Phòng của gia đình"

class Children(Parent):
    def __init__(self):
        super().__init__()      # Kế thừa tất cả các thuộc tính/phương thức từ cha
        self.pool = "Bể bơi mới của con"

## Kế thừa nhiều cấp
class GrandParent:
    def __init__(self):
        self.manh_dat = 50_000_000

class Parent(GrandParent):
    def __init__(self):
        super().__init__()
        self.home = "Parent Home"
        self.room = "Phòng của gia đình"

class Children(Parent):
    def __init__(self):
        super().__init__()      # Kế thừa tất cả các thuộc tính/phương thức từ cha
        self.pool = "Bể bơi mới của con"

## Kế thừa phân cấp (ứng dụng nhiều hơn)
"""
Một cha có nhiều con
Một con chỉ có duy nhất 1 cha thôi
"""
class Parent:
    def __init__(self):
        self.ho_cua_bo = "Tran"
        self.home = "Nhà của bố"

class Children_01(Parent):
    def __init__(self):
        super().__init__()
        self.gioi_tinh = "Nam"

class Children_02(Parent):
    def __init__(self):
        super().__init__()
        self.gioi_tinh = "Nữ"

## Đa kế thừa
"""
Một lớp con có thể kế thừa từ nhiều hơn 2 lớp
"""
class Father:
    def __init__(self):
        self.dad_information = "Thông tin của bố"
    
    def xay_nha(self):
        print("Người cha xây nhà")

class Mother:
    def __init__(self):
        self.mom_information = "Thông tin của mẹ"

    def noi_tro(self):
        print("Người mẹ nội trợ trong gia đình")

class Children(Father, Mother):
    def __init__(self):
        super().__init__()  # Chỉ kế thừa Father thôi

        # Kế thừa cả cha và mẹ
        Father.__init__(self)
        Mother.__init__(self)
    
    def di_hoc(self):
        print("Đứa con đi học ở trường")

child01 = Children()
print(child01.dad_information)
print(child01.mom_information)


# Cơ chế MRO
"""
class Children(A, B, C, D, ...)
    def __init__(self):
        super().__init__() => Từ bên trái sang bên phải
"""
## Phương thức mro
print(Children.mro())