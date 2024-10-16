import numpy as np 
import pygame
from animation_functions import *
from variables import *

def handle_key_commands(const_params_dict, var_params_dict, steps_dict_constants,
                        updates_dict, algorithm_mode):
      
    updates_dict['shift_coords'] = False    
    
    # Check for key combinations
    keys = pygame.key.get_pressed()
    
   
    if keys[pygame.K_z]:
        
        # Zoom-in 
        if keys[pygame.K_UP]:
            var_params_dict['l'] += steps_dict_constants['l']

            updates_dict['update_screen'], updates_dict['update_spiral'],\
            updates_dict['update_line'], updates_dict['shift_coords'] = True, True, True, True
        
        # Zoom-out
        elif keys[pygame.K_DOWN]:

            possible_length = const_params_dict['l'] + var_params_dict['l'] - steps_dict_constants['l']

            if possible_length > 0:
                var_params_dict['l'] -= steps_dict_constants['l']

            updates_dict['update_screen'], updates_dict['update_spiral'],\
            updates_dict['update_line'], updates_dict['shift_coords'] = True, True, True, True
        
       
    elif keys[pygame.K_b]:
        
        # Move the screen up along the y-axis.
        if keys[pygame.K_UP]:
            var_params_dict['c'][1] += steps_dict_constants['c']

            updates_dict['update_screen'], updates_dict['update_spiral'],\
            updates_dict['update_line'], updates_dict['shift_coords'] = True, True, True, True

        # Move the screen down along the y-axis.    
        elif keys[pygame.K_DOWN]:
            var_params_dict['c'][1] -= steps_dict_constants['c']

            updates_dict['update_screen'], updates_dict['update_spiral'],\
            updates_dict['update_line'], updates_dict['shift_coords'] = True, True, True, True

        # Move the screen left along the y-axis.    
        elif keys[pygame.K_LEFT]:
            var_params_dict['c'][0] -= steps_dict_constants['c']

            updates_dict['update_screen'], updates_dict['update_spiral'],\
            updates_dict['update_line'], updates_dict['shift_coords'] = True, True, True, True

        # Move the screen right along the y-axis. 
        elif keys[pygame.K_RIGHT]:
            var_params_dict['c'][0] += steps_dict_constants['c']

            updates_dict['update_screen'], updates_dict['update_spiral'],\
            updates_dict['update_line'], updates_dict['shift_coords'] = True, True, True, True

    
    if not algorithm_mode:    
        
        
        if keys[pygame.K_x]:
            
            # Right movement of the line
            if keys[pygame.K_RIGHT]:

                var_params_dict['x'] += steps_dict_constants['x']           

                updates_dict['update_screen'], updates_dict['update_line'] = True, True

            # Left movement of the line
            elif keys[pygame.K_LEFT]:
                var_params_dict['x'] -= steps_dict_constants['x']

                updates_dict['update_screen'], updates_dict['update_line'] = True, True

        elif keys[pygame.K_w]:
            
            # Increase angular velocity `w`    
            if keys[pygame.K_UP]:
                var_params_dict['w'] += steps_dict_constants['w']

                updates_dict['update_screen'], updates_dict['update_spiral'] = True, True

            # Decrease angular velocity `w`  
            elif keys[pygame.K_w] and keys[pygame.K_DOWN]:

                var_params_dict['w'] -= steps_dict_constants['w']

                updates_dict['update_screen'], updates_dict['update_spiral'] = True, True

          
        elif keys[pygame.K_k]:
            
            # Increase initial spiral angle coefficient `k`
            if keys[pygame.K_UP]:

                var_params_dict['k'] += steps_dict_constants['k']


                if const_params_dict['k'] + var_params_dict['k'] >= 4:         
                    var_params_dict['k'] = 0

                updates_dict['update_screen'], updates_dict['update_spiral'] = True, True


            # Decrease initial spiral angle coefficient `k`
            elif keys[pygame.K_DOWN]:

                var_params_dict['k'] -= steps_dict_constants['k']

                if const_params_dict['k'] + var_params_dict['k'] <= 0:         
                    var_params_dict['k'] = 4

                updates_dict['update_screen'], updates_dict['update_spiral'] = True, True

        
        elif keys[pygame.K_v]:
            
            # Increase spiral radius velocity `v`
            if keys[pygame.K_UP]:
                var_params_dict['v'] += steps_dict_constants['v']            


                updates_dict['update_screen'], updates_dict['update_spiral'] = True, True

            # Decrease spiral radius velocity `v`
            elif keys[pygame.K_DOWN]:           

                if const_params_dict['v'] + var_params_dict['v'] > 0:
                    var_params_dict['v'] -= steps_dict_constants['v']

                    updates_dict['update_screen'], updates_dict['update_spiral'] = True, True


        
        elif keys[pygame.K_t]:
            
            # Increase time `t`
            if keys[pygame.K_UP]:
                var_params_dict['t'] += steps_dict_constants['t']            

                updates_dict['update_screen'], updates_dict['update_spiral'] = True, True

            # Decrease time `t`
            elif  keys[pygame.K_DOWN]:           

                if const_params_dict['t'] + var_params_dict['t'] > 0:
                    var_params_dict['t'] -= steps_dict_constants['t']

                    updates_dict['update_screen'], updates_dict['update_spiral'] = True, True
                    
    return const_params_dict, var_params_dict, steps_dict_constants, updates_dict, algorithm_mode



def handle_shift_key_commands(event, updates_dict, const_params_dict, var_params_dict, mode_statuses_dict):
     
    # Turn the direction of the spiral
    if event.type == pygame.KEYDOWN:
        
        updates_dict['update_screen'] = True
        
        if (pygame.key.get_mods() & pygame.KMOD_SHIFT) and event.key == pygame.K_w:
            const_params_dict['w'] *= -1

            var_params_dict['w'] *= -1

            updates_dict['update_spiral'] = True 


        # Reset variables to their initial values
        elif (pygame.key.get_mods() & pygame.KMOD_SHIFT):
            
            if event.key == pygame.K_r:

                var_params_dict['t'], var_params_dict['v'], \
                var_params_dict['w'], var_params_dict['x'], \
                var_params_dict['k'], var_params_dict['l'], \
                var_params_dict['c'],var_params_dict['deg'] = t_additional, v_additional, w_additional,\
                                                              x_additional, k_additional, l_additional, [0, 0], deg_additional

                const_params_dict['w'] = w

                mode_dict_keys = mode_statuses_dict.keys()
                mode_dict_default_values = iter([background_mode, algorithm_mode, algorithm_data_mode,\
                                                 t_diagram_mode, vertical_line_mode,spiral_mode,\
                                                 y_axis_intersects, line_intersects, parameters_mode, True, derivatives_mode])

                for key in  mode_statuses_dict.keys():
                    mode_statuses_dict[key][1] = next(mode_dict_default_values)

                updates_dict['update_spiral'], updates_dict['update_line'], updates_dict['reset_background'] = True, True, True
            
            keys = pygame.key.get_pressed()
            
            # Change the degree of the spiral curve
            if keys[pygame.K_e]:
               
                if keys[pygame.K_UP]:
                    var_params_dict['deg'] += 1

                elif keys[pygame.K_DOWN]:
                    var_params_dict['deg'] -= 1

                updates_dict['update_spiral'] = True
            
            
    return updates_dict, const_params_dict, var_params_dict, mode_statuses_dict

def handle_ctrl_commands(event, updates_dict, mode_statuses_dict):
           
    updates_dict['is_turn_off'] = None
    updates_dict['is_t_diagram_change'] = False
    
    if event.type == pygame.KEYDOWN:
        
        mods = pygame.key.get_mods()
        updates_dict['update_screen'] = True
        
        if (mods & pygame.KMOD_CTRL)  and event.key == pygame.K_a:
            
            if not mode_statuses_dict['T-diagram'][1]:
                init_state = mode_statuses_dict['Algorithm mode'][1]
                mode_statuses_dict['Algorithm mode'][1] = False if init_state else True

                if init_state:
                    updates_dict['is_turn_off'] = True

                if mode_statuses_dict['Algorithm mode'][1]:
                    mode_statuses_dict['T-diagram'][1] = False
                
                # Set the layers to True
                for mode, (_, boolean) in mode_statuses_dict.items():
                    if mode not in ['Algorithm mode', 'T-diagram', 'Algorithm data mode','Modes layer']:
                        if not boolean:
                            mode_statuses_dict[mode][1] = True 
                        
        elif (mods & pygame.KMOD_CTRL) and event.key == pygame.K_t:
            
            if not mode_statuses_dict['Algorithm mode'][1]:
                mode_statuses_dict['T-diagram'][1] = not mode_statuses_dict['T-diagram'][1]
                updates_dict['is_t_diagram_change'] = True 

                if mode_statuses_dict['T-diagram'][1]:
                 
                    mode_statuses_dict['Algorithm mode'][1] = False
                    mode_statuses_dict['Vertical line'][1] = True
                    mode_statuses_dict['Derivatives'][1] = False
                    mode_statuses_dict['Y-intersects'][1] = True
                    mode_statuses_dict['Line-intersects'][1] = True
                
        if not mode_statuses_dict['Algorithm mode'][1]:
            if event.key == pygame.K_l:
                mode_statuses_dict['Vertical line'][1] = not mode_statuses_dict['Vertical line'][1]

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
                
            elif event.key == pygame.K_d:
                mode_statuses_dict['Derivatives'][1] = not mode_statuses_dict['Derivatives'][1]
                if mode_statuses_dict['Derivatives'][1]:
                    mode_statuses_dict['Y-intersects'][1] = False
                    mode_statuses_dict['Line-intersects'][1] = False
                
    return updates_dict, mode_statuses_dict



def handle_algorithm_mode_controls(event, algorithm_variables_dict, t_mth_aproxim_list, updates_dict):

    n = algorithm_variables_dict['n']
    m = algorithm_variables_dict['m']
    total_n = algorithm_variables_dict['total_n']

    keys = pygame.key.get_pressed()
   
    if event.type == pygame.KEYDOWN:
        updates_dict['update_screen'] = True
        
        if keys[pygame.K_n] and keys[pygame.K_UP]:


            if n+1 <= total_n:

                algorithm_variables_dict['n'] +=1
                algorithm_variables_dict['m'] = 0

                t_mth_aproxim_list.clear()

               

        elif keys[pygame.K_n] and keys[pygame.K_DOWN]:

            if n-1 > 0:
                algorithm_variables_dict['n'] -=1
                algorithm_variables_dict['m'] = 0

                t_mth_aproxim_list.clear()
           
        elif keys[pygame.K_m] and keys[pygame.K_UP]:

            algorithm_variables_dict['m'] +=1


        elif keys[pygame.K_m] and keys[pygame.K_DOWN]:

            if m-1 >= 0:
                algorithm_variables_dict['m'] -=1
 
            
    return algorithm_variables_dict, updates_dict
