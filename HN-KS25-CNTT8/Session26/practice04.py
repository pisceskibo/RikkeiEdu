# TÍNH ĐA HÌNH => lấy tính chất từ kế thừa
"""
Ghi đè (override): thay đổi lại phương thức từ lớp cha
Nạp chồng (overloading): 
"""

## Ghi đè
class Animal:
    def tieng_keu():
        print("Tiếng kêu của con vật")

class Cat(Animal):
    def tieng_keu(self):
        print("Meow Meow")

class Dog(Animal):
    def tieng_keu(self):
        print("Gou Gou")

class Cow(Animal):
    def tieng_keu(self):
        print("Boo Boo")

cat = Cat()
dog = Dog()
cow = Cow()

cat.tieng_keu()
dog.tieng_keu()
cow.tieng_keu()

## Nạp chồng
class SinhVien:
    def tong_diem(self, *args):
        return sum([*args])
    
sv = SinhVien().tong_diem(10, 9, 8)
print(sv)

sv2 = SinhVien().tong_diem(10, 9, 9, 1, 4)
print(sv2)