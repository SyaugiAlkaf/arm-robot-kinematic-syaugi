from scipy.optimize import minimize
import numpy as np

# Deklarasi variabel dan parameter
# Calibration parameters
m1, c1 = 0.9167, 20
m2, c2 = -0.9873, 150
m3, c3 = -0.8056, 120.0

# DH parameters
a1, a2, a3, a4, a5 = 0, 0, 0, 8, 9
d1, d2, d3, d4, d5 = 0, 4, 1, 0, 0
alpha1, alpha2, alpha3, alpha4, alpha5 = 0, 0, np.radians(90), 0, 0  # Added alpha parameters

# Fungsi kalibrasi
def calibrate_servo(servo_input, slope, intercept):
    return slope * servo_input + intercept

# Konversi sudut ke radian
def toRadians(degrees):
    return np.radians(degrees)

# Definisikan fungsi untuk perhitungan forward kinematics
def forward_kinematics(theta):
    theta1, theta2, theta3, theta4, theta5 = theta
    # theta1, theta2, theta3, theta4 = theta
    # theta1, theta2, theta3 = theta
    # theta1, theta2 = theta

    T1 = np.array(
        [[np.cos(theta1), -np.sin(theta1) * np.cos(alpha1), np.sin(theta1) * np.sin(alpha1), a1 * np.cos(theta1)],
         [np.sin(theta1), np.cos(theta1) * np.cos(alpha1), -np.cos(0) * np.sin(alpha1), a1 * np.sin(theta1)],
         [0, np.sin(alpha1), np.cos(alpha1), d1],
         [0, 0, 0, 1]])

    T2 = np.array(
        [[np.cos(theta2), -np.sin(theta1) * np.cos(alpha2), np.sin(theta1) * np.sin(alpha2), a1 * np.cos(theta1)],
         [np.sin(theta1), np.cos(theta1) * np.cos(alpha2), -np.cos(theta1) * np.sin(alpha2), a1 * np.sin(theta1)],
         [0, np.sin(alpha2), np.cos(alpha2), d2],
         [0, 0, 0, 1]])

    T3 = np.array(
        [[np.cos(theta2), -np.sin(theta2) * np.cos(alpha3), np.sin(theta2) * np.sin(alpha3), a2 * np.cos(theta2)],
         [np.sin(theta2), np.cos(theta2) * np.cos(alpha3), -np.cos(theta2) * np.sin(alpha3), a2 * np.sin(theta2)],
         [0, np.sin(alpha3), np.cos(alpha3), d3],
         [0, 0, 0, 1]])

    T4 = np.array(
        [[np.cos(theta3), -np.sin(theta3) * np.cos(alpha4), np.sin(theta3) * np.sin(alpha4), a3 * np.cos(theta3)],
         [np.sin(theta3), np.cos(theta3) * np.cos(alpha4), -np.cos(theta3) * np.sin(alpha4), a3 * np.sin(theta3)],
         [0, np.sin(alpha4), np.cos(alpha4), d4],
         [0, 0, 0, 1]])
    #
    T5 = np.array(
        [[np.cos(theta5), -np.sin(theta5) * np.cos(alpha5), np.sin(theta5) * np.sin(alpha5), a3 * np.cos(theta5)],
         [np.sin(theta5), np.cos(theta5) * np.cos(alpha5), -np.cos(theta5) * np.sin(alpha5), a3 * np.sin(theta5)],
         [0, np.sin(alpha5), np.cos(alpha5), d5],
         [0, 0, 0, 1]])

    T = np.dot(np.dot(np.dot(np.dot(T1, T2), T3), T4), T5)
    # T = np.dot(np.dot(np.dot(T1, T2), T3), T4)
    # T = np.dot(np.dot(T1, T2), T3)
    # T = np.dot(T1, T2)
    return T[:3, 3]

# Definisikan fungsi kesalahan (error function)
def error_function(theta, target_position):
    end_effector_position = forward_kinematics(theta)
    error = np.linalg.norm(target_position - end_effector_position)
    return error

# Fungsi untuk menghitung inverse kinematics
# def inverse_kinematics(desired_position, initial_guess):
#     result = minimize(error_function, initial_guess, args=(desired_position,), method='L-BFGS-B')
#     if result.success:
#         return result.x
#     else:
#         return None

# Posisi yang diinginkan
desired_position = np.array([-0.6,9,5])

# Tebakan awal untuk nilai sudut sendi
initial_guess = np.radians([0, 20, 0, -25, 0])
# initial_guess = np.radians([0, 20, 0, -25])
# initial_guess = np.radians([0, 20, 0])
# initial_guess = np.radians([0, 20])

# Batasan untuk initial guess x=-0.61, y=9.38, z=5.41
initial_guess_bounds = ((np.radians(0), np.radians(0)),
                        (np.radians(20), np.radians(180)),
                        (np.radians(0), np.radians(150)),
                        (np.radians(-25), np.radians(120)),
                        (np.radians(0), np.radians(0)))
# initial_guess_bounds = ((np.radians(0), np.radians(0)),
#                         (np.radians(20), np.radians(180)),
#                         (np.radians(0), np.radians(150)),
#                         (np.radians(-25), np.radians(120)))
# initial_guess_bounds = ((np.radians(0), np.radians(0)),
#                         (np.radians(20), np.radians(180)),
#                         (np.radians(0), np.radians(150)))
# initial_guess_bounds = ((np.radians(0), np.radians(0)),
#                         (np.radians(20), np.radians(180)))

# Temukan nilai sudut sendi menggunakan inverse kinematics dengan batasan
result = minimize(error_function, initial_guess, args=(desired_position,),
                  method='L-BFGS-B', bounds=initial_guess_bounds)
solution = result.x

if solution is not None:
    print("Inverse Kinematics Solution (degrees):", np.degrees(solution))
else:
    print("Inverse Kinematics failed to converge.")

m1, c1 = 0.9138, -23.68
m2, c2 = -0.9123, 150
m3, c3 = -0.9083, 120

inverse_calibrated_solution = [
    (np.degrees(solution)[0] - c1) / m1,
    (np.degrees(solution)[1] - c2) / m2,
    (np.degrees(solution)[2] - c3) / m3
]

print("Inverse Calibrated Solution (degrees):", inverse_calibrated_solution)

