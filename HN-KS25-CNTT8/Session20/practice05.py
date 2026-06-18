# SỬ LÝ NGOẠI LỆ TRY - EXCEPT
"""
try:
    # Các logic mình chưa chắc và có thể sinh ra crash web/app
except:
    # Bắt lỗi tương ứng => trong TH tránh bị crash app
else:
    # Nếu mà không bị crash => thì sẽ chạy vào đây
finally:
    # Kể cả bị crash hay không => luôn luôn chạy vào đây
"""
def divide_numbers(a, b):
    try:
        x = a / b
        print(f"x = {x}")
    except ZeroDivisionError:
        print("Không chia được cho 0")
    except Exception as e:
        print(e)
    finally:
        print("Chương trình đã kiểm tra xong lỗi")

    print("CHương trình thành công ngon lành")

divide_numbers(10, 0)

"""
Bình thường làm bài => try và except tương ứng
"""