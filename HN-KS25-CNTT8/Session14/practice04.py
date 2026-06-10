"""
Biến global:
    + Được khai báo ngoài function
    + Bên trong function có thể sử dụng biến global (khai báo: global name_variable)

Biến local khai báo bên trong function (gọi tham số)
"""
status = False

def get_information_of_student(name, age, school):
    global status

    print(name)
    print(age)
    print(school)
    
    status = True
    # print(f"(1) --- {name} | {age} | {school}")

    return status

new_status = get_information_of_student("Tùng", 26, "PTIT")
print(new_status)