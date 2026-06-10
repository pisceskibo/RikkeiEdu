# Đây là docstring
def get_information_student(name, age, school):
    """
    Tiêu đề hàm: Lấy ra thông tin của học sinh

    args:
        + name: tên của học sinh
        + age: tuổi của học sinh
        + school: trường của học sinh

    return
        + In ra đươc thông tin của học sinh theo định "name | age | school"

    raise (bắt lỗi)
        + Sai kiểu dữ liệu
        + Chưa validate biến dữ liệu

    example:
        get_information_student("Tung", 25, "PTIT")
        => Tung | 25 | PTIT
    """
    return f"{name} | {age} | {school}"

new_student = get_information_student("Tung", 25, "PTIT")
print(new_student)