"""
So sánh return và print trong function
"""
# Cách 1: Nếu không có return => không cần gán biến
def get_information_of_student_1(name, age, school):
    print(f"(1) --- {name} | {age} | {school}")

# Cách 2: Nếu có return => trả về 1 biến biến
def get_information_of_student_2(name, age, school):
    return f"(2) --- {name} | {age} | {school}"

get_information_of_student_1("tung", 25, "PTIT")
student = get_information_of_student_2("tung", 25, "PTIT")
print(student)