from alpha_generator import generate_schedule

week = generate_schedule()

for i in range(len(week)):
    print("Day", i + 1, end=": ")
    for subject in week[i]:
        print(subject, end=' ')

        # Check if the subject has an assigned teacher
        if hasattr(subject, 'assigned_teacher') and subject.get_teacher():
            print(subject.get_teacher().name_shortcut, end=' ')
        else:
            print("No teacher assigned", end=' ')

    print("\n")