def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    quantity_students = 0
    for p in permanence_period:
        if type(p[0]) != int or type(p[1]) != int:
            return None
        if p[0] <= target_time and target_time <= p[1]:
            quantity_students += 1

    return quantity_students
