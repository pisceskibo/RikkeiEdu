# NẠP CHỒNG TOÁN TỬ
class PhepTinh:
    def __init__(self, x):
        self.x = x
    
    def __add__(self, other):
        return PhepTinh(self.x + other.x)

    """
    Thay thế cho tên địa chỉ ô nhớ
    """
    def __str__(self):
        return f"Kết quả của phép tính là: {self.x}"


a = PhepTinh(5)
b = PhepTinh(10)
c = a + b
print(f"c = {c}")