from collections import Counter

def sort_by_frequency(arr):
    # Подсчет количества каждого элемента
    counter = Counter(arr)
    
    # Сортировка по убыванию частоты, при равной частоте - по значению элемента
    return sorted(arr, key=lambda x: (-counter[x], x))

# Пример использования
arr = [5, 6, 2, 2, 3, 3, 3, 5, 5, 5]
sorted_arr = sort_by_frequency(arr)
print("Новый список, упорядоченный по частоте:", sorted_arr)
