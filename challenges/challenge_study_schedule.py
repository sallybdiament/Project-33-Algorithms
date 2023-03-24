def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    for p in permanence_period:
        if type(p[0]) != int or type(p[1]) != int:
            return None
    