"""
Cấp độ truy cập:
+ public (default): truy cập mọi lúc mọi nơi
+ protected: dùng cho class/subclass
+ private: hạn chế tối đa truy cập trực tiếp vào đây => giải pháp là getter và setter

Ký hiệu khai báo:
self.<tên biến> => public
self._<tên biến> => protected (dùng khá ít)
self.__<tên biến> => private

getter/setter (thuộc tính của mình là private)
+ getter là lấy ra giá trị của thuộc tính 
+ setter là thay đổi giá trị của thuộc tính
"""

class NganHang:
    def __init__(self):
        self.name = "BIDV Banking"
        self._tien_gui = 1_000_000
        self.__tien_trong_tai_khoan = 20_000_000

        # Nếu dùng property
        self.get_tien_tai_khoan = self.get_tien_tai_khoan()

    # Getter
    @property
    def get_tien_tai_khoan(self):
        print(f"Số tiền tài khoản hiện tại của tôi là: {self.__tien_trong_tai_khoan}")

    # Setter
    @get_tien_tai_khoan.setter
    def get_tien_tai_khoan(self, new_value):
        self.__tien_trong_tai_khoan = new_value

# Khai báo đối tượng
ngan_hang = NganHang()
# print(f"Name: {ngan_hang.name}")
# print(f"Tiền gửi: {ngan_hang.tien_gui}")
# print(f"Tiền trong TK: {ngan_hang.tien_trong_tai_khoan}")
ngan_hang.get_tien_tai_khoan

# Nếu dùng @property thì sẽ đưa phương thức về thuộc tính
"""
Nếu có @property => ngan_hang.get_tien_tai_khoan => thuộc tính
Nếu không có => ngan_hang.get_tien_tai_khoan() => vẫn là phương thức
"""

# Setter
"""
@<tên method của getter>.setter
"""
ngan_hang.get_tien_tai_khoan = 10_000_000
ngan_hang.get_tien_tai_khoan