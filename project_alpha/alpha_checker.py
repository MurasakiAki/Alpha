def grade_day(day, seen_prac_subjects):
    daily_score = 0
    seen_theo_subjects = set()
    how_many_tv = 0
    how_many_free = 0

    for index, subject in enumerate(day):
        if subject.shortcut != "X":
            if subject.shortcut == "CIT":
                how_many_tv += 1

            daily_score += 20 if subject.get_classroom().classroom_floor == subject.get_teacher().cabinet_floor else -20

            if subject.is_practical:
                if subject.shortcut not in seen_prac_subjects:
                    seen_prac_subjects.add(subject.shortcut)
                else:
                    daily_score -= 10

                if subject.need_theoretical and index + 1 < len(day) and not day[index + 1].is_practical:
                    daily_score -= 20

                if len([s for s in seen_prac_subjects if s == subject.shortcut]) > 2:
                    daily_score -= 30

                if index - 1 >= 0 and not day[index - 1].is_practical and day[index - 1].need_theoretical:
                    daily_score += 15
            else:
                if subject.shortcut not in seen_theo_subjects:
                    seen_theo_subjects.add(subject.shortcut)
                else:
                    daily_score -= 50
        else:
            how_many_free += 1
            daily_score += 10 if index == 0 else 5

            if how_many_free >= 2 and index > 5 and subject.is_profile:
                daily_score -= 15

    daily_score -= 25 * (len(seen_theo_subjects) - len(seen_theo_subjects))

    for index in range(1, len(day)):
        if day[index - 1].is_practical and day[index].is_practical and day[index - 1].shortcut == day[index].shortcut:
            daily_score += 30

    if len(day) <= 7:
        daily_score += 15
    else:
        daily_score -= 5

    return [daily_score, how_many_tv]


def grade_week(week):
    final_week_score = 0
    seen_prac_sub_in_week = set()
    final_tv_count = 0

    for day in week:
        graded_day = grade_day(day, seen_prac_sub_in_week)
        final_week_score += graded_day[0]
        
        if isinstance(graded_day[1], list):
            seen_prac_sub_in_week.update(graded_day[1])
            
        final_tv_count += graded_day[1]

    final_week_score += 20 if final_tv_count == 2 else -30

    return final_week_score
