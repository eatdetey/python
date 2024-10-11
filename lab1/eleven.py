def count_words_in_string(s):
    # Подсчет количества слов в строке
    return len(s.split())

def sort_by_word_count(strings):
    # Сортировка по количеству слов в строке
    return sorted(strings, key=count_words_in_string)

# Пример использования
input_list = input("Введите строки через запятую: ").split(', ')
sorted_by_words = sort_by_word_count(input_list)
print("Отсортированный список по количеству слов в строке:", sorted_by_words)
