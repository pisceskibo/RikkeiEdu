from abc import ABC, abstractmethod

class BaseAccout(ABC):
    pass

    @property
    def get_balance(self):
        return self.__balance
    
    @abstractmethod
    def deposit(self, amount):
        pass

    @staticmethod
    def validate_account_number(account_number):
        # Chuyên phục vụ cho validate dữ liệu
        pass


class SavingsAccount(BaseAccout):
    def __init__(self):
        super().__init__()

class CreditAccount(BaseAccout):
    def __init__(self):
        super().__init__()

class DigitalPremiumMixin:
    @staticmethod
    def cashback_reward():
        pass

class HybridAccount(SavingsAccount, DigitalPremiumMixin):
    def __init__(self):
        super().__init__()

        SavingsAccount.__init__()
        DigitalPremiumMixin.__init__()

"""
INPUT: menubar và lựa chọn của người
OUTPUT: với mỗi chức năng trả về thông tin tương ứng

1. Mở tài khoản mới (Chọn loại tài khoản)                       => Create
2. Xem thông tin & Kiểm tra thứ tự kế thừa (MRO)                => Read
3. Giao dịch Nạp / Rút tiền & Tính điểm thưởng (Đa hình)        => Update
4. Tích lũy / Áp dụng lãi suất định kỳ                          => Update
5. Kiểm tra tính năng gộp tài khoản & So sánh (Overloading)     
6. Thanh toán hóa đơn qua Cổng trung gian (Duck Typing)
7. Thoát chương trình                                           

## Bám sát long mạch:
Thoát chương trình
Hiển thị trên menubar (Chiếm nhiều điểm)
Thêm/sửa/xóa
"""
