from visual_kinematics import Link, Robot

# Create links with Denavit-Hartenberg parameters
link1 = Link(d=3, a=0, alpha=0, theta=-20)
link2 = Link(d=1.5, a=1.5, alpha=90, theta=150)
link3 = Link(d=0, a=8, alpha=0, theta=245)

# Create a robot by combining links
robot = Robot([link1, link2, link3])

# Visualize the robot arm
robot.plot([0, 0, 0])  # Set joint angles as required
