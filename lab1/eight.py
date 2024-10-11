import re

def find_min_rational(text):
    # Регулярное выражение для поиска целых (рациональных) чисел
    rational_pattern = r'-?\d+'
    
    # Поиск всех рациональных чисел в тексте
    rationals = re.findall(rational_pattern, text)
    
    # Преобразуем найденные строки в целые числа
    rationals = [int(num) for num in rationals]
    
    # Если числа найдены, возвращаем минимальное, иначе None
    return min(rationals) if rationals else None

# Пример использования
input_text = input("Введите строку с рациональными числами: ")
min_rational = find_min_rational(input_text)
if min_rational is not None:
    print("Минимальное рациональное число:", min_rational)
else:
    print("В строке нет рациональных чисел.")
