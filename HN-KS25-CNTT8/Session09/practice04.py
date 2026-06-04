name_array = ["Tung", "Quang", "Linh", "Minh", "Trung", "Thu"]

# Duyệt các phần tử trong mảng
length_name_array = len(name_array) # 6
print(name_array[0])
print(name_array[1])
print(name_array[2])
print(name_array[3])
print(name_array[4])
print(name_array[5])
"""
for i in range(start, stop, step):
    => Thực thi câu lệnh
"""

## Cách 1: Duyệt theo index
for idx in range(len(name_array)):
    print(name_array[idx])
print()

## Cách 2: Duyệt theo value
for value in name_array:
    print(value)
print()

## Duyệt danh sách những sinh viên bắt đầu bằng chữ "T"
for value in name_array:
    # if "T" in value:
    #     print(value)

    if value.startswith("T"):
        print(value)
print()

## Duyệt phần tử trong mảng bằng while
print("Duyệt phần tử trong mảng bằng while")
i = 0
while i < len(name_array):
    print(name_array[i])
    i += 1