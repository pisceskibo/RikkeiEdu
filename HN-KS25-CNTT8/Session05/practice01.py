"""
+ break: dừng vòng lặp ngay lập tức
+ continue: dừng lần lặp hiện tại của vòng lặp
"""

# Bài toán quy trình sản xuất
"""
Quy trình:
state01 -> state02 -> ... -> state05
"""

## Cách dùng break, continue
"""
Nhân viên sẽ có lương = lương gốc (12_000_000) + lương theo state
+ state chẵn => không cộng tiền thưởng
+ state lẻ => có tiền thưởng
"""

state = 1
cost = 0

while state > 0:
    state_name = f"State{state}"
    print(state_name)

    if state % 2 == 0:
        state += 1
        continue

    cost += 100_000
    if state == 5:
        break

    state += 1

print(f"Tiền thưởng theo state = {cost}")

"""
state lẻ: 1, 3, 5
=> cost = 100_000 + 100_000 + 100_000 = 300_000

"""

# In bảng cửu chương từ 2 -> 9
for i in range(2, 10):
    print(f"Bảng cửu chương {i}")
    for j in range(1, 10):
        print(f"{i}x{j}={i*j}")