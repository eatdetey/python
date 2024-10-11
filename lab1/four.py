import re

def find_dates(text):
    # Регулярное выражение для поиска дат в формате "день.месяц.год"
    date_pattern = r'\b(0?[1-9]|[12][0-9]|3[01])\.(0?[1-9]|1[0-2])\.(\d{4})\b'
    
    # Поиск всех совпадений в тексте
    dates = re.findall(date_pattern, text)
    
    # Преобразуем к форматированному виду (например, '01.12.2023')
    formatted_dates = [".".join(date) for date in dates]
    
    return formatted_dates

# Пример использования:
input_text = input("Введите текст: ")
found_dates = find_dates(input_text)
print("Найденные даты:", found_dates)
