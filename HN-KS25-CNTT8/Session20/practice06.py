import logging

"""
logging được config từ đầu
"""
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)
logger = logging.getLogger(__name__)

# Bảng cửu chương
for i in range(2, 10):
    print(f"Bảng số {i}")
    for j in range(1, 11):
        result = i * j

        logger.warning(f"result = {result}")
        print("WARNING: result = ")
"""
Hạn chế sử dụng print()
"""
