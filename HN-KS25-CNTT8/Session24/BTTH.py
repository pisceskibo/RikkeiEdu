class Drink:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.__price = price
        self.is_available = True

    @property
    def get_price(self):
        return self.__price

# INPUT: menubar gồm list các Object
menu = [
    Drink("CF01", "Cà phê sữa", 35000),
    Drink("TS01", "Trà sữa matcha", 45000),
    Drink("TD01", "Trà đào cam sả", 40000)
]

menubar = """
=== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE ===

1. Xem danh sách đồ uống
2. Thêm đồ uống mới
3. Cập nhật trạng thái kinh doanh
4. Thoát chương trình

==============================================
"""

while True:
    print(menubar)
    choice = int(input("Chọn chức năng (1 - 4): "))

    # Chức năng 1: Xem danh sách
    if choice == 1:
        # Tạo function riêng
        print("--- DANH SÁCH ĐỒ UỐNG ---")
        print("Mã món | Tên món | Giá bán | Trạng thái")
        print("-------------------------------------------------")

        for drink in menu:
            print(f"{drink.code} | {drink.name} | {drink.get_price} | {drink.is_available}")

    elif choice == 2:
        code_drink = input("Nhập mã món: ")
        name_drink = input("Nhập tên món: ")
        cost_drink = float(input("Nhập giá bán: "))

        # Kiểm tra mã món không trùng nhau
        ma_do_uong_hien_tai = []
        for check_drink in menu:
            ma_do_uong_hien_tai.append(check_drink.code)
        if code_drink in ma_do_uong_hien_tai:
            print("Mã món không được trùng với món đã có")
            continue

        # Kiểm tra giá bán không được âm  
        if cost_drink <= 0:
            print("Giá bán phải lớn hơn 0")
            continue

        created_drink = Drink(code_drink, name_drink, cost_drink)
        menu.append(created_drink)
    elif choice == 3:
        pass
    elif choice == 4:
        print("Cảm ơn bạn đã sử dụng hệ thống quản lý thực đơn Rikkei Coffee!")
        break
    else:
        print("Xử lý ngoại lệ tại đây")