def is_latin_lowercase_palindrome(text):
    latin_lowercase_chars = [char for char in text if 'a' <= char <= 'z']
    
    return latin_lowercase_chars == latin_lowercase_chars[::-1]

# Пример использования:
input_string = input("Введите строку: ")
if is_latin_lowercase_palindrome(input_string):
    print("Строчные латинские буквы образуют палиндром.")
else:
    print("Строчные латинские буквы не образуют палиндром.")
