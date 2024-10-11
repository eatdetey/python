import re

def find_max_float(text):
    # Регулярное выражение для поиска вещественных чисел
    float_pattern = r'-?\d+\.\d+'
    
    # Поиск всех вещественных чисел в тексте
    floats = re.findall(float_pattern, text)
    
    # Преобразуем найденные строки в числа с плавающей точкой
    floats = [float(num) for num in floats]
    
    # Если числа найдены, возвращаем максимальное, иначе None
    return max(floats) if floats else None

# Пример использования
input_text = input("Введите строку с вещественными числами: ")
max_float = find_max_float(input_text)
if max_float is not None:
    print("Максимальное вещественное число:", max_float)
else:
    print("В строке нет вещественных чисел.")
