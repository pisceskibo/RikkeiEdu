"""
INPUT: menubar, chức năng (1 - 4)
OUTPUT: hiện thị thông tin theo lựa chọn
"""

# Global variable
inventory_stock = 100
total_revenue = 0.0

# Chức năng 1
def add_stock(amount):
    # Tính toán giá trị inventory_stock (global variable)
    global inventory_stock
    
    """
    Số lượng hàng muốn thêm => 
        + so_luong: số tự nhiên (>=0)
        => Nhập bao nhiêu hàng
        => Tồn kho hiện tại
    """
    # Tự triển khai

# Chức năng 2
def tinh_toan_hoa_don(so_luong_muon_mua, don_gia):
     
    # Kiểm tra kho hàng
    def process_sale(quantity):
        global inventory_stock
        # Kiểm tra xem inventory_stock có giá trị nhảy sang bước 3

    # Tính toán chi phí
    def calculate_final_price(quantity, price):
        # Tính toán tổng tiền theo công thức
        final_total = 0
        
        # Viết hết logic về chức năng tính giá tiền trong này

        global inventory_stock
        inventory_stock -= quantity
        
        return final_total
    
    # Xử lý logic mà không trả về giá trị nào
    # Bước 1: Nhập đầu vào
    quantity = int(input())
    price = float(input())

    # Bước 2: kiểm tra hàng
    process_sale(quantity)

    # Bước 3: Tính toán chi phí
    calculate_final_price(quantity, price)

# Chức năng 3
def print_report():
    # Viêt docstrings
    """
    Tiêu đề hàm: Xem thông tin báo cáo

    # Có thể thêm args là các biến toàn cục
    args: (INPUT)
        inventory_stock: ..... 
        total_revenue:  .....

    return
        Thông tin báo cáo
            --- BÁO CÁO KINH DOANH ---
            Tồn kho hiện tại: ... sản phẩm
            Tổng doanh thu: $...
    """

# Phần main
while True:
    choice = int(input("Chọn chức năng: "))

    if choice == 1:
        # Xử lý các logic ở trong
        amount = input(input("Nhập số lượng sản phẩm muốn thêm: "))
        variable = add_stock(amount)
        
    elif choice == 2:
        # Xử lý các logic ở trong
        so_luong_muon_mua = int(input("Nhập số lượng muốn mua: "))
        don_gia = float(input("Nhập đơn giá tương ứng: "))

        tinh_toan_hoa_don(so_luong_muon_mua, don_gia)

    elif choice == 3:
        print_report()

    elif choice == 4:
        break
    else:
        # Xử lý các logic validate các dữ liệu
        pass