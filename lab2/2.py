def find_country_for_cities(country_city_map, city_names):
    # Для каждого города найдем страну
    results = {}
    for city in city_names:
        if city in country_city_map:
            results[city] = country_city_map[city]
        else:
            results[city] = "Unknown"  # Если город не найден
    return results

# Задаем список стран и городов
country_city_map = {
    "Москва": "Россия",
    "Санкт-Петербург": "Россия",
    "Новосибирск": "Россия",
    "Нью-Йорк": "США",
    "Лос-Анджелес": "США",
    "Чикаго": "США",
    "Токио": "Япония",
    "Сидней": "Австралия",
    "Лондон": "Великобритания",
    "Париж": "Франция",
}

# Чтение названий городов для поиска
city_names = []
while True:
    city_name = input("Введите название города для поиска (или пустую строку для завершения): ")
    if not city_name:
        break
    city_names.append(city_name)

# Получение и вывод стран для введенных городов
results = find_country_for_cities(country_city_map, city_names)

for city, country in results.items():
    print(f"{city}: {country}")
