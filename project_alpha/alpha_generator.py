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
    lesson("Tělesná výchova", "TV", True, False, False)
]

def join_practical(day):
    seen_shortcuts = set()
    result_day = []
    practical_subjects = []

    for subject in day:
        if subject.is_practical:
            if any(practical.shortcut == subject.shortcut for practical in practical_subjects):
                index = practical_subjects.index(next(practical for practical in practical_subjects if practical.shortcut == subject.shortcut))
                practical_subjects.insert(index + 1, subject)
            else:
                practical_subjects.append(subject)
        elif subject.shortcut in seen_shortcuts:
            index = result_day.index(subject)
            result_day.insert(index + 1, subject)
        else:
            seen_shortcuts.add(subject.shortcut)
            result_day.append(subject)

    result_day.extend(practical_subjects)

    return result_day

def get_random_lab_classroom(classrooms):
    lab_classrooms = [classroom for classroom in classrooms if classroom.is_lab]
    if lab_classrooms:
        return random.choice(lab_classrooms)
    else:
        return None

def get_random_theo_classroom(classrooms):
    theo_classrooms = [classroom for classroom in classrooms if not classroom.is_lab]
    if theo_classrooms:
        return random.choice(theo_classrooms)
    else:
        return None

def add_classrooms(day):
    for subject in day:
        index = day.index(subject)
        try:
            if subject.is_practical and subject.shortcut == day[index + 1].shortcut:
                subject.set_classroom(get_random_lab_classroom(classrooms))
            else:
                subject.set_classroom(get_random_theo_classroom(classrooms))
        except:
            subject.set_classroom(get_random_theo_classroom(classrooms))
            
def add_teachers(day):
    for index, subject in enumerate(day):
        suitable_teachers = []

        for teacher in teachers:
            if subject.shortcut in teacher.professions:
                suitable_teachers.append(teacher)

        if suitable_teachers:
            assigned_teacher = random.choice(suitable_teachers)
            subject.set_teacher(assigned_teacher)

            try:
                if subject.is_practical and subject.shortcut == day[index + 1].shortcut:
                    day[index + 1].set_teacher(assigned_teacher)
            except:
                pass
def generate_schedule():

    monday = []
    tuesday = []
    wednesday = []
    thursday = []
    friday = []

    week = [monday, tuesday, wednesday, thursday, friday]

    for day in week:
        number_of_subjects = random.randint(5, 10)
        when_begin = random.randint(0, 1)
        has_lunch = False
        if number_of_subjects == 5:
            has_lunch = True
        for i in range(number_of_subjects):
            if i == 0 and when_begin == 1:
                day.append(free_lesson)
            else:
                if len(day) == 7:
                    if not has_lunch:
                        day.append(free_lesson)
                        has_lunch = True
                if len(day) > 4 and random.randint(0, 1):
                    if not has_lunch:
                        day.append(free_lesson)
                        has_lunch = True
                else:
                    if len(day) == 0:
                        sub_to_append = subjects[random.randint(0, len(subjects) - 1)]
                        while sub_to_append.is_profile:
                            sub_to_append = subjects[random.randint(0, len(subjects) - 1)]
                        day.append(sub_to_append)
                    else:
                        day.append(subjects[random.randint(0, len(subjects) - 1)])

        if day[len(day) - 1].shortcut == "X":
            day.pop()
        
        day = join_practical(day)
        
        add_classrooms(day)
        add_teachers(day)
    
    return week