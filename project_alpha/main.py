from alpha_generator import generate_schedule
from alpha_checker import grade_week

'''
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

print(grade_week(week))
'''

best_week = []

for i in range(1000):
    week = generate_schedule()
    week_score = grade_week(week)
    if i == 0:
        best_week.append(week)
        best_week.append(week_score)
    else:
        if best_week[1] < week_score:
            best_week[0] = week
            best_week[1] = week_score

for i in range(len(best_week[0])):
    print("Day", i + 1, end=": ")
    for subject in best_week[0][i]:
        print(subject, end=' ')
    print("\n")

print(best_week[1])