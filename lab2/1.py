def possible_numbers(n, questions):
    possible = set(range(1, n + 1))

    for question, answer in questions:
        question_set = set(map(int, question.split()))

        if answer == "YES":
            possible.intersection_update(question_set)
        elif answer == "NO":
            possible.difference_update(question_set)

    return sorted(possible)


n = int(input("Введите максимальное число n: "))
questions = []

while True:
    line = input("Введите вопрос и ответ (или пустую строку для завершения): ")
    if line.strip() == "":
        break
    question, answer = line.rsplit(maxsplit=1)
    questions.append((question, answer))

result = possible_numbers(n, questions)
print(" ".join(map(str, result)))
