import re

def find_text_dates(text):
    months = [
        'января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
        'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'
    ]
    
    date_pattern = r'\b([1-9]|[12][0-9]|3[01])\s+(' + '|'.join(months) + r')\s+(\d{4})\b'
    
    dates = re.findall(date_pattern, text)
    
    formatted_dates = [" ".join(date) for date in dates]
    
    return formatted_dates

input_text = input("Введите текст: ")
found_dates = find_text_dates(input_text)
print("Найденные даты:", found_dates)
