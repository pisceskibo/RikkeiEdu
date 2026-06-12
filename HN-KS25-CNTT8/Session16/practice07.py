# Sắp xếp các phần tử trong mảng
"""
array.sort(reverse=False/True)
"""
# numbers = [1, 5, 2, 7, 0, 8, 10]
# numbers.sort(reverse=True)      # Phương thức
# print(numbers)

# Đảo ngược phần tử trong mảng
numbers = [1, 5, 2, 7, 0, 8, 10]

## Cách 1:
numbers.reverse()
print(numbers)

## Cách 2: (nên nhớ)
print(numbers[::-1])