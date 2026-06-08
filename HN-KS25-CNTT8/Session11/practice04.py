# Duyệt các phần tử trong dictionary
"""
+ Duyệt theo key => dict.keys() hoặc dict
+ Duyệt theo value => .values()
+ Duyệt theo cả key, value =. .items() hoặc là (key, dict[key])
"""

information_dictionary = {
    "id": 1,
    "name": "Tung",
    "age": 20,
    "school": "PTIT",
    "date_of_birth": 2000,
    "score": 9
}
# Cách duyệt theo key
print(information_dictionary.keys())
for key in information_dictionary.keys():
    print(f"key = {key}")

print(information_dictionary)
for data in information_dictionary:
    print(data)

# Cách duyệt theo value
print(information_dictionary.values())
for value in information_dictionary.values():
    print(f"value = {value}")

# In ra cả cặp key và value như nào?
## Cách 1:
for key in information_dictionary.keys():
    print(f"{key} | {information_dictionary[key]}")

## Cách 2: .items()
for key, value in information_dictionary.items():
    print(f"{key} | {value}")