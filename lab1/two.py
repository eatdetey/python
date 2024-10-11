def count_russian_characters(text):
    count = 0
    for char in text:
        if 'А' <= char <= 'я' or char in 'Ёё':
            count += 1
    return count

input_string = input("Введите строку: ")
russian_chars_count = count_russian_characters(input_string)
print("Количество русских символов в строке:", russian_chars_count)
