"""
SLICING VÀ TOÁN TỬ CHUỖI
"""

# Hãng-Loại-Mã
laptop = "DELL-LAPTOP-001"

# Lấy hãng DELL
brand = laptop[0:4:1]
print(brand)

# Lấy loại
type_laptop = laptop[5:11]
print(type_laptop)

# Lấy mã
code = laptop[12:]
print(code)

# Tên hãng - tên của bạn - năm sinh
name = "Minh"
date_of_birth = "2006"
new_string = brand + "-" + name + "-" + date_of_birth
print(new_string)

# Toán tử nhân "DELL-Minh-2006-2006-2006"
## Cách 1:
new_string2 = brand + "-" + name + "-" + date_of_birth + "-" + date_of_birth + "-" + date_of_birth
print(new_string2)

## Cách 2:
new_string = brand + "-" + name + ("-" + date_of_birth)*3
print(new_string)


# TOÁN TỬ SO SÁNH (==, !=)
my_laptop = "DELL-Minh-2006"
print("Minh" in my_laptop)
print("Minh" not in my_laptop)

my_laptop2 = "DELL-Phuong-2006"
my_laptop3 = "DELL-Tung-2006"
print(my_laptop == my_laptop2)
print(my_laptop != my_laptop3)


# TOÁN TỬ SO SÁNH (>, <) dành cho bảng mã ASCII
print("A" > "B") 

"""
CẦN LƯU Ý:
==, !=, in, not in
+ chuỗi, * chuỗi
"""