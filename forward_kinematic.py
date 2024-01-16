import numpy as np

# Calibration parameters
m1, c1 = 0.9167, 20
m2, c2 = -0.9873, 150
m3, c3 = -0.8056, 120.0

# Calibration functions
def calibrate_servo(servo_input, slope, intercept):
    return slope * servo_input + intercept

# DH parameters
a1, a2, a3, a4, a5 = 0, 0, 0, 8, 10
d1, d2, d3, d4, d5 = 0, 3.5, 2, 0, 0
alpha1, alpha2, alpha3, alpha4, alpha5 = 0, 0, np.radians(90), 0, 0  # Added alpha parameters

servo_input2 = 0
servo_input3 = 0
servo_input4 = 0

# Joint angles from servo input
theta1_deg = 0
theta2_deg = calibrate_servo(servo_input2, m1, c1)
theta3_deg = calibrate_servo(servo_input3, m2, c2)
theta4_deg = calibrate_servo(servo_input4, m2, c2)
theta5_deg = 0

# Convert angles to radians
theta1 = np.radians(theta1_deg)
theta2 = np.radians(theta2_deg)
theta3 = np.radians(theta3_deg)
theta4 = np.radians(theta4_deg)
theta5 = np.radians(theta5_deg)

# Forward kinematics matrices
T1 = np.array([[np.cos(theta1), -np.sin(theta1)*np.cos(alpha1), np.sin(theta1)*np.sin(alpha1), a1*np.cos(theta1)],
               [np.sin(theta1), np.cos(theta1)*np.cos(alpha1), -np.cos(0)*np.sin(alpha1), a1*np.sin(theta1)],
               [0, np.sin(alpha1), np.cos(alpha1), d1],
               [0, 0, 0, 1]])

T2 = np.array([[np.cos(theta2), -np.sin(theta1)*np.cos(alpha2), np.sin(theta1)*np.sin(alpha2), a1*np.cos(theta1)],
               [np.sin(theta1), np.cos(theta1)*np.cos(alpha2), -np.cos(theta1)*np.sin(alpha2), a1*np.sin(theta1)],
               [0, np.sin(alpha2), np.cos(alpha2), d2],
               [0, 0, 0, 1]])

T3 = np.array([[np.cos(theta2), -np.sin(theta2)*np.cos(alpha3), np.sin(theta2)*np.sin(alpha3), a2*np.cos(theta2)],
               [np.sin(theta2), np.cos(theta2)*np.cos(alpha3), -np.cos(theta2)*np.sin(alpha3), a2*np.sin(theta2)],
               [0, np.sin(alpha3), np.cos(alpha3), d3],
               [0, 0, 0, 1]])

T4 = np.array([[np.cos(theta3), -np.sin(theta3)*np.cos(alpha4), np.sin(theta3)*np.sin(alpha4), a3*np.cos(theta3)],
               [np.sin(theta3), np.cos(theta3)*np.cos(alpha4), -np.cos(theta3)*np.sin(alpha4), a3*np.sin(theta3)],
               [0, np.sin(alpha4), np.cos(alpha4), d4],
               [0, 0, 0, 1]])

T5 = np.array([[np.cos(theta5), -np.sin(theta5)*np.cos(alpha5), np.sin(theta5)*np.sin(alpha5), a3*np.cos(theta5)],
               [np.sin(theta5), np.cos(theta5)*np.cos(alpha5), -np.cos(theta5)*np.sin(alpha5), a3*np.sin(theta5)],
               [0, np.sin(alpha5), np.cos(alpha5), d5],
               [0, 0, 0, 1]])

# Overall transformation matrix
T = np.dot(np.dot(np.dot(np.dot(T1, T2), T3), T4), T5)
# T = np.dot(np.dot(T1, T2), T3)

# Extract end-effector pose
end_effector_position = T[:3, 3]
end_effector_orientation_matrix = T[:3, :3]

print("End-Effector Position:", end_effector_position)
print("End-Effector Orientation Matrix:", end_effector_orientation_matrix)
