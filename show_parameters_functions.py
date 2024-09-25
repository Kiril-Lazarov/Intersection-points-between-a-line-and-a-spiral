import pygame 
import numpy as np

def show_parameters(params_layer, font_small, const_params_dict,
                    var_params_dict):
    
    params_layer.fill((0, 0, 0, 0))  
    
    text_x = 20
    text_y = 60
    for param, value in const_params_dict.items():  
            
        curr_value = value + var_params_dict[param]
        text = font_small.render(f'{param}: {curr_value:.2f}', True, (0, 0, 0))
        
        params_layer.blit(text, (text_x, text_y))
        text_y += 20

        if param == 'k':
            theta_0 = (value + var_params_dict[param]) * (np.pi /2) * 180 / np.pi 
            text = font_small.render(f'theta_0: {theta_0:.2f}', True, (0, 0, 0))
            
            params_layer.blit(text, (text_x, text_y))
            text_y += 20


def show_mode_statuses(show_modes_layer, font_small, mode_statuses_dict):
    
    show_modes_layer.fill((0, 0, 0, 0))

    text_x = 20
    text_y = 20
   
    for mode, status in mode_statuses_dict.items():

        statement = 'On' if status else 'Off'

        text = font_small.render(f'{mode}: {statement}', True, (0, 0, 0))

        
        show_modes_layer.blit(text, (text_x, text_y))
        
        x_text_displacement = len(mode) * 8
        
        text_x += x_text_displacement