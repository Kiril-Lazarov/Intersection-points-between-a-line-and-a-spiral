import pygame 
import numpy as np

from formula_functions import *

def show_parameters(data_processing, font_small):
    
    if not data_processing.mode_statuses_dict['Steps change'][1]:

        params_layer = data_processing.mode_statuses_dict['Parameters'][0]
        params_layer.fill((0, 0, 0, 0))  

        const_params_dict = data_processing.constants.constants_dict
        var_params_dict = data_processing.variables.variables_dict
        accuracy = data_processing.constants.accuracy

        text_x = data_processing.text_unit
        text_y = 3 * text_x
        
        text = font_small.render('Spiral parameters:', True, (0, 0, 0))
                    
        params_layer.blit(text, (text_x, text_y))
        text_y += data_processing.text_unit

        for param in data_processing.constants.constants_dict.keys():  

            if param != 'c' and param != 'l':
                curr_value = data_processing.get_curr_param(param)
                if param == 'k':
                    text = font_small.render(f'{param}: {curr_value}', True, (0, 0, 0))
                    
                    params_layer.blit(text, (text_x, text_y))
                    text_y += data_processing.text_unit
                    
                    theta_0 = (curr_value) * (np.pi /2) * 180 / np.pi 
                    text = font_small.render(f'Start angle: {theta_0:.{accuracy}f} deg', True, (0, 0, 0))

                else:

                    if param == 'deg':
                        text = font_small.render(f'{param}: {curr_value}', True, (0, 0, 0))
                    else:
                        text = font_small.render(f'{param}: {curr_value:.{accuracy}f}', True, (0, 0, 0))

                params_layer.blit(text, (text_x, text_y))
                text_y += data_processing.text_unit
                
         # Curr time
        t = data_processing.get_curr_param('t')

        # Curr vector velocity
        v = data_processing.get_curr_param('v')

        # Curr angular velocity
        w = data_processing.get_curr_param('w')

        # Curr initial spiral angle
        k = data_processing.get_curr_param('k')
        
        deg_x, deg_y = data_processing.get_curr_param('deg')
                
        x = get_nth_deg_x_derivative(deg_x,t, v,w,k)
        y = get_nth_deg_y_derivative(deg_y,t, v,w,k)
        
        rad_vec_length = np.sqrt(x**2 + y**2)
        curr_spiral_angle = np.arccos(x / X_bin(rad_vec_length)) * 180/np.pi
        
        text_y += data_processing.text_unit
        
        text = font_small.render(f'Spiral angle: {curr_spiral_angle:.5f} deg', True, (0, 0, 0))
        params_layer.blit(text, (text_x, text_y))
        
        text_y += data_processing.text_unit
 
        if not data_processing.mode_statuses_dict['Algorithm mode'][1]:
            text_y += data_processing.text_unit

            x = data_processing.spiral_coordinates['x']
            y = data_processing.spiral_coordinates['y']

            coordinates_list = list(zip(data_processing.spiral_coordinates.keys(), [x, y]))


            for name, coord in coordinates_list:

                text = font_small.render(f'Spiral {name}: {coord:.{accuracy}f}', True, (0, 0, 0))
                params_layer.blit(text, (text_x, text_y))

                text_y += data_processing.text_unit
             
        text_y += data_processing.text_unit
        
        text = font_small.render('Line parameters:', True, (0, 0, 0))
                    
        params_layer.blit(text, (text_x, text_y))
        text_y += data_processing.text_unit
        
        for param in data_processing.constants.line_constants_dict.keys():
            curr_value = data_processing.get_curr_param(param)
            
            text = font_small.render(f'{param}: {curr_value}', True, (0, 0, 0))
            params_layer.blit(text, (text_x, text_y))
            text_y += data_processing.text_unit

        if data_processing.mode_statuses_dict['Derivatives'][1]:


            colors = iter([(255, 0, 0),  (0, 0,255), (0, 255, 0)])

            text_y += data_processing.text_unit

            dx_dt = data_processing.derivative_slopes['dx_dt'] * np.pi/180
            dy_dt = data_processing.derivative_slopes['dy_dt'] * np.pi/180
            dy_dx = data_processing.derivative_slopes['dy_dx'] * np.pi/180

            derivatives_list = list(zip(data_processing.derivative_slopes.keys(), [dx_dt, dy_dt, dy_dx]))


            for name, slope in derivatives_list:



                text = font_small.render(f'{name}: {slope:.6f} deg', True, next(colors))
                params_layer.blit(text, (text_x, text_y))

                text_y += data_processing.text_unit




def show_mode_statuses(data_processing, font_small):
    
    if data_processing.mode_statuses_dict['Modes layer'][1]:
        
        show_modes_layer = data_processing.mode_statuses_dict['Modes layer'][0]
        show_modes_layer.fill((0, 0, 0, 0))

        text_x = data_processing.text_unit
        text_y = data_processing.text_unit

        for mode, status in data_processing.mode_statuses_dict.items():

            if mode not in ['Algorithm data mode','Modes layer']:

                statement = 'On' if status[1] else 'Off'
                expression = f'{mode}: {statement}'

                text = font_small.render(expression, True, (0, 0, 0))


                show_modes_layer.blit(text, (text_x, text_y))

                x_text_displacement = len(mode) * 12 + 25

                text_x += x_text_displacement
        

def show_algorithm_rows_and_cols(data_processing, x, y, font_small):
    
    show_algorithm_data_layer = data_processing.mode_statuses_dict['Algorithm data mode'][0]
    show_algorithm_data_layer.fill((0, 0, 0, 0))
    
    text_x = data_processing.text_unit
    text_y = 18 * data_processing.text_unit
    
    text = font_small.render('Algorithm approximations:', True, (0, 0, 0))
    show_algorithm_data_layer.blit(text, (text_x, text_y))
    text_y += data_processing.text_unit
    
    for param, value in data_processing.algorithm_vars.algorithm_vars_dict.items():

        text = font_small.render(f'{param}: {value}', True, (0, 0, 0))
        
        show_algorithm_data_layer.blit(text, (text_x, text_y))
        
        text_y += data_processing.text_unit
    
    text_y += data_processing.text_unit
    
    text = font_small.render(f'Spiral x: {x}', True, (0, 0, 0))
    show_algorithm_data_layer.blit(text, (text_x, text_y))
    
    text_y += data_processing.text_unit
    
    text = font_small.render(f'Spiral y: {y}', True, (0, 0, 0))
    
    show_algorithm_data_layer.blit(text, (text_x, text_y))
    
    
    
def show_steps_variables(data_processing, font_small):
    
    if data_processing.mode_statuses_dict['Steps change'][1]:
    
        params_layer = data_processing.mode_statuses_dict['Parameters'][0]
        params_layer.fill((0, 0, 0, 0))

        factors_dict = data_processing.variables.factors_dict
        var_params_dict = data_processing.variables.variables_dict
        steps_const_params_dict = data_processing.constants.steps_constants_dict 

        text_x = data_processing.text_unit
        text_y = 3 * text_x

        for param, value in data_processing.variables.factors_dict.items():
            
            step_const_value = steps_const_params_dict[param]
            total_value = step_const_value * value

            param_name = param + ' step'
            text = font_small.render(f'{param_name}: {total_value}', True, (0, 0, 0))

            params_layer.blit(text, (text_x, text_y))
            text_y += data_processing.text_unit