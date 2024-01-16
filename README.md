# Arm Robot Kinematic Project

<p align="center">
  <img src="images/robot_arm.jpg" alt="Robot Arm" width="600"/>
</p>

## Hardware Used
- **MCU:** Arduino Uno
  ![Arduino Uno](images/arduino_uno.jpg)
- **3D Printed Arm Robot Structure:**
  - 3 Revolute Joints
  - 1 Fixed Joint for gripping things
  ![Arm Robot Structure](images/arm_structure.jpg)
- **Servos:** 4 Servos
  ![Servos](images/servos.jpg)
- **Breadboard & Wire:**
  ![Breadboard & Wire](images/breadboard_wire.jpg)
- **Case:** Case to cover the MCU and breadboard
  ![Case](images/case.jpg)

## Method
The kinematics of the arm robot are determined using the k-nearest neighbors (KNN) algorithm, specifically its Euclidean range method. The x, y, z data are collected through actual measurements using the servos as the independent variables. The x, y, z values are stored to calculate the Euclidean distance between the collected and desired x, y, z coordinates.

## Future Development
In the future, I plan to enhance the capabilities of the robot by incorporating machine learning. The goal is to enable the robot to move according to camera input, opening up possibilities for more interactive and dynamic functionalities.

## Project Showcase
Here are some snapshots of the Arm Robot in action:

<p align="center">
  <img src="images/robot_action_1.jpg" alt="Robot Action 1" width="400"/>
  <img src="images/robot_action_2.jpg" alt="Robot Action 2" width="400"/>
</p>

Feel free to explore the [demo video](#) to see the Arm Robot Kinematic project in action!

## License
This project is licensed under the [MIT License](LICENSE).
