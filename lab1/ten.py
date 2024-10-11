def sort_by_length(strings):
    # Сортировка списка строк по длине
    return sorted(strings, key=len)

# Пример использования
input_list = input("Введите строки через запятую: ").split(', ')
sorted_list = sort_by_length(input_list)
print("Отсортированный список по длине строки:", sorted_list)
