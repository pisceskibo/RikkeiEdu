"""
+ Tham số thông thường là tên biến được truyền vào trong def
+ Tham số mặc định là giá trị cụ thể truyền vào trong def
+ Tham số từ khóa là có thể đổi vị trí linh hoạt ở đối số
+ Tham số args
"""
def get_all_student(name="Minh", age=19, school="PTIT", *args):
    pass


get_all_student(age=20, name="Ninh", school="VNU")