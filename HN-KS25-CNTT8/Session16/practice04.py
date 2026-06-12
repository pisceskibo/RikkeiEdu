students = [
    {
        "name": "Tung",
        "score": 9
    },
    {
        "name": "Quang",
        "score": 10
    },
    {
        "name": "Anh",
        "score": 7
    }
]

# Cách 1:
score_list = [] # Gồm những sinh viên có điểm > 8
for student in students:
    if student["score"] >= 8:
        score_list.append(student["name"])
print(score_list)

# Cách 2:
score_list = [student["name"] for student in students if student["score"] >= 8]
print(score_list)