# .split(phần tử cần tách, maxsplit) tách chuỗi thành mảng (mặc định là khoảng trắng)
"""
maxsplit: chia chuỗi theo maxsplit thành maxsplit + 1 
=> mảng mới có maxsplit + 1
"""
my_information = "My name is Tung and i am a student in PTIT"
my_information_list = my_information.split(" ", 3)
print(my_information_list)

# <phần tử nối>.join(<mảng của mình>)
my_array = ['My', 'name', 'is', 'Tung', 'and', 'i', 'am', 'a', 'student', 'in', 'PTIT']
my_string = "-".join(my_array)
print(my_string)

# .replace(old, new, count)
"""
count có thể truyền vô số giá trị
"""
language_string = "Hello Python, Hello Java, Hello C++"
print(language_string.replace("Hello", "Goodbye", 7))