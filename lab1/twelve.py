def avg_consonant_vowel_diff(string):
    vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"  # Список гласных латиницы и кириллицы
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZбвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
    
    vowel_count = sum(1 for char in string if char in vowels)
    consonant_count = sum(1 for char in string if char in consonants)
    
    if len(string) == 0:
        return 0  # Если строка пустая, то разница 0
    
    avg_vowels = vowel_count / len(string)
    avg_consonants = consonant_count / len(string)
    
    return abs(avg_consonants - avg_vowels)

def sort_by_avg_consonant_vowel_diff(strings):
    return sorted(strings, key=avg_consonant_vowel_diff)

# Пример использования:
strings = ["hello", "world", "example", "text"]
sorted_strings = sort_by_avg_consonant_vowel_diff(strings)
print("Строки, отсортированные по разнице между средним количеством согласных и гласных:", sorted_strings)
