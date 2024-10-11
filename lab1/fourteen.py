def avg_ascii_value(string):
    if len(string) == 0:
        return 0  # Если строка пустая, возвращаем 0
    return sum(ord(char) for char in string) / len(string)

def max_avg_triple_ascii(string):
    if len(string) < 3:
        return 0  # Если в строке меньше 3 символов, возвращаем 0
    max_avg = 0
    for i in range(len(string) - 2):
        triple_avg = sum(ord(string[i + j]) for j in range(3)) / 3
        max_avg = max(max_avg, triple_avg)
    return max_avg

def quadratic_deviation_from_max_triple(strings):
    def deviation(string):
        avg_ascii = avg_ascii_value(string)
        max_triple_avg = max_avg_triple_ascii(string)
        return (avg_ascii - max_triple_avg) ** 2
    
    return sorted(strings, key=deviation)

# Пример использования:
strings = ["hello", "world", "example", "text"]
sorted_strings = quadratic_deviation_from_max_triple(strings)
print("Строки, отсортированные по квадратичному отклонению от максимальной тройки символов:", sorted_strings)
