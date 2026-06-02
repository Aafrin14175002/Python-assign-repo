#main.py

from sensor import read_sensors
from movement import decide_movement

sensor_values, active_sensors = read_sensors()

action = decide_movement(sensor_values)

print("Sensor Values:", sensor_values)
print("Active Sensors:", active_sensors)
print("Robot Action:", action)
