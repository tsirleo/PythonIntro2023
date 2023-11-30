from decimal import getcontext
from decimal import Decimal


def gauss_area(x1, y1, x2, y2, x3, y3):
    return abs(x1*y2 + x2*y3 + x3*y1 - (y1*x2 + y2*x3 + y3*x1)) * Decimal(0.5)


input_data = input()
if '.' in input_data:
    accuracy = 1
    for number in input_data.split(','):
        if '.' in number:
            accuracy = len(number[number.find('.') + 1:]) * 2
    getcontext().prec = accuracy * 4
    coordinates = [Decimal(coord) for coord in input_data.split(',')]
    area = gauss_area(coordinates[0], coordinates[1], coordinates[2], coordinates[3], coordinates[4], coordinates[5])
    print(Decimal(round(area, accuracy)).normalize())
else:
    accuracy = round(len(input_data) / 6)
    getcontext().prec = accuracy * 4
    coordinates = [Decimal(coord) for coord in input_data.split(',')]
    area = gauss_area(coordinates[0], coordinates[1], coordinates[2], coordinates[3], coordinates[4], coordinates[5])
    print(round(area))
