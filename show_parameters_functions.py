import pygame 
import numpy as np 

from formula_functions import *
from equation_funcs import *


def show_parameters(data_processing, font_small):
    
    if not data_processing.mode_statuses_dict['Steps change'][1]:

        params_layer = data_processing.mode_statuses_dict['Parameters'][0]
        params_layer.fill((0, 0, 0, 0))  

        const_params_dict = data_processing.constants.constants_dict
        var_params_dict = data_processing.variables.variables_dict
        accuracy = data_processing.constants.accuracy
        
        text_unit = data_processing.constants.text_unit
        
        # font_small = pygame.font.Font(None, data_processing.constants.text_spacing)

        text_x = text_unit
        text_y = 4*text_unit
        # text_y = temp_text_init
        

        text = font_small.render('Spiral parameters:', True, (0, 0, 0))
                    
        params_layer.blit(text, (text_x, text_y))
        text_y += text_unit

        for param in data_processing.constants.constants_dict.keys():  

            if param != 'c' and param != 'l':
                curr_value = data_processing.get_curr_param(param)
                if param == 'k':
                    text = font_small.render(f'{param}: {curr_value}', True, (0, 0, 0))
                    
                    params_layer.blit(text, (text_x, text_y))
                    text_y += text_unit
                    
                    theta_0 = (curr_value) * (np.pi /2) * 180 / np.pi 
                    text = font_small.render(f'Start angle: {theta_0:.{accuracy}f} deg', True, (0, 0, 0))

                else:

                    if param == 'deg':
                        text = font_small.render(f'{param}: {curr_value}', True, (0, 0, 0))
                    else:
                         text = font_small.render(f'{param}: {curr_value:.{accuracy}f}', True, (0, 0, 0))
                         
                        
                params_layer.blit(text, (text_x, text_y))
                text_y += text_unit
                
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
        # curr_spiral_angle = np.arccos(x / X_bin(rad_vec_length)) * 180/np.pi
        curr_spiral_angle = t * w * 180/np.pi
        
        text_y += text_unit
        
        text = font_small.render(f'Spiral angle: {curr_spiral_angle:.5f} deg', True, (0, 0, 0))
        params_layer.blit(text, (text_x, text_y))
        
        text_y += text_unit
 
        if not data_processing.mode_statuses_dict['Algorithm mode'][1]:
            text_y += text_unit

            x = data_processing.spiral_coordinates['x']
            y = data_processing.spiral_coordinates['y']

            coordinates_list = list(zip(data_processing.spiral_coordinates.keys(), [x, y]))


            for name, coord in coordinates_list:

                text = font_small.render(f'Spiral {name}: {coord:.{accuracy}f}', True, (0, 0, 0))
                params_layer.blit(text, (text_x, text_y))

                text_y += text_unit
                
            if data_processing.mode_statuses_dict['General solution'][1]: 

                text_y += text_unit

                text = font_small.render('Line parameters:', True, (0, 0, 0))

                params_layer.blit(text, (text_x, text_y))
                text_y += text_unit

                for param in data_processing.constants.line_constants_dict.keys():
                    curr_value = data_processing.get_curr_param(param)
                    if param == 'a':

                        text = font_small.render(f'line angle: {curr_value} deg', True, (0, 0, 0))
                        params_layer.blit(text, (text_x, text_y))
                        # text_y += data_processing.text_unit

                        a_param = data_processing.slope

                        text = font_small.render(f'{param}: {a_param}', True, (0, 0, 0))

                        text_y += text_unit

                    else:
                        text = font_small.render(f'{param}: {curr_value}', True, (0, 0, 0))
                    params_layer.blit(text, (text_x, text_y))
                    text_y += text_unit

        if data_processing.mode_statuses_dict['Derivatives'][1]:


            colors = iter([(255, 0, 0),  (0, 0,255), (0, 255, 0)])

            text_y += text_unit

#             dx_dt = data_processing.derivative_slopes['dx_dt'] * np.pi/180
#             dy_dt = data_processing.derivative_slopes['dy_dt'] * np.pi/180
#             dy_dx = data_processing.derivative_slopes['dy_dx'] * np.pi/180
            
            dx_dt = data_processing.derivative_slopes['dx_dt'] 
            dy_dt = data_processing.derivative_slopes['dy_dt'] 
            dy_dx = data_processing.derivative_slopes['dy_dx'] 

            derivatives_list = list(zip(data_processing.derivative_slopes.keys(), [dx_dt, dy_dt, dy_dx]))


            for name, slope in derivatives_list:



                text = font_small.render(f'{name}: {slope:.6f} deg', True, next(colors))
                params_layer.blit(text, (text_x, text_y))

                text_y += text_unit           


def show_mode_statuses(data_processing, font_small):

    
    show_modes_layer = data_processing.mode_statuses_dict['Modes layer'][0]
    
    text_x = data_processing.constants.text_unit
    text_y = data_processing.constants.text_unit
    
    if not data_processing.mode_statuses_dict['Equation mode'][1]:
    
        if data_processing.mode_statuses_dict['Modes layer'][1]:

            
            show_modes_layer.fill((0, 0, 0, 0))



            for mode, status in data_processing.mode_statuses_dict.items():
                
                if mode not in ['Algorithm data mode','Modes layer']:
  
                    statement = 'On' if status[1] else 'Off'
                    expression = f'{mode}: {statement}'

                    text = font_small.render(expression, True, (0, 0, 0))


                    show_modes_layer.blit(text, (text_x, text_y))

                    x_text_displacement = len(mode) * 12 + 25

                    text_x += x_text_displacement

                    if mode == 'Parameters':
                        text_x = data_processing.constants.text_unit
                        text_y = 2*data_processing.constants.text_unit
  
        
def show_equation(data_processing):

    if data_processing.mode_statuses_dict['Equation mode'][1]:
        
        text_x = data_processing.constants.text_unit
        text_y = data_processing.constants.text_unit
        
        equation_layer = data_processing.mode_statuses_dict['Equation mode'][0]
        equation_layer.fill((0, 0, 0, 0))           
     
        font_path = r"C:\Users\lenovo\Desktop\Artificial Inteligence\Jupyter projects\Intersection point between a spiral and a line test file\Paper\DejaVuFonts\dejavu-fonts-ttf-2.37\ttf\DejaVuSans.ttf"
        
        font = pygame.font.Font(font_path, 26)

        average_letter_size, half_space_lefted = construct_expression(data_processing, font)
        copy_half_space = np.copy(half_space_lefted)
        
        n, m = data_processing.reduct_funcs_dict['n'], data_processing.reduct_funcs_dict['m']
 
        index_n = contruct_index(n)
        index_m = contruct_index(m)
        
        t_eq = f't{index_n} {index_m} = '
        
        text = font.render(t_eq, True, (0, 0, 0))

        equation_layer.blit(text, (half_space_lefted, text_y))
        
        half_space_lefted+=75
        
        # print('General solution: ', data_processing.mode_statuses_dict['General solution'][1])
        # print('n: ', n, ' m:', m)
        # print()
        for word, data in data_processing.reduct_funcs_dict.items():
            if word not in ['n', 'm']:
                if word == 'NSwitch':
                    text_y += 30
                    half_space_lefted = copy_half_space + (len(t_eq)-2) * average_letter_size
                    text = font.render('+', True, (0, 0, 0))
                    equation_layer.blit(text, (half_space_lefted, text_y))
                    half_space_lefted += 25
                
                if word == 'KWL' or word == '~XYSwitch':

                    text = font.render('(', True, (0, 0, 0))            

                    equation_layer.blit(text, (half_space_lefted, text_y))
                    half_space_lefted += 10
                    
                

                text = font.render(word, True, data[1])            

                equation_layer.blit(text, (half_space_lefted, text_y))               

                half_space_lefted += data[2][0]                    
                    
                if word == 'KL':
                    
                    text = font.render(')', True, (0, 0, 0))            

                    equation_layer.blit(text, (half_space_lefted, text_y))
                    half_space_lefted += 10                    

                if word in ['LB-Alg', 'KWL', 'AB-Alg']:
                    text = font.render('+', True, (0, 0, 0))
                    equation_layer.blit(text, (half_space_lefted, text_y))
       
                    half_space_lefted += 25
                else:
                    if word not in ['AB-Alg', 'NLB-Alg']:
                        text = font.render('*', True, (0, 0, 0))

                        equation_layer.blit(text, (half_space_lefted, text_y))

                        half_space_lefted += 15
                        
                        if  word == 'ISSCDD':
                            text = font.render('(', True, (0, 0, 0))            

                            equation_layer.blit(text, (half_space_lefted, text_y))
                            half_space_lefted += 10
                        
                    else:
                        
                        text = font.render(')', True, (0, 0, 0))

                        equation_layer.blit(text, (half_space_lefted, text_y)) 
                        
        text = font.render(')', True, (0, 0, 0))

        equation_layer.blit(text, (half_space_lefted+5, text_y))
                        

def show_algorithm_rows_and_cols(data_processing, nth_t, mth_t,  x, y, font_small):
    
    show_algorithm_data_layer = data_processing.mode_statuses_dict['Algorithm data mode'][0]
    show_algorithm_data_layer.fill((0, 0, 0, 0))
    
    text_x = data_processing.constants.text_unit
    text_y = 15 * data_processing.constants.text_unit
    # text_y = 12 * data_processing.constants.text_unit
    
    
    text = font_small.render('Algorithm approximations:', True, (0, 0, 0))
    show_algorithm_data_layer.blit(text, (text_x, text_y))
    text_y += data_processing.constants.text_unit
    
    n, m = data_processing.algorithm_vars.algorithm_vars_dict['n'],\
           data_processing.algorithm_vars.algorithm_vars_dict['m']
    
    for param, value in data_processing.algorithm_vars.algorithm_vars_dict.items():

        text = font_small.render(f'{param}: {value}', True, (0, 0, 0))
        
        show_algorithm_data_layer.blit(text, (text_x, text_y))
        
        text_y += data_processing.constants.text_unit
    
    text_y += data_processing.constants.text_unit
    
    text = font_small.render(f'nth_t {n}: {nth_t}', True, (0, 0, 0))
    show_algorithm_data_layer.blit(text, (text_x, text_y))
    
    text_y += data_processing.constants.text_unit
    
    text = font_small.render(f'mth_t {m}: {mth_t}', True, (0, 0, 0))
    show_algorithm_data_layer.blit(text, (text_x, text_y))
    
    text_y +=2* data_processing.constants.text_unit
    
    
    text = font_small.render(f'Spiral x: {x}', True, (0, 0, 0))
    show_algorithm_data_layer.blit(text, (text_x, text_y))
    
    text_y += data_processing.constants.text_unit
    
    text = font_small.render(f'Spiral y: {y}', True, (0, 0, 0))
    
    show_algorithm_data_layer.blit(text, (text_x, text_y))
    
    
    
def show_steps_variables(params_layer, text_unit, factors_dict, var_params_dict,
                         steps_const_params_dict, variables_factors_dict,
                         steps_change, font_small):
    
    if steps_change:
    
        params_layer.fill((0, 0, 0, 0))


        text_x = text_unit
        text_y = 4 * text_x

        for param, value in variables_factors_dict.items():
            
            step_const_value = steps_const_params_dict[param]
            total_value = step_const_value * value

            param_name = param + ' step'
            text = font_small.render(f'{param_name}: {total_value}', True, (0, 0, 0))

            params_layer.blit(text, (text_x, text_y))
            text_y += text_unit
            
def show_circle_mode_parameters(data_processing, font_small):
    
    if data_processing.mode_statuses_dict['Explanations layer'][1]:
        explanations_layer = data_processing.mode_statuses_dict['Explanations layer'][0]
        explanations_layer.fill((0, 0, 0, 0))
        
        accuracy = data_processing.constants.accuracy
        text_unit = data_processing.constants.text_unit
        
        # Curr angular velocity
        w = data_processing.get_curr_param('w')
        
        w_sign = E(w)
        
        direction = 'clockwise' if w_sign < 0 else 'anticlockwise'

        # Curr initial spiral angle
        k = data_processing.get_curr_param('k')
        
        text_x = data_processing.constants.text_unit
        text_y = 4 * text_unit
        
        text = font_small.render(f'w: {w}', True, (0, 0, 0))
        explanations_layer.blit(text, (text_x, text_y))
        text_y += text_unit
        
        text = font_small.render(f'Direction: {direction}', True, (0, 0, 0))
        explanations_layer.blit(text, (text_x, text_y))
        text_y += text_unit
        
        text = font_small.render(f'k: {k}', True, (0, 0, 0))
                    
        explanations_layer.blit(text, (text_x, text_y))
        text_y += text_unit
        
        theta_0 = (k) * (np.pi /2) * 180 / np.pi 
        text = font_small.render(f'Start angle: {theta_0:.{accuracy}f} deg', True, (0, 0, 0))
        
        explanations_layer.blit(text, (text_x, text_y))
        