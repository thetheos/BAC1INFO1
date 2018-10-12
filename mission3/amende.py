def fine(authorized_speed, actual_speed):
    if actual_speed - authorized_speed > 10:
        return (actual_speed - authorized_speed) * 5 * 2
    elif actual_speed - authorized_speed < 3:
        return 12.5
    else:
        return (actual_speed - authorized_speed) * 5
    return 0

print(fine(50,62))