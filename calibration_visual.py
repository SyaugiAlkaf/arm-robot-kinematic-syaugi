import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

# Function to simulate changes in measurements based on servo values
def generate_new_samples(servo_values):
    # Simulate changes based on servo values
    # Here, random changes are simulated for illustration purposes
    new_measurements = [val + random.uniform(-1, 1) for val in servo_values]
    return new_measurements

dataset = [
    # Data omitted for brevity, please paste your dataset here
    (0, 0, 0, -5.27, -1.48, 0),
    (20, 0, 0, -3.46, -3.18, 0),
    (40, 0, 0, -1.90, -4.42, 0),
    (60, 0, 0, -1.50, -4.15, 0),
    (80, 0, 0, 0.25, -5.76, 0),
    (120, 0, 0, 4.62, -4.43, 0),
    (160, 0, 0, 6.12, -0.87, 0),
    (180, 0, 0, 5.76, 0.54, 0),
    (0, 40, 0, -6.00, -1.56, 4.33),
    (40, 40, 0, -2.80, -5.25, 4.33),
    (80, 40, 0, 0.58, -7.15, 4.33),
    (120, 40, 0, 2.75, -5.15, 4.33),
    (160, 40, 0, 6.12, -1.05, 4.33),
    (0, 80, 0, -5.78, -0.98, 8.76),
    (40, 80, 0, -3.44, -5.76, 8.76),
    (80, 80, 0, 0.60, -7.05, 8.76),
    (120, 80, 0, 4.11, -4.31, 8.76),
    (160, 80, 0, 5.45, -1.02, 8.76),
    (0, 120, 0, -2.10, -0.97, 12.03),
    (40, 120, 0, -1.20, -1.68, 12.03),
    (80, 120, 0, 0.12, -3.47, 12.03),
    (120, 120, 0, 1.96, -2.17, 12.03),
    (160, 120, 0, 2.18, -0.96, 12.03),
    (0, 140, 0, -1.06, -1.29, 13.35),
    (40, 140, 0, -0.86, -1.28, 13.35),
    (80, 140, 0, -0.28, -0.97, 13.35),
    (120, 140, 0, 0.17, 0.20, 13.35),
    (160, 140, 0, 0.24, 0.08, 13.35),
    (0, 0, 80, -10.67, -2.59, 6.24),
    (80, 0, 80, -0.60, -11.34, 6.24),
    (160, 0, 80, 11.34, -2.38, 6.24),
    (0, 80, 80, 0.64, -1.03, 15.01),
    (80, 80, 80, 0.53, -1.00, 15.01),
    (160, 80, 80, 1.20, -1.04, 15.01),
    (0, 160, 80, 12.13, 1.02, 9.29),
    (80, 160, 80, 1.16, 11.64, 9.29),
    (160, 160, 80, 10.76, 3.30, 9.29),
    (0, 0, 160, -6.94, -1.52, 14.98),
    (80, 0, 160, 0.92, -8.28, 14.98),
    (160, 0, 160, 7.95, -1.94, 14.98),
    (0, 80, 160, 7.94, 1.23, 14.98),
    (80, 80, 160, 1.38, 10.07, 14.98),
    (160, 80, 160, -7.59, 1.35, 14.98),
    (0, 160, 160, 12.32, 1.28, -1.47),
    (80, 160, 160, 1.15, 11.60, -1.47),
    (160, 160, 160, -10.60, 3.51, -1.47)
]

# Extracting the last three columns
data = [row[3:] for row in dataset]

# Unpacking the columns into separate lists for x, y, z coordinates
x_data, y_data, z_data = zip(*data)

# Creating the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotting the data points
ax.scatter(x_data, y_data, z_data)

# Plotting (0, 0, 0) as a red point (pivot)
ax.scatter(0, 0, 0, color='red', label='Pivot Point (0, 0, 0)')

# Setting labels for each axis
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.title('3D Scatter Plot with Pivot Point')
plt.legend()  # Show legend
plt.show()

# Get the servo values from the initial samples
servo_values = [sample[:3] for sample in data]

# Generate new samples based on servo values
num_new_samples = 5  # Change this to generate more or fewer samples
new_samples = [generate_new_samples(servo) for servo in servo_values for _ in range(num_new_samples)]

# Display the generated new samples
for sample in new_samples:
    print(sample)