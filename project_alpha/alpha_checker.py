def grade_day(day, seen_prac_subjects):
    daily_score = 0
    seen_theo_subjects = []
    how_many_tv = 0
    how_many_free = 0
    how_many_cit = 0

    for index, subject in enumerate(day):
        if subject.shortcut != "X":

            if subject.shortcut == "CIT":
                how_many_cit += 1

            # Check if the classroom floor matches the teacher's cabinet floor
            daily_score += 20 if subject.get_classroom().classroom_floor == subject.get_teacher().cabinet_floor else -20

            if subject.is_practical:
                # Check for duplicate practical subjects
                if subject.shortcut not in seen_prac_subjects:
                    seen_prac_subjects.append(subject.shortcut)
                else:
                    daily_score -= 10  # Deduct score for duplicate practical subjects

                # Check for practical lessons without a theoretical counterpart
                if subject.need_theoretical and index + 1 < len(day) and not day[index + 1].is_practical:
                    daily_score -= 20  # Deduct score for missing theoretical lesson in a practical pair

                # Check for more than two practical lessons of the same subject
                if seen_prac_subjects.count(subject.shortcut) > 2:
                    daily_score -= 30  # Deduct score for more than two practical lessons of the same subject

                # Check for one practical theoretical lesson before the two practical ones
                if index - 1 >= 0 and not day[index - 1].is_practical and day[index - 1].need_theoretical:
                    daily_score += 15  # Increase score for one practical theoretical lesson before two practical ones
            else:
                # Check for duplicate non-practical subjects
                if subject.shortcut not in seen_theo_subjects:
                    seen_theo_subjects.append(subject.shortcut)
                else:
                    daily_score -= 50  # Deduct more score for duplicate non-practical subjects
        else:
            how_many_free += 1
            # Bonus for the first "X" subject in the day
            daily_score += 10 if index == 0 else 5

            # Deduct score for profile subjects after the 5th lesson
            if how_many_free >= 2 and index > 5 and subject.is_profile:
                daily_score -= 15

    # Penalty for having the same theoretical subjects in one day
    daily_score -= 5 * (len(seen_theo_subjects) - len(set(seen_theo_subjects)))

    # Bonus for having two practical lessons of the same subject next to each other
    for index in range(1, len(day)):
        if day[index - 1].is_practical and day[index].is_practical and day[index - 1].shortcut == day[index].shortcut:
            daily_score += 15

    # Bonus based on the number of lessons in the day
    if len(day) <= 7:
        daily_score += 15
    else:
        daily_score -= 5

    return [daily_score, seen_prac_subjects, how_many_tv, how_many_cit]


def grade_week(week):
    final_week_score = 0
    seen_prac_sub_in_week = []
    final_tv_count = 0
    final_cit_count = 0

    for day in week:
        graded_day = grade_day(day, seen_prac_sub_in_week)
        final_week_score += graded_day[0]
        seen_prac_sub_in_week.extend(graded_day[1])
        final_tv_count += graded_day[2]
        final_cit_count += graded_day[3]

    # Bonus for meeting the TV count requirement
    final_week_score += 20 if final_tv_count == 2 else -30
    final_week_score += 20 if final_cit_count == 2 else -30

    return final_week_score