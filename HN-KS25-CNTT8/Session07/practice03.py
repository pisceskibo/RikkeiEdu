"""
STRING FORMAT
"""

# Format String
name = "Tung"
name_class = "Python"

# Định dạng "Tôi là Tung, học lớp Python"
print("Tôi là " + name + ", học lớp Python")
print(f"Tôi là {name}, học lớp Python")
print("Tôi là {}, học lớp {}".format(name, name_class))
print("Tôi là %s, học lớp %s" % (name, name_class))