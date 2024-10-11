def avg_ascii_value(string):
    if len(string) == 0:
        return 0  # Если строка пустая, возвращаем 0
    return sum(ord(char) for char in string) / len(string)

def quadratic_deviation_from_first(strings):
    first_avg_ascii = avg_ascii_value(strings[0])
    
    def deviation(string):
        avg_ascii = avg_ascii_value(string)
        return (avg_ascii - first_avg_ascii) ** 2
    
    return sorted(strings, key=deviation)

# Пример использования:
strings = ["hello", "world", "example", "text"]
sorted_strings = quadratic_deviation_from_first(strings)
print("Строки, отсортированные по квадратичному отклонению от первой строки:", sorted_strings)
