# TÍNH KẾ THỪA
class Parent:
    def __init__(self):
        self.home = "Parent Home"
        self.room = "Phòng của gia đình"
        # .....

class Children:
    def __init__(self):
        self.home = "Parent Home"
        self.room = "Phòng của gia đình"
        self.pool = "Bể bơi"

# Giải pháp => tính kế thừa
"""
class Children(Parent):
    def __init__(self):
        super().__init__()
+ Nếu super().__init__() => kế thừa tất cả các thuộc tính/phương thức từ cha
+ Nếu super().__init__(atr1, atr2, ...) => kế thừa atr1, atr2, ... từ cha thôi
"""
class Children(Parent):
    def __init__(self):
        super().__init__()      # Kế thừa tất cả các thuộc tính/phương thức từ cha
        self.pool = "Bể bơi mới của con"

child = Children()
print(child.home)
print(child.pool)