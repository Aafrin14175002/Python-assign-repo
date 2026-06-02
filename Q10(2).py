#movement.py

def decide_movement(sensors):

    if all(x == 0 for x in sensors):
        return "Stop Robot"

    elif all(x == 1 for x in sensors):
        return "Junction Detected"

    elif sensors[2] == 1 or sensors[3] == 1:
        return "Move Forward"

    elif sensors[0] == 1 or sensors[1] == 1:
        return "Turn Left"

    elif sensors[4] == 1 or sensors[5] == 1:
        return "Turn Right"

    else:
        return "No Action"
