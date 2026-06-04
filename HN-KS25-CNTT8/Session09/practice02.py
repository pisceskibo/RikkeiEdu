# Thêm: append, insert, extend
"""
+ list.append(value)            => thêm value vào vị trí cuối cùng
+ list.insert(index, value)     => thêm value vào vị trí index
+ listA.extend(listB)           => thêm từng phần tử của listB vào listA
"""
score_list = [8, 9, 10, 7, 6, 6]
print(f"score_list = {score_list}")

# Thêm 1 phần tử vào list
score_list.append(0)
print(score_list)

# Thêm 1 phần tử vào vị trị trí index của list
score_list.insert(1, "Tung")
print(score_list)

# List thêm vào List
listA = [1, 2, 3, 4]
listB = ["Tung", "Quang", "Linh"]
listA.extend(listB)
print(listA)

# Sửa 
name_list = ["Tung", "Quang", "Linh"]
name_list[2] = "Minh"
print(name_list) 