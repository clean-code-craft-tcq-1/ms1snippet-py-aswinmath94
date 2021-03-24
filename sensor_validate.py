tolerance_limit = {'soc': 0.05, 'current': 0.1}


def in_max_tolerence_limit(value, nextValue, maxDelta):
    if nextValue - value > maxDelta:
        return False
    return True


def validate_sensor_reading(values, parameter_type):
    last_but_one_reading = len(values) - 1
    for i in range(last_but_one_reading):
        if (not in_max_tolerence_limit(values[i], values[i + 1], tolerance_limit[parameter_type])):
            return False
    return True

def validate_sensor_reading_if_value_not_none(value,parameter_type):
    value_length = len(value)
    if value_length !=0:
        validate_sensor_reading(value,parameter_type)
    else:
        print('Received Empty Value List; Validation not possible')
