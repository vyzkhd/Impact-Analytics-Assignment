import itertools


def is_allowed(attendance):
    consecutive_absent = 0
    temp = set()
    for i in attendance:
        if i not in temp:
            temp = set()
            temp.add(i)
            if i == 1:
                continue
            else:
                consecutive_absent = 1
        else:
            if i == 1:
                continue
            else:
                consecutive_absent += 1
                if consecutive_absent >= abs_limit:
                    return False
    return True 

def prob_miss_graduation(days, abs_limit):
    absent = 0
    present = 1
    options = [absent, present]

    attendance_combinations = [combination for combination in itertools.product(options, repeat=days)]
    allowed_combinations = [attendance for attendance in attendance_combinations if is_allowed(attendance)]
    miss_graduation = [attandence for attandence in allowed_combinations if attandence[-1] == 0]

    return f'{len(miss_graduation)}/{len(allowed_combinations)}'

if __name__ == '__main__':
    days = 10 # int(input().strip())
    abs_limit = 4 # int(input().strip())
    print(prob_miss_graduation(days, abs_limit))
    






