import numpy as np 
import pygame
from animation_functions import *


def handle_key_commands(layers_list, 
                        const_params_dict, var_params_dict, steps_dict_constants,
                        half_screen_width, half_screen_height, length, half_units,
                        update_screen, update_spiral, update_line):
   
    
    #Check for key combinations
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

    # Return to the initial parameters
#     elif (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) and keys[pygame.K_r]:

#         var_params_dict['t'], var_params_dict['v'], var_params_dict['w'], var_params_dict['x'], var_params_dict['k'] = 0, 0, 0, 0, 0

#         const_params_dict['w'] = 1

#         update_screen, update_spiral, update_line = True, True, True


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


def handle_shift_key_controls(event, update_screen, update_spiral, const_params_dict, var_params_dict):
    
    if event.type == pygame.KEYDOWN and (pygame.key.get_mods() & pygame.KMOD_SHIFT) and event.key == pygame.K_w:
        const_params_dict['w'] *= -1

        var_params_dict['w'] *= -1
        
        update_screen, update_spiral = True, True
        
    if event.type == pygame.KEYDOWN and (pygame.key.get_mods() & pygame.KMOD_SHIFT) and event.key == pygame.K_r:
        
        var_params_dict['t'], var_params_dict['v'], var_params_dict['w'], var_params_dict['x'], var_params_dict['k'] = 0, 0, 0, 0, 0

        const_params_dict['w'] = 1
        
        update_screen, update_spiral = True, True
        
    return update_screen, update_spiral, const_params_dict, var_params_dict