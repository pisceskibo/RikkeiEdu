# Static Method
"""
Chỉ sử dụng khi chỉ cần thực hành vi mà không cần liên quan đến thuộc tính
"""

class MathOperator:
    # def __init__(self):
    #     pass

    @staticmethod
    def add_function(x, y):
        print(x + y)

phep_tinh = MathOperator()
phep_tinh.add_function(10, 5)
"""
static method biến các phương thức method(self) thành các function() bình thường
"""