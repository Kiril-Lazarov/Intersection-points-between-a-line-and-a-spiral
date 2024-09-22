import pygame 
import numpy as np

def show_parameters(params_layer, font_small, const_params_dict,
                    var_params_dict):
    
    params_layer.fill((0, 0, 0, 0))  
    
    text_x = 20
    text_y = 20
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
        
        
def update_var_params_dict(var_params_dict, v_additional, w_additional, x_additional, k_additional):
    
    var_params_dict = {'v': v_additional, 
                        'w': w_additional, 
                       'k': k_additional, 
                       'x': x_additional} 
    return var_params_dict