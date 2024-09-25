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
    
units =20
half_units = units/2
length = screen_width/ units

t_step = 0.02
v_step = 0.02
w_step = 0.025
k_step = 0.02
x_step = 0.02

# steps_dict_constants = {'t': t_step, 'v': v_step, 'w': w_step, 'k': k_step, 'x': x_step}

t = 1
v = 1
w = 1
k = 0
vert_line_x = 1


# const_params_dict = {'t': t,'v': v, 'w': w, 'k': k, 'x': vert_line_x}


t_additional, v_additional, w_additional, x_additional, k_additional = 0, 0, 0, 0, 0

# var_params_dict = {'t': t_additional,
#                    'v': v_additional, 
#                    'w': w_additional, 
#                    'k': k_additional, 
#                    'x': x_additional}