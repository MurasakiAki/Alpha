from lessons import lesson
from classrooms import classroom
from teachers import teacher
import random

teachers = [
    teacher("Mgr.", "Libuše", "Hrabalová", "Hr", 4, "M"),
    teacher("Ing.", "Antonín", "Vobecký", "Vc", 2, "DS", "PV"),
    teacher("", "Jan", "Molič", "Mo", 2, "PSS", "WA"),
    teacher("Ing.", "Lukáš", "Masopust", "Ms", 2, "PSS", "WA", "IT", "TP"),
    teacher("Ing.", "Tomáš", "Juchelka", "Ju", 1, "A"),
    teacher("Mgr.", "Pavel", "Lopocha", "Lc", 0, "TV"),
    teacher("Ing.", "Lucie", "Brčáková", "Bc", 1, "PIS", "EK", "ZSV"),
    teacher("Ing.", "Jaroslav", "Benda", "Bd", 2, "CIT", "PIS"),
    teacher("MUDr.", "Kristina", "Studénková", "Su", 2, "C", "D"),
    teacher("Ing. Mgr.", "Vladimír", "Váňa", "Vd", 2, "CIT", "EP"),
    teacher("Mgr.", "Jakub", "Mazuch", "Mz", 2, "CIT", "TI", "IT", "M"),
    teacher("", "Daniel", "Adámek", "Ad", 2, "IT", "WA"),
    teacher("Mgr.", "Alena", "Reichlová", "Re", 1, "PV", "IT", "MVH"),
    teacher("Ing.", "Filip", "Kallmünzer", "Kl", 2, "F", "M", "AM"),
    teacher("Mgr.", "Simona", "Hemžalová", "Hs", 1, "IT", "A", "WA"),
    teacher("Ing. Bc.", "Šárka", "Paltíková", "Pa", 2, "A"),
    teacher("Ing.", "Ondřej", "Mandík", "Ma", 1, "PV"),
    teacher("", "", "", "", 0, "X")
]

gym = classroom("TV", 0, False)

classrooms = [
    classroom("25", 4, False),
    classroom("19", 3, True),
    classroom("8", 2, True),
    classroom("29", 4, False),
    classroom("17", 3, True),
    classroom("26", 3, False),
    classroom("18", 3, True),
    classroom("5", 1, False)
]

free_lesson = lesson("Volná hodina/Oběd", "X", False, False, False)

subjects = [
    lesson("Český jazyk", "C", False, False, True),
    lesson("Matematika", "M", False, False, True),
    lesson("Aplikovaná matematika", "AM", False, False, False),
    lesson("Počítačové systémy a sítě", "PSS", True, True, False),
    lesson("Databázové systémy", "DS", True, True, False),
    lesson("Webové aplikace", "WA", True, True, False),
    lesson("Programové vybavení", "PV", True, True, False),
    lesson("Cvičení ze správy IT", "CIT", True, False, False),
    lesson("Anglický jazyk", "A", False, False, True),
    lesson("Technický projekt", "TP", False, False, False),
    lesson("Tělesná výchova", "TV", False, False, False)
]

def generate_schedule():
    week = []

    for _ in range(5):
        number_of_subjects = random.randint(5, 10)
        when_begin = random.randint(0, 1)
        has_lunch = number_of_subjects == 5

        day = []
        for i in range(number_of_subjects):
            if i == 0 and when_begin == 1 or (len(day) > 4 and random.randint(0, 1)):
                day.append(free_lesson)
                has_lunch = True
            else:
                sub_to_append = subjects[random.randint(0, len(subjects) - 1)]
                while sub_to_append.is_profile and len(day) == 0:
                    sub_to_append = subjects[random.randint(0, len(subjects) - 1)]
                day.append(sub_to_append)

        if day and day[-1].shortcut == "X":
            day.pop()

        day = join_practical(day)
        add_classrooms(day)
        add_teachers(day)
        week.append(day)

    return week

def join_practical(day):
    seen_shortcuts = set()
    result_day = []

    for subject in day:
        if subject.is_practical:
            if subject.shortcut in seen_shortcuts:
                index = max(i for i, subj in enumerate(result_day) if subj.shortcut == subject.shortcut)
                result_day.insert(index + 1, subject)
            else:
                result_day.append(subject)
        else:
            seen_shortcuts.add(subject.shortcut)
            result_day.append(subject)

    return result_day

def get_random_lab_classroom(classrooms):
    lab_classrooms = [classroom for classroom in classrooms if classroom.is_lab]
    return random.choice(lab_classrooms) if lab_classrooms else None

def get_random_theo_classroom(classrooms):
    theo_classrooms = [classroom for classroom in classrooms if not classroom.is_lab]
    return random.choice(theo_classrooms) if theo_classrooms else None

def add_classrooms(day):
    lab_classroom = get_random_lab_classroom(classrooms)
    theo_classroom = get_random_theo_classroom(classrooms)

    for subject in day:
        subject.set_classroom(lab_classroom) if subject.is_practical else subject.set_classroom(theo_classroom)

def add_teachers(day):
    for subject in day:
        suitable_teachers = [t for t in teachers if subject.shortcut in t.professions]
        if suitable_teachers:
            assigned_teacher = random.choice(suitable_teachers)
            subject.set_teacher(assigned_teacher)

def print_schedule(week):
    for i, day in enumerate(week, start=1):
        print("Day", i, end=": ")
        for subject in day:
            print(subject, end=' ')
        print()