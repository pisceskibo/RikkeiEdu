""" TIÊU CHUẨN PEP8:
Tên hàm + tên biến => snake_case
Tên class => PascalCase (giống phương thức .title() của bài string)
Các hằng số, các giá trị cụ thể => viết in HOA hết
"""

MY_SCHOOL = "PTIT"
SO_PI = 3.14

class MyStudent:
    def get_all_student(name: str, dob: int, score: float) -> str:
        name_student = name + "01"
        age_student = 2026 - dob
        score_student = score / 100

        return f"Học sinh {name_student} có tuổi là {age_student} và điểm số là {score_student}"