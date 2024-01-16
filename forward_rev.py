import numpy as np

# DH parameters
a1, a2, a3, a4, a5 = 0, 0, 0, 8, 9
d1, d2, d3, d4, d5 = 0, 4, 2, 0, 0
alpha1, alpha2, alpha3, alpha4, alpha5 = 0, 0, np.radians(90), 0, 0  # Alpha parameters

# Joint angles in radians
theta1, theta2, theta3, theta4, theta5 = np.radians(0), np.radians(50), np.radians(1), np.radians(120), np.radians(0)

# Transformation matrices for movable joints
T1 = np.array([[np.cos(theta1), -np.sin(theta1)*np.cos(alpha1), np.sin(theta1)*np.sin(alpha1), a1*np.cos(theta1)],
               [np.sin(theta1), np.cos(theta1)*np.cos(alpha1), -np.cos(theta1)*np.sin(alpha1), a1*np.sin(theta1)],
               [0, np.sin(alpha1), np.cos(alpha1), d1],
               [0, 0, 0, 1]])

T2 = np.array([[np.cos(theta2), -np.sin(theta2)*np.cos(alpha2), np.sin(theta2)*np.sin(alpha2), a2*np.cos(theta2)],
               [np.sin(theta2), np.cos(theta2)*np.cos(alpha2), -np.cos(theta2)*np.sin(alpha2), a2*np.sin(theta2)],
               [0, np.sin(alpha2), np.cos(alpha2), d2],
               [0, 0, 0, 1]])

T3 = np.array([[np.cos(theta3), -np.sin(theta3)*np.cos(alpha3), np.sin(theta3)*np.sin(alpha3), a3*np.cos(theta3)],
               [np.sin(theta3), np.cos(theta3)*np.cos(alpha3), -np.cos(theta3)*np.sin(alpha3), a3*np.sin(theta3)],
               [0, np.sin(alpha3), np.cos(alpha3), d3],
               [0, 0, 0, 1]])

T4 = np.array([[np.cos(theta4), -np.sin(theta4)*np.cos(alpha4), np.sin(theta4)*np.sin(alpha4), a4*np.cos(theta4)],
               [np.sin(theta4), np.cos(theta4)*np.cos(alpha4), -np.cos(theta4)*np.sin(alpha4), a4*np.sin(theta4)],
               [0, np.sin(alpha4), np.cos(alpha4), d4],
               [0, 0, 0, 1]])

T5 = np.array([[np.cos(theta5), -np.sin(theta5)*np.cos(alpha5), np.sin(theta5)*np.sin(alpha5), a5*np.cos(theta5)],
               [np.sin(theta5), np.cos(theta5)*np.cos(alpha5), -np.cos(theta5)*np.sin(alpha5), a5*np.sin(theta5)],
               [0, np.sin(alpha5), np.cos(alpha5), d5],
               [0, 0, 0, 1]])
print(T1[:3, 3])
print(T2[:3, 3])
print(T3[:3, 3])
print(T4[:3, 3])
print(T5[:3, 3])
# Overall transformation matrix (excluding fixed joints 1 and 5)
# T = np.dot(np.dot(T2, T3), T4)
# T = np.dot(np.dot(np.dot(np.dot(T5, T4), T3), T2), T1)
T = np.dot(np.dot(np.dot(T2, T3), T4), T5)
# Extract end-effector pose
end_effector_position = T[:3, 3]
end_effector_orientation_matrix = T[:3, :3]

print("End-Effector Position:", end_effector_position)
print("End-Effector Orientation Matrix:", end_effector_orientation_matrix)
