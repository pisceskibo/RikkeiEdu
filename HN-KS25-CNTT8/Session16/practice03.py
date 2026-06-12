"""str.format_map() - Template Động"""
information_string = "Hello {name}, i am a student in {school}"

# Định nghĩa quy tắc
key_dictionary = {
    "name": "Tung",
    "school": "PTIT"
}

formatted_information = information_string.format_map(key_dictionary)
print(formatted_information)

# makestran, translate => giúp ích cho việc chỉnh sửa chính tả
text = "Hêllo Tùng, Mý schôl is PTIT"
table = str.maketrans(
    "êùýô",         # Các ký tự muốn đổi
    "euyo",         # Các ký tự sau khi đổi
)
new_text = text.translate(table)
print(new_text)