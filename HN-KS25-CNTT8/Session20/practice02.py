""" CODE REVIEWER
Không được import các thư viện thừa
"""

## Tính tổng điểm của sinh viên
def sum_of_score(math_score: float, physic_score: float, chemistry_score: float) -> float:
    return math_score + physic_score + chemistry_score

print(sum_of_score(9, 8, 8))

"""
Các chức năng nên được tách thành các function riêng
Mỗi function thực hiện duy nhất 1 chức năng
"""

## Nhập xuât thư viện
from typing import Optional
import pandas as mlp
"""
from thư viên import class, biến, phương thức, hàm, ....
import thư viên as tên của thư viện (tự đặt)
"""

# Type Hinting (typing) => tùy quy mô dự án
"""
tham_so: Optional[kiểu dữ liệu] = None
"""
from typing import Optional

def caculate_discount(
        price: float,
        rate: float,
        user_id: Optional[int] = None,
        cost: Optional[float] = 0
):
    pass