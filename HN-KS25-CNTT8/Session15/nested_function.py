# Nested Function (Hàm lồng hàm)
def get_information_of_student(name, age):
    id = f"{name}-{age}"

    # Lấy số điểm tương ứng của sinh viên
    """
    Nếu mà người dùng nhập số 1 => Toán, Lý hóa
    Nếu mà người dùng nhập số 2 => Toán, Văn, Anh
    """
    choice = int(input("Nhập lựa chọn của bạn: "))
    my_score = get_score(choice)

    def get_score(choice):
        if choice == 1:
            # Tính điêm theo A00
            pass
        else:
            # Tính điểm theo D01
            pass