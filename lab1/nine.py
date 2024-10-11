import re

def max_consecutive_numbers(text):
    # Регулярное выражение для поиска чисел (целые и вещественные)
    number_pattern = r'-?\d+(\.\d+)?'
    
    # Разбиваем строку по пробелам
    words = text.split()
    
    max_streak = 0
    current_streak = 0
    
    for word in words:
        if re.fullmatch(number_pattern, word):  # Если слово является числом
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0
    
    return max_streak

# Пример использования
input_text = input("Введите строку с числами: ")
max_streak = max_consecutive_numbers(input_text)
print("Наибольшее количество идущих подряд чисел:", max_streak)
