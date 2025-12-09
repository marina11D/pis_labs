groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Мария",
        "surname": "Соколова",
        "exams": ["Физика", "АиГ", "ОБЖ"],
        "marks": [3, 4, 5]
    },
    {
        "name": "Олег",
        "surname": "Орлов",
        "exams": ["Информатика", "КТП", "Web"],
        "marks": [2, 3, 4]
    }
]

def print_students(students): #функция для вывода списка всех студентов
    print("Имя".ljust(15), "Фамилия".ljust(10), "Экзамены".ljust(30), "Оценки".ljust(20))
    # ljust – метод строки, используется для выравнивания строк, добавляя пробелы
    for student in students:
        print(
            student["name"].ljust(15),
            student["surname"].ljust(10),
            str(student["exams"]).ljust(30),
            str(student["marks"]).ljust(20)
        )

def filter_by_average(students, min_avg): #функция для фильтрации студентов по средней оценке
    filtered = []
    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])
        if avg >= min_avg:
            filtered.append(student)
    return filtered
