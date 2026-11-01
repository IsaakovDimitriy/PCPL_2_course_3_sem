# Класс университета
class University:
    def __init__(self, id, name):
        self.id = id        # Первичный ключ университета
        self.name = name    # Название университета


# Класс факультета
class Faculty:
    def __init__(self, id, name, budget, university_id):
        self.id = id                        # Первичный ключ факультета
        self.name = name                    # Название факультета
        self.budget = budget                # Бюджет факультета
        self.university_id = university_id  # Внешний ключ на университет


# Класс связи многие ко многим
class FacultyUniversity:
    def __init__(self, faculty_id, university_id):
        self.faculty_id = faculty_id        # Внешний ключ на факультет
        self.university_id = university_id  # Внешний ключ на университет


def main():
    # Создаем университеты
    universities = [
        University(1, "Северный университет"),
        University(2, "Центральный университет"),
        University(3, "Южный университет")
    ]

    # Создаем факультеты
    # Последнее число — ID университета, к которому относится факультет.
    # Это связь один-ко-многим.
    faculties = [
        Faculty(1, "Архитектурный", 1200000, 1),
        Faculty(2, "Математический", 800000, 1),
        Faculty(3, "Авиационный", 950000, 2),
        Faculty(4, "Физический", 1100000, 3),
        Faculty(5, "Экономический", 700000, 2)
    ]

    # Для связи многие ко многим используем отдельный список.
    # Факультет с ID 1 связан сразу с университетами 1 и 2.
    relations = [
        FacultyUniversity(1, 1),
        FacultyUniversity(1, 2),
        FacultyUniversity(2, 1),
        FacultyUniversity(3, 2),
        FacultyUniversity(4, 3),
        FacultyUniversity(5, 2)
    ]

    # Словари помогают найти объект по его ID.
    university_dict = {u.id: u for u in universities}
    faculty_dict = {f.id: f for f in faculties}

    # ЗАПРОС 1
    # Факультеты на букву «А» и университеты, к которым они относятся.
    # Здесь используется связь один-ко-многим.
    query1 = [
        (f.name, university_dict[f.university_id].name)
        for f in faculties
        if f.name.startswith("А")
    ]

    print("ЗАПРОС 1. Факультеты на букву А:")
    for faculty_name, university_name in query1:
        print(faculty_name, "—", university_name)

    # ЗАПРОС 2
    # Минимальный бюджет факультета в каждом университете.
    query2 = []
    for u in universities:
        # Собираем бюджеты факультетов данного университета.
        budgets = [f.budget for f in faculties if f.university_id == u.id]
        if budgets:  # Проверка нужна, чтобы min() не получил пустой список.
            query2.append((u.name, min(budgets)))

    # Сортировка по бюджету (второй элемент пары).
    query2 = sorted(query2, key=lambda x: x[1])

    print("\nЗАПРОС 2. Минимальный бюджет по университетам:")
    for university_name, budget in query2:
        print(university_name, "—", budget, "руб.")

    # ЗАПРОС 3
    # Все пары «Факультет — Университет» по связи многие ко многим.
    query3 = [
        (faculty_dict[r.faculty_id].name, university_dict[r.university_id].name)
        for r in relations
    ]

    # Сортировка по названию факультета (первый элемент пары).
    query3 = sorted(query3, key=lambda x: x[0])

    print("\nЗАПРОС 3. Связь многие ко многим:")
    for faculty_name, university_name in query3:
        print(faculty_name, "—", university_name)


# Запускаем главную функцию программы.
if __name__ == "__main__":
    main()
