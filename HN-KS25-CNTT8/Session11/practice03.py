information_dict = {
    "ID": 1,
    "Name": "Tung", 
    "School": "PTIT",
}

# Cách 1: dict[key]
print(information_dict["School"])

# TH lấy key không trong dictionary thì sao?
# print(information_dict["Age"])

# Cách 2: dict.get(key, default)
"""
+ Nếu có key trong dict thì trả về value tương ứng với key
+ Nếu không có key trong dict thì trả về default
"""
print(information_dict.get("Age", "Không có key này trong dict"))

# Thêm và sửa
"""
+ Nếu key không trong dict => new_key => Thêm => dict[new_key] = new_value
+ Nếu key trong dict => key => Sửa => dict[key] = new_value
"""
information_dict = {
    "ID": 1,
    "Name": "Tung", 
    "School": "PTIT",
}

# Thêm
print(information_dict)
information_dict["Age"] = 25
print(information_dict)

# Sửa
print(information_dict)
information_dict["Name"] = "Quang Minh"
print(information_dict)

# Xóa
"""
Cơ bản giống list (thay index = key)
pop, clear, del
"""
information_dict = {
    "ID": 1,
    "Name": "Tung", 
    "School": "PTIT",
}

# Cách 1: pop
print(information_dict)
information_dict.pop("Name")
print(information_dict)

# Cách 2: del
print(information_dict)
del information_dict["Name"]
print(information_dict)

# Cách 3: clear => xóa sạch cặp key-value
print(information_dict)
information_dict.clear()
print(information_dict)