employee_number = int(input("Nhập số lượng nhân viên: "))
print()

for i in range(employee_number):
    employee_name = input("Nhập tên nhân viên: ")
    working_date = int(input("Nhập số ngày làm: "))

    if working_date != 0:
        print(f"{employee_name}: {"*"*working_date}")

    # Điều kiện không hợp lệ
    if working_date < 0 or working_date > 22:
        print("Dữ liệu không hợp lệ")
        continue

    if working_date == 0:
        print("Nhân viên nghỉ toàn bộ tháng")
        continue

    # Đánh giá nhân viên
    if working_date >= 18:
        print("Làm việc chăm chỉ")
    elif working_date < 10:
        print("Làm việc ít")
    else:
        print("Làm việc bình thường")
    
    print()