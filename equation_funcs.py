import numpy as np
import pygame 

from formula_functions import *

def contruct_index(number):
    base_unicode = 0x2080
    
    final_index = ''
    
    for letter in str(number):
        final_index += chr(base_unicode + int(letter))
    return final_index

def construct_expression(data_processing, font):
        
    algorithm_vars_dict = data_processing.algorithm_vars.algorithm_vars_dict
    
    reduct_funcs_dict = data_processing.reduct_funcs_dict
    
    data_processing.reduct_funcs_dict['n'] = np.copy(algorithm_vars_dict['n'])
    data_processing.reduct_funcs_dict['m'] = np.copy(algorithm_vars_dict['m'])
    
        
    data_processing.reduct_funcs_dict['NSwitch'][0] = get_n_coeff(reduct_funcs_dict['n'])

    data_processing.reduct_funcs_dict['~NSwitch'][0] = 1 - data_processing.reduct_funcs_dict['NSwitch'][0]


    n, m = data_processing.reduct_funcs_dict['n'], data_processing.reduct_funcs_dict['m']

    index_n = contruct_index(n)
    index_m = contruct_index(m)
    

    t_eq = f't{index_n} {index_m} = '
    k_sign = ''
    n_switch = 'NSwitch'
    opp_n_switch = '~NSwitch'

    expression = f'{t_eq}{opp_n_switch}*{k_sign}*LB-Alg + {n_switch}*AB-Alg'
    
    expression_pixels_count = ((len(expression) + 20) * 20)/2

    half_space_lefted = (data_processing.constants.screen_width - expression_pixels_count)/2
  
    data_processing.update_reduct_funcs_dict()

    average_letter_size = expression_pixels_count/ len(expression)
    
    return average_letter_size, half_space_lefted