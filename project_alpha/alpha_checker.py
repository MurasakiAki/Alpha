def grade_day(day, seen_prac_subjects):
    score = 0
    seen_theo_subjects = []

    for index, subject in enumerate(day):
        if subject.shortcut != "X":
            if subject.get_classroom().classroom_floor == subject.get_teacher().cabinet_floor:
                score += 20
            else:
                score -= 20

            if subject.is_practical:
                # Check for duplicate practical subjects
                if subject.shortcut not in seen_prac_subjects:
                    seen_prac_subjects.append(subject.shortcut)
                else:
                    score -= 10  # Deduct score for duplicate practical subjects

                # Check for practical lessons without a theoretical counterpart
                if subject.need_theoretical and index + 1 < len(day) and not day[index + 1].is_practical:
                    score -= 20  # Deduct score for missing theoretical lesson in a practical pair

                # Check for more than two practical lessons of the same subject
                if seen_prac_subjects.count(subject.shortcut) > 2:
                    score -= 30  # Deduct score for more than two practical lessons of the same subject

                # Check for one practical theoretical lesson before the two practical ones
                if (
                    index - 1 >= 0
                    and not day[index - 1].is_practical
                    and day[index - 1].need_theoretical
                ):
                    score += 15  # Increase score for one practical theoretical lesson before two practical ones

            else:
                # Check for duplicate non-practical subjects
                if subject.shortcut not in seen_theo_subjects:
                    seen_theo_subjects.append(subject.shortcut)
                else:
                    score -= 10  # Deduct score for duplicate non-practical subjects
        else:
            if index == 0:
                score += 100
            else:
                score += 50
            
            if index > 5 and subject.is_profile:
                score -= 5

    if len(day) == 5:
        score += 20
    elif len(day) == 6:
        score += 10
    elif len(day) == 7:
        score += 5
    else:
        score -= 10 

    return [score, seen_prac_subjects]

def grade_week(week):
    final_week_score = 0
    seen_prac_sub_in_week = []
    for day in week:
       graded_day = grade_day(day, seen_prac_sub_in_week)
       final_week_score += graded_day[0]
       seen_prac_sub_in_week.extend(graded_day[1])
    
    return final_week_score
    #my checks