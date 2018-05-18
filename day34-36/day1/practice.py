days = 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split()
routines = 'Chest+biceps Back+triceps Core Legs Shoulders Rest Rest'.split()
workouts = dict(zip(days, routines))


def main():
    #rint(get_workout('Saturday'))
    #count_days(days)
    timings = '45 45 30 55 45'.split()
    workout_times = dict(zip(routines,timings))
    print(max(workout_times.items(), key=lambda  x: x[1]))

def get_workout_old(day):
    if day == 'Monday':
        return 'Chest+biceps'
    elif day == 'Tuesday':
        return 'Back+triceps'
    elif day == 'Wednesday':
        return 'Core'
    elif day == 'Thursday':
        return 'Legs'
    elif day == 'Friday':
        return 'Shoulders'
    elif day in ('Saturday', 'Sunday'):
        return 'Rest'
    raise ValueError('Not a day')

def get_workout(day):

    routine = workouts.get(day)
    if routine is None:
        raise ValueError('Not a day')
    return routine



def count_days(days):
    for i, day in enumerate(days, 1):
        print(f'{i}. {day}')
if __name__ == '__main__':
    main()