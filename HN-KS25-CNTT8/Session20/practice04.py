""" LIST COMPREHENSION
Chỉ sử dụng trong trường hợp logic đơn giản
"""
number_score = [1, 2, 3, 5, 6, 7]

## Tạo 1 mảng mới gồm bình phương các số trong list => list comprehension hoặc lambda
### Cách 1: Sử dụng Lambda
new_numbers = list(map(lambda i : i**2, number_score))
print(new_numbers)

### Cách 2: Sử dụng List Comprehension (khi và chỉ khi vòng lặp thực hiện duy nhất 1 tác vụ)
new_numbers_2 = [number**2 for number in number_score]
print(new_numbers_2)