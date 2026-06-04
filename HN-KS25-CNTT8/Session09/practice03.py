"""
+ remove(value):
    B1: Kiểm tra xem value có trong list không?
    B2: Nếu có thì xóa, không có thì lỗi

+ pop(index):
    Xóa phần tử thứ index trong mảng
    Lấy ra khỏi mảng phần tử thứ index đó

+ del list[index]:
    Xóa hẳn luôn phần tử thứ index trong mảng

+ clear():
    Xóa sạch hẳn mảng
"""

# remove() method
name_array = ["Tung", "Quang", "Linh", "Minh", "Trung", "Thu"]
name_array.remove("Tung")
print(name_array)

# pop() method
name_array.pop(1)
print(name_array)

# del list[i]
del name_array[1]
print(name_array)

# .clear() method
name_array.clear()
print(name_array)