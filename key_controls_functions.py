import numpy as np 
import pygame
from animation_functions import *
from variables import *

def handle_key_commands(const_params_dict, var_params_dict, steps_dict_constants,
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


def handle_shift_key_commands(event, update_screen, update_spiral, const_params_dict, var_params_dict, mode_statuses_dict):
    
    # Turn the direction of the spiral
    if event.type == pygame.KEYDOWN and (pygame.key.get_mods() & pygame.KMOD_SHIFT) and event.key == pygame.K_w:
        const_params_dict['w'] *= -1

        var_params_dict['w'] *= -1
        
        update_screen, update_spiral = True, True
       
      
    # Reset variables to their initial values
    if event.type == pygame.KEYDOWN and (pygame.key.get_mods() & pygame.KMOD_SHIFT) and event.key == pygame.K_r:
        
        var_params_dict['t'], var_params_dict['v'], \
        var_params_dict['w'], var_params_dict['x'], \
        var_params_dict['k'] = t_additional, v_additional, w_additional, x_additional, k_additional

        const_params_dict['w'] = w
        
        '''background_mode = True
            algorithm_mode = False
            line_mode = True
            spiral_mode = True
            y_axis_intersects = True
        line_intersects = True
        algorithm_data_mode = True
        parameters_mode = True 
        t_diagram_mode = False'''
        
        mode_dict_keys = mode_statuses_dict.keys()
        mode_dict_default_values = iter([background_mode, algorithm_mode, algorithm_data_mode, t_diagram_mode, line_mode, spiral_mode,\
                                         y_axis_intersects, line_intersects, parameters_mode, True])
        
        for key in  mode_statuses_dict.keys():
            mode_statuses_dict[key][1] = next(mode_dict_default_values)

        update_screen, update_spiral = True, True
   
    return update_screen, update_spiral, const_params_dict, var_params_dict



def handle_ctrl_commands(event, update_screen, mode_statuses_dict):
           
    is_turn_off = None

    
    if event.type == pygame.KEYDOWN:
        mods = pygame.key.get_mods()
        update_screen = True
        if (mods & pygame.KMOD_CTRL)  and event.key == pygame.K_a:
            
            init_state = mode_statuses_dict['Algorithm mode'][1]
            mode_statuses_dict['Algorithm mode'][1] = False if init_state else True
            
            if init_state:
                is_turn_off = True
                
            # Set the layers to True
            for mode, (_, boolean) in mode_statuses_dict.items():
                if mode not in ['Algorithm mode', 'T-diagram', 'Algorithm data mode','Modes layer']:
                    if not boolean:
                        mode_statuses_dict[mode][1] = True 
                        
        elif (mods & pygame.KMOD_CTRL) and event.key == pygame.K_t:
            mode_statuses_dict['T-diagram'][1] = not mode_statuses_dict['T-diagram'][1]
             
        if not mode_statuses_dict['Algorithm mode'][1]:
            if event.key == pygame.K_l:
                mode_statuses_dict['Line'][1] = not mode_statuses_dict['Line'][1]

            elif event.key == pygame.K_s:
                mode_statuses_dict['Spiral'][1] = not mode_statuses_dict['Spiral'][1]
                
            elif event.key == pygame.K_n:
                mode_statuses_dict['Y-intersects'][1] = not mode_statuses_dict['Y-intersects'][1]

            elif event.key == pygame.K_m:
                mode_statuses_dict['Line-intersects'][1] = not mode_statuses_dict['Line-intersects'][1]

            elif event.key == pygame.K_p:
                mode_statuses_dict['Parameters'][1] = not mode_statuses_dict['Parameters'][1]
            
            elif event.key == pygame.K_c:
                mode_statuses_dict['Coordinates'][1] = not mode_statuses_dict['Coordinates'][1]
            
    return update_screen, mode_statuses_dict, is_turn_off 



def handle_algorithm_mode_controls(event, algorithm_variables_dict, t_mth_aproxim_list, update_screen):

    n = algorithm_variables_dict['n']
    m = algorithm_variables_dict['m']
    total_n = algorithm_variables_dict['total_n']

    keys = pygame.key.get_pressed()
   
   
    if event.type == pygame.KEYDOWN and keys[pygame.K_n] and keys[pygame.K_UP]:
        
    
        if n+1 <= total_n:
      
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
