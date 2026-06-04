# Cách khởi tạo

## Cách 1: List rỗng []; list() => ép kiểu cấu trúc dữ liệu
array_list = []
array_list2 = list()

print(array_list)
print(array_list2)

# a = {1, 2, 3} => list(a)
a = {1, 2, 3}
print(a)
print(list(a))

## Cách 2: Khai báo cùng và khác kiểu dữ liệu
name_list = ["Tung", "Phuong", "Hong", "Mai"]
score_list = [8, 9, 10, 7]
students = ["Trang", 18, "Ha Noi", 8.7] # Đa kiểu dữ liệu

print(name_list)
print(score_list)
print(students)

# Cơ chế index
name_list = ["Tung", "Phuong", "Hong", "Mai"]
print(name_list[0])
print(name_list[3])
print(name_list[-1])
print(name_list[-2])