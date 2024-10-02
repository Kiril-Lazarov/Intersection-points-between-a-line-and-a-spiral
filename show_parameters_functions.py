import pygame 
import numpy as np

def show_parameters(params_layer, font_small, const_params_dict,
                    var_params_dict):
    
    params_layer.fill((0, 0, 0, 0))  
    
    text_x = 20
    text_y = 60
    for param, value in const_params_dict.items():  
            
        if param == 'c':
       
            curr_x = value[0] + var_params_dict[param][0]
            curr_y = value[1] + var_params_dict[param][1]
            
            text = font_small.render(f'x: {curr_x}', True, (0, 0, 0))
            params_layer.blit(text, (text_x, text_y))
            text_y += 20
            
            
            text = font_small.render(f'y: {curr_y}', True, (0, 0, 0))
            params_layer.blit(text, (text_x, text_y))
            text_y += 20
        else:
            curr_value = value + var_params_dict[param]
            text = font_small.render(f'{param}: {curr_value:.2f}', True, (0, 0, 0))
        
            params_layer.blit(text, (text_x, text_y))
            text_y += 20

        if param == 'k':
            theta_0 = (value + var_params_dict[param]) * (np.pi /2) * 180 / np.pi 
            text = font_small.render(f'Start angle: {theta_0:.2f} deg', True, (0, 0, 0))
            
            params_layer.blit(text, (text_x, text_y))
            text_y += 20


def show_mode_statuses(show_modes_layer, font_small, mode_statuses_dict):
    
    if mode_statuses_dict['Parameters']:
        show_modes_layer.fill((0, 0, 0, 0))

        text_x = 20
        text_y = 20

        for mode, status in mode_statuses_dict.items():

            if mode not in ['Algorithm data mode','Modes layer']:

                statement = 'On' if status[1] else 'Off'
                expression = f'{mode}: {statement}'

                text = font_small.render(expression, True, (0, 0, 0))


                show_modes_layer.blit(text, (text_x, text_y))

                x_text_displacement = len(mode) * 12 + 40

                text_x += x_text_displacement
        

def show_algorithm_rows_and_cols(show_algorithm_data_layer, x, y, algorithm_variables_dict, font_small):
    
    show_algorithm_data_layer.fill((0, 0, 0, 0))
    
    text_x = 20
    text_y = 200
    
    for param, value in algorithm_variables_dict.items():

        text = font_small.render(f'{param}: {value}', True, (0, 0, 0))
        
        show_algorithm_data_layer.blit(text, (text_x, text_y))
        
        text_y += 20
    
    text_y += 20
    
    text = font_small.render(f'Spiral x: {x}', True, (0, 0, 0))
    show_algorithm_data_layer.blit(text, (text_x, text_y))
    
    text_y += 20
    
    text = font_small.render(f'Spiral y: {y}', True, (0, 0, 0))
    show_algorithm_data_layer.blit(text, (text_x, text_y))