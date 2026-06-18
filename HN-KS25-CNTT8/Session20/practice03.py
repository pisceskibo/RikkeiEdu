""" BẮT LỖI CÁC NGOẠI LỆ TRƯỚC
Ưu tiên bắt các ngoại lệ trước để tinh giản code lồng nhau
"""

# Tính toán điểm số 
def sum_of_score_01(math_score: float, physic_score: float, chemistry_score: float) -> float:
    # Cách viết tường minh
    if math_score > 0:
        if physic_score > 0:
            if chemistry_score:
                return math_score + physic_score + chemistry_score
            else:
                return "Điểm môn hóa không được nhỏ hơn 0"
        else:
            return "Điểm mô lý không được nhỏ hơn 0"
    else:
        return "Điểm môn toán không được nhỏ hơn 0"

def sum_of_score_02(math_score: float, physic_score: float, chemistry_score: float) -> float:
    # Bắt các ngoại lệ trước
    if math_score < 0:
        return "Điểm môn toán không được nhỏ hơn 0"

    if physic_score < 0:
        return "Điểm mô lý không được nhỏ hơn 0"
    
    if chemistry_score < 0:
        return "Điểm môn hóa không được nhỏ hơn 0"
    
    return math_score + physic_score + chemistry_score
    
"""
Giải pháp: dùng toán tử so sánh => and, or, >, <, ..
"""