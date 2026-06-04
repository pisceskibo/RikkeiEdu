# ENUMERATE()
name_array = ["Tung", "Quang", "Linh", "Minh", "Trung", "Thu"]

# Lấy theo index - value
for i in range(len(name_array)):
    print(f"{i} - {name_array[i]}")
print()

# Sử dụng enumerate
for i, value in enumerate(name_array):
    print(f"{i} - {value}")
print()

for value in enumerate(name_array):
    print(f"{value}")