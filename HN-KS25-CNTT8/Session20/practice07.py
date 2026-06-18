# Unit test
def caculation_discount(price: float, rate: float) -> float:
    if price < 0:
        raise ValueError("Giá tiền không được âm")
    
    return price * (1 - rate)

# Viết unit test
"""
Tải thư viện => pip install <tên thư viện>
"""
import pytest

def test_happy_case():
    assert caculation_discount(100, 0.1) == 90.0

def test_bad_case():
    with pytest.raises(ValueError):
        caculation_discount(-10, 0.1)