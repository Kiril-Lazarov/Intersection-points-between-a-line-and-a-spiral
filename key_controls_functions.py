import numpy as np 
import pygame
from animation_functions import *


def handle_key_commands(layers_list, 
                        const_params_dict, var_params_dict, steps_dict_constants,
                        half_screen_width, half_screen_height, length, half_units,
                        update_screen, update_spiral, update_line):
   
    
    # Check for key combinations
    keys = pygame.key.get_pressed()
  
    # Right movement of the line
    if keys[pygame.K_x] and keys[pygame.K_RIGHT]:

        var_params_dict['x'] += steps_dict_constants['x']           

        update_screen, update_line = True, True

    # Left movement of the line
    elif keys[pygame.K_x] and keys[pygame.K_LEFT]:
        var_params_dict['x'] -= steps_dict_constants['x']

        update_screen, update_line = True, True

    # Increase angular velocity `w`    
    elif keys[pygame.K_w] and keys[pygame.K_UP]:
        var_params_dict['w'] += steps_dict_constants['w']

        update_screen, update_spiral = True, True

    # Decrease angular velocity `w`  
    elif keys[pygame.K_w] and keys[pygame.K_DOWN]:
        var_params_dict['w'] -= steps_dict_constants['w']


        update_screen, update_spiral = True, True

    # Increase initial spiral angle coefficient `k`  
    elif keys[pygame.K_k] and keys[pygame.K_UP]:

        var_params_dict['k'] += steps_dict_constants['k']


        if const_params_dict['k'] + var_params_dict['k'] >= 4:         
            var_params_dict['k'] = 0

        update_screen, update_spiral = True, True


    # Decrease initial spiral angle coefficient `k`
    elif keys[pygame.K_k] and keys[pygame.K_DOWN]:

        var_params_dict['k'] -= steps_dict_constants['k']

        if const_params_dict['k'] + var_params_dict['k'] <= 0:         
            var_params_dict['k'] = 4

        update_screen, update_spiral = True, True

    # Increase spiral radius velocity `v`
    elif keys[pygame.K_v] and keys[pygame.K_UP]:
        var_params_dict['v'] += steps_dict_constants['v']            


        update_screen, update_spiral = True, True

    # Decrease spiral radius velocity `v`
    elif keys[pygame.K_v] and keys[pygame.K_DOWN]:           

        if const_params_dict['v'] + var_params_dict['v'] > 0:
            var_params_dict['v'] -= steps_dict_constants['v']

            update_screen, update_spiral = True, True


    # Increase time `t`
    elif keys[pygame.K_t] and keys[pygame.K_UP]:
        var_params_dict['t'] += steps_dict_constants['t']            

        update_screen, update_spiral = True, True

    # Decrease time `t`
    elif keys[pygame.K_t] and keys[pygame.K_DOWN]:           

        if const_params_dict['t'] + var_params_dict['t'] > 0:
            var_params_dict['t'] -= steps_dict_constants['t']

            update_screen, update_spiral = True, True

            
    return update_screen, update_spiral, update_line, var_params_dict, const_params_dict


def handle_shift_key_commands(event, update_screen, update_spiral, const_params_dict, var_params_dict):
    
    # Turn the direction of the spiral
    if event.type == pygame.KEYDOWN and (pygame.key.get_mods() & pygame.KMOD_SHIFT) and event.key == pygame.K_w:
        const_params_dict['w'] *= -1

        var_params_dict['w'] *= -1
        
        update_screen, update_spiral = True, True
      
    # Reset variables to their initial values
    if event.type == pygame.KEYDOWN and (pygame.key.get_mods() & pygame.KMOD_SHIFT) and event.key == pygame.K_r:
        
        var_params_dict['t'], var_params_dict['v'], var_params_dict['w'], var_params_dict['x'], var_params_dict['k'] = 0, 0, 0, 0, 0

        const_params_dict['w'] = 1
        
        update_screen, update_spiral = True, True
   
    return update_screen, update_spiral, const_params_dict, var_params_dict


def handle_ctrl_commands(event, update_screen, mode_statuses_dict):
           
    is_turn_off = None
    
    if event.type == pygame.KEYDOWN:
        mods = pygame.key.get_mods()
        if (mods & pygame.KMOD_CTRL) and not (mods & pygame.KMOD_SHIFT) and event.key == pygame.K_a:
            
            init_state = mode_statuses_dict['Algorithm mode']
            mode_statuses_dict['Algorithm mode'] = False if init_state else True
            
            if init_state:
                is_turn_off = True 
            
            update_screen = True

    return update_screen, mode_statuses_dict, is_turn_off 



def handle_algorithm_mode_controls(event, algorithm_variables_dict, t_mth_aproxim_list, update_screen):

    n = algorithm_variables_dict['n']
    m = algorithm_variables_dict['m']
    total_n = algorithm_variables_dict['total_n']

    keys = pygame.key.get_pressed()
   
   
    if event.type == pygame.KEYDOWN and keys[pygame.K_n] and keys[pygame.K_UP]:
        
    
        if n+1 <= total_n:
            # print('n: ', algorithm_variables_dict['nth_y_intersect'])
            algorithm_variables_dict['n'] +=1
            algorithm_variables_dict['m'] = 0
            
            t_mth_aproxim_list.clear()
            
            update_screen = True
            
    elif event.type == pygame.KEYDOWN and keys[pygame.K_n] and keys[pygame.K_DOWN]:
    
        if n-1 > 0:
            algorithm_variables_dict['n'] -=1
            algorithm_variables_dict['m'] = 0
            
            t_mth_aproxim_list.clear()
            update_screen = True
            
    elif event.type == pygame.KEYDOWN and keys[pygame.K_m] and keys[pygame.K_UP]:

        algorithm_variables_dict['m'] +=1
        
        update_screen = True

    elif event.type == pygame.KEYDOWN and keys[pygame.K_m] and keys[pygame.K_DOWN]:

        if m-1 >= 0:
            algorithm_variables_dict['m'] -=1
            update_screen = True
            
    return algorithm_variables_dict, update_screen
