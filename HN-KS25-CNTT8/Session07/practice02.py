"""
STRING METHOD
"""

string_a = "hELlo, pytHon"

# string.method()
print(string_a.upper())
print(string_a.lower())
print(string_a.title())
print(string_a.capitalize())

# A in B? -> true/false
stringA = "Python Python"
stringB = "yt"

""" string.find(substring)
B1: kiểm tra xem B in A
B2: Tìm index
"""
print(stringA.find(stringB))

# string.count(substring)
print(stringA.count("P")) # 

# startswith, endswith
print(stringA.startswith("J"))
print(stringA.endswith("n"))

# Thay thế chuỗi 
a = "Ta Quang Tung"
print(a.replace("Ta", "Nguyen"))