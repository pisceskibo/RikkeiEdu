# map(function, iterable)
numbers = [1, 2, 3, 4, 5, 6, 7]

# Tạo ra 1 mảng mà gồm các số i^2
## Cách 1: Thông thường
new_numbers = []
for i in numbers:
    new_number = i**2
    new_numbers.append(new_number)
print(new_numbers)

## Cách 2: lambda expression
"""
map(lambda i : i**2, numbers)

def function(i):
    return i**2
"""
new_numbers = list(map(lambda i : i**2, numbers))
print(new_numbers)

# filter(function, iterable)
numbers = [1, 2, 3, 4, 5, 6, 7]
searched_numbers = list(filter(lambda i : i % 2 == 1, numbers))
print(searched_numbers)

"""
map (thay thế cho def), filter (tìm kiếm) => dùng giống nhau
"""