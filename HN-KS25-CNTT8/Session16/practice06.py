# filter(function, iterable)
numbers = [1, 2, 3, 4, 5, 6, 7]
searched_numbers = list(filter(lambda i : i % 2 == 1, numbers))
print(searched_numbers)

"""
map (thay thế cho def), filter (tìm kiếm) => dùng giống nhau
"""