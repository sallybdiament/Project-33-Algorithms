# [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5), (6, 7)]

# target_time de 1 a 7.
# target_time = 5 ---> resultado: 3

def study_schedule(permanence_period, target_time):
    for p in permanence_period:
        if type(p[0]) != int or type(p[1]) != int:
            return None

    if target_time is None:
        return None
    
    quantity_students = 0
    for p in permanence_period:
        if p[0] <= target_time and target_time <= p[1]:
            quantity_students += 1
    
    return quantity_students
    