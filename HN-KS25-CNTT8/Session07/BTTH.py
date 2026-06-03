"""
XÂY DỰNG HỆ THỐNG CHUẨN HÓA VÀ TẠO THẺ THÀNH VIÊN
"""

# Chuỗi dữ liệu thô
raw_input = "   nGuyen vaN aN  ;  2004   "

menubar = """
===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====
1. Hiển thị chuỗi dữ liệu gốc
2. Chuẩn hóa Họ tên và tính Tuổi
3. Tạo Mã ID và Email tự động
4. Thoát chương trình
=====================================
"""

while True:
    print(menubar)
    input_user = int(input("Nhập lựa chọn của bạn (1-4): "))

    user_array = raw_input.split(";")
    name = user_array[0].strip().title()
    year = user_array[1].strip()

    if input_user == 1:
        print(raw_input)

    elif input_user == 2:
        age = 2026 - int(year)
        summary_user = f"""
[KẾT QUẢ CHUẨN HÓA DỮ LIỆU]
- Họ và tên: {name}
- Tuổi hiện tại: {age} tuổi
"""
        print(summary_user)
        
    elif input_user == 3:
        # Tạo mã ID
        name_array = name.split(" ")
        last_name = name_array[-1].upper()
        last_year = year[2:]

        code = last_name + last_year
        
        # Tạo email
        first_name = name_array[0]
        char_first_name = first_name[0].lower()
        second_name = name_array[1]
        char_second_name = second_name[0].lower()

        email = f"{char_first_name}{char_second_name}{last_name.lower()}@company.com"
        
        summary_new_user = f"""
=====================================
THẺ THÀNH VIÊN MỚI
=====================================
Họ và tên   : {name}
Mã ID       : {code}
Email       : {email}
"""
        print(summary_new_user)

    elif input_user == 4:
        print("Chương trình đã dừng!")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")