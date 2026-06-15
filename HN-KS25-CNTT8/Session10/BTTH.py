# Khởi tạo dữ liệu mẫu cho giỏ hàng
gio_hang = [
    {"ma_sp": "P001", "ten_sp": "Dien thoai iPhone 15", "sl": 1, "gia": 25000000},
    {"ma_sp": "P002", "ten_sp": "Op lung Silicon", "sl": 2, "gia": 150000}
]

def hien_thi_menu_va_gio_hang():
    # 1. Vẽ Menu hệ thống
    print("===============================================================")
    print(f"{'SHOPEE CART MANAGEMENT SYSTEM':^63}")
    print("===============================================================")
    print("[1] Xem chi tiet gio hang & Tinh tong tien")
    print("[2] Them san pham moi / Cong don so luong")
    print("[3] Cap nhat so luong cua mot san pham")
    print("[4] Xoa san pham khoi gio hang")
    print("[5] Thoat chuong trinh")
    print("---------------------------------------------------------------")

    # Giả lập nhập chức năng 1
    print("Moi ban chon chuc nang (1-5): 1\n")

    # 2. Vẽ bảng CHI TIẾT GIỎ HÀNG
    print(f"{'--- CHI TIET GIO HANG ---':^63}")

    # Tiêu đề cột (Độ rộng các cột: STT=4, Mã=6, Tên=25, SL=4, Đơn giá=14, Thành tiền=14)
    print(f"{'STT':<4}| {'Ma SP':<6} | {'Ten San Pham':<25} | {'SL':<4} | {'Don Gia':<14} | {'Thanh Tien':<14}")
    print("-" * 79)

    tong_so_luong = 0
    tong_tien = 0

    # Duyệt và in từng dòng sản phẩm thẳng hàng
    for i, sp in enumerate(gio_hang, start=1):
        thanh_tien = sp["sl"] * sp["gia"]
        tong_so_luong += sp["sl"]
        tong_tien += thanh_tien

        # Định dạng tiền tệ có dấu phẩy phân cách và chữ đ phía sau
        gia_str = f"{sp['gia']:,}đ"
        thanh_tien_str = f"{thanh_tien:,}đ"

        # In dòng sản phẩm căn lề chuẩn
        print(f"{i:<4}| {sp['ma_sp']:<6} | {sp['ten_sp']:<25} | {sp['sl']:<4} | {gia_str:<14} | {thanh_tien_str:<14}")

    print("-" * 79)
    # 3. In tổng kết cuối bảng
    print(f"=> Tong so luong san pham trong gio: {tong_so_luong}")
    print(f"=> TONG TIEN THANH TOAN: {tong_tien:,}đ")

# Chạy thử hàm
hien_thi_menu_va_gio_hang()