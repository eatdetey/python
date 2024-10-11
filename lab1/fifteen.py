from collections import Counter

def most_common_char(strings):
    combined_text = ''.join(strings)
    counter = Counter(combined_text)
    most_common = counter.most_common(1)[0][0]
    return most_common

def frequency_of_char(string, char):
    return string.count(char) / len(string) if len(string) > 0 else 0

def quadratic_deviation_from_common_char(strings):
    common_char = most_common_char(strings)
    overall_frequency = frequency_of_char(''.join(strings), common_char)
    
    def deviation(string):
        string_frequency = frequency_of_char(string, common_char)
        return (string_frequency - overall_frequency) ** 2
    
    return sorted(strings, key=deviation)

# Пример использования:
strings = ["hello", "world", "example", "text"]
sorted_strings = quadratic_deviation_from_common_char(strings)
print("Строки, отсортированные по отклонению частоты самого распространённого символа:", sorted_strings)
