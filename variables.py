"""
Global animation variables

""" 

screen_width = 1500
screen_height = 800
half_screen_width = screen_width / 2
half_screen_height = screen_height / 2

FPS = 25


'''
Global spiral and line variables
'''

# Total number of units on the x-axis – both positive and negative.
units =20
half_units = units/2

# Length of one unit along the coordinate axis, calculated as a function of the screen width and the number of units.
length = screen_width/ units


# The step for changing the values of the spiral and line parameters.
t_step = 0.025
v_step = 0.025
w_step = 0.04
k_step = 0.025
x_step = 0.025

# Spiral and line constants. The angular velocity is also constant, even though it can have a value of -1.
t= 1 # Time
v = 1 # Speed of the radius-vector
w = 1 # Angular velocity
k = 0 # Initial angle coefficient measured by pi/2
vert_line_x = 1 # Start position of the vertical line over x-axis

# Variables for parameter changes.
t_additional, v_additional, w_additional, x_additional, k_additional = 0, 0, 0, 0, 0

background_mode = True
algorithm_mode = False
line_mode = True
spiral_mode = True
y_axis_intersects = True
line_intersects = True
algorithm_data_mode = True
parameters_mode = True 
t_diagram_mode = False
