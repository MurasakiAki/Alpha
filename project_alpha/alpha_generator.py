from lessons import lesson
from classrooms import classroom
from teachers import teacher
import random

monday = []
tuesday = []
wednesday = []
thursday = []
friday = []

week = [monday, tuesday, wednesday, thursday, friday]

teachers = [
    teacher("Mgr.", "Libuše", "Hrabalová", "Hr", 4, "M"),
    teacher("Ing.", "Antonín", "Vobecký", "Vc", 2, "DS", "PV"),
    teacher("", "Jan", "Molič", "Mo", 2, "PSS", "WA"),
    teacher("Ing.", "Lukáš", "Masopust", "Ms", 2, "PSS", "WA", "IT"),
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
    teacher("Ing.", "Ondřej", "Mandík", "Ma", 1, "PV")
]

classrooms = [
    classroom("25", 4, False),
    classroom("19", 3, True),
    classroom("8", 2, True),
    classroom("29", 4, False),
    classroom("17", 3, True),
    classroom("26", 3, False),
    classroom("TV", 0, False),
    classroom("18", 3, True),
    classroom("5", 1, False)
]

subjects = [
    lesson("Český jazyk", "C", False, False),
    lesson("Matematika", "M", False, False),
    lesson("Aplikovaná matematika", "AM", False, False),
    lesson("Počítačové systémy a sítě", "PSS", True, True),
    lesson("Databázové systémy", "DS", True, True),
    lesson("Webové aplikace", "WA", True, True),
    lesson("Programové vybavení", "PV", True, True),
    lesson("Cvičení ze správy IT", "CIT", True, False),
    lesson("Anglický jazyk", "A", False, False),
    lesson("Technický projekt", "TP", False, False),
    lesson("Tělesná výchova", "TV", False, False)
]

def generate_schedule():
    for day in week:
        number_of_subjects = random.randrange(5, 10)
        for i in range(number_of_subjects):
            day.append(subjects[random.randrange(0, len(subjects))])

def rate_schedule():
    score = 0

    for day in week:
        for subject in day:
            pass

generate_schedule()

for i in range(len(week)):
    print("Day", i + 1, end=": ")
    for subject in week[i]:
        print(subject, end=' ')
    print("\n")