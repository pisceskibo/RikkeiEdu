# Khởi tạo tuple
my_tuple = (1, 2, 3, 4, )
my_tuple2 = ("Tung", "Quang", "Trang", )
my_tuple3 = 1, 2, 3, 4

# Cách lấy giá trị trong Tuple
print(my_tuple[1])

# Cách kết hợp tuple => Dùng vòng for để duyệt các phần tử
tuple_a = ("Tung", "Minh", "Trang")
tuple_b = ("Trung", "Tien", "Linh", "Anh")
new_tuple = tuple_a + tuple_b
print(new_tuple)

# Tính chất nhân trong tuple
"""
new_tuple = old_tuple*number 
"""
my_tuple = (1, 2, 3, 4, )
print(my_tuple*5)