input_hour = int(input('Input hours: '))
input_minute = int(input('Input minutes: '))

def calc_angle(hour, minute):
    if hour in range (12, 23):
        hour -= 12
    if hour >= 24 or hour < 0:
        print('Input correct value!')
        return
    hour_angle = hour * 30
    if minute >= 60 or minute < 0:
        print('Input correct value!')
        return
    minute_angle = minute * 6
    new_hour_angle = hour_angle + (minute * 0.5)
    right_angle = abs(new_hour_angle - minute_angle)
    if right_angle >= 360:
        right_angle -= 360
    if right_angle > 180:
        right_angle = 360 - right_angle
    print(f'Minimal angle is {right_angle} degrees')

calc_angle(input_hour, input_minute)