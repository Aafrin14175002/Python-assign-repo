#sensors.py
def read_sensors():
    data = input("Enter 6 sensor values (e.g. 001100): ")

    sensors = list(map(int, data))

    active = len(list(filter(lambda x: x == 1, sensors)))

    return sensors, active

