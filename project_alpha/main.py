from alpha_generator import generate_schedule

week = generate_schedule()

for i in range(len(week)):
    print("Day", i + 1, end=": ")
    for subject in week[i]:
        print(subject, end=' ')
    print("\n")
