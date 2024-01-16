import pandas as pd
import numpy as np

# Load the CSV data
data = pd.read_csv('./fkcalibrate.csv')


# Define a function to find the closest XYZ match
def find_closest_match(desired_x, desired_y, desired_z):
    # Calculate Euclidean distance for each row
    data['distance'] = np.sqrt(
        (data['xA'] - desired_x) ** 2 + (data['yA'] - desired_y) ** 2 + (data['zA'] - desired_z) ** 2)

    # Find the row with the smallest distance
    closest_row = data.loc[data['distance'].idxmin()]

    # Retrieve servo values from the closest row
    servo1 = closest_row['servo1']
    servo2 = closest_row['servo2']
    servo3 = closest_row['servo3']

    return servo1, servo2, servo3


# Example usage
desired_x = 1  # Replace with your desired X value
desired_y = -8  # Replace with your desired Y value 1.23,-8.94,14.98
desired_z = 14  # Replace with your desired Z value -8.28,-0.92,14.98

servo1_result, servo2_result, servo3_result = find_closest_match(desired_x, desired_y, desired_z)
print(f"Closest Servo Values - Servo1: {servo1_result}, Servo2: {servo2_result}, Servo3: {servo3_result}")
