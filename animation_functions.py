import pygame 
import numpy as np

from formula_functions import *

def create_background(background_surface,screen_width, screen_height, units, length, bg_color, font_small, after_stop = False):
    
    background_surface.fill(bg_color)

    line_color = (200,200,200)
    center_point = (screen_width/2, screen_height/2)

    # Coordinate x-line parameters
    x_line_start = 0
    x_line_end = screen_width
    
    #Coordinate y-line parameters
    y_line_start = 0
    y_line_end = screen_height
    
    # Height of the numbers lines
    y_line = screen_height/2
    
    x_line = screen_width/2
    

    
    pygame.draw.line(background_surface, color=line_color, start_pos=(x_line_start, y_line),
                         end_pos = (x_line_end, y_line), width=2)
    
    pygame.draw.line(background_surface, color=line_color, start_pos=(x_line, y_line_start),
                         end_pos = (x_line, y_line_end), width=2)

    pygame.draw.circle(background_surface, color='darkgrey', center=center_point, radius=4)
    
    # Upper and lower bounds of the vertical divisions of the x-axis
    vertical_line_start = y_line - 5
    vertical_line_end = y_line + 5
    
    # Upper and lower bounds of the horizontal divisions of the y-axis
    horizontal_line_start = x_line - 5
    horizontal_line_end = x_line + 5
    
    
    number_y = vertical_line_end + 15
     
    number_x = horizontal_line_end + 15
        
   
    half_units = (units)/2

    for i in range(int(half_units)):
        
        neg_number = int((half_units)-i)
        pos_number = int(half_units - neg_number)
        draw_x_axis_values(background_surface, screen_width, screen_height,
                i, length, x_line_start,vertical_line_start,
                vertical_line_end, line_color, font_small, half_units, number_y, pos_number, neg_number)
        
        draw_y_axis_values(background_surface, screen_width, screen_height,
                i, length, y_line_start,horizontal_line_start,
                horizontal_line_end, line_color,font_small, half_units,number_x,pos_number, neg_number)



def draw_x_axis_values(background_surface, screen_width, screen_height,
                i, length, x_line_start,vertical_line_start,
                vertical_line_end, line_color,font_small, half_units,number_y,pos_number, neg_number):
    
    vertical_line_x_neg = x_line_start + i*length
    vertical_line_x_pos = screen_width/2 + i*length

    #Draw unit lines for negative x-axis
    pygame.draw.line(background_surface, color = line_color, start_pos=(vertical_line_x_neg, vertical_line_start),
                 end_pos = (vertical_line_x_neg, vertical_line_end), width=1)  

    #Draw unit lines for positive x-axis
    pygame.draw.line(background_surface, color = line_color, start_pos=(vertical_line_x_pos, vertical_line_start),
                 end_pos = (vertical_line_x_pos, vertical_line_end), width=1)  

    #Draw zero
    if i == 0:
        pos_number_text = font_small.render(f'{pos_number}', True, line_color)
        background_surface.blit(pos_number_text, (vertical_line_x_pos-15,number_y-4))
        
    else:
        #Draw negative numbers
        neg_number_text = font_small.render(f'-{neg_number}', True, line_color)
        background_surface.blit(neg_number_text, (vertical_line_x_neg-12,number_y-4)) 

        #Draw positive numbers
        pos_number_text = font_small.render(f'{pos_number}', True, line_color)
        background_surface.blit(pos_number_text, (vertical_line_x_pos-5,number_y-4))

    
    
def draw_y_axis_values(background_surface, screen_width, screen_height,
                i, length, y_line_start,horizontal_line_start,
                horizontal_line_end, line_color,font_small, half_units,number_x,pos_number, neg_number):
    
    horizontal_line_y_neg = screen_height/2 + i*length
    horizontal_line_y_pos = screen_height/2 - i*length

    #Draw unit lines for negative y-axis
    pygame.draw.line(background_surface, color = line_color, start_pos=(horizontal_line_start, horizontal_line_y_neg),
             end_pos = (horizontal_line_end, horizontal_line_y_neg), width=1)

    #Draw unit lines for positive y-axis
    pygame.draw.line(background_surface, color = line_color, start_pos=(horizontal_line_start, horizontal_line_y_pos),
             end_pos = (horizontal_line_end, horizontal_line_y_pos), width=1)

    if i >=1:
       
        #Draw negative numbers
        neg_number_text = font_small.render(f'-{pos_number}', True, line_color)
        background_surface.blit(neg_number_text, (number_x-46,horizontal_line_y_neg-4)) 

        #Draw positive numbers
        neg_number_text = font_small.render(f'{pos_number}', True, line_color)
        background_surface.blit(neg_number_text, (number_x-46,horizontal_line_y_pos-4))
        
        
            
def x_transform(x, half_screen_width,length):
    
    return x* length + half_screen_width

def x_inverse_transform(x, half_screen_width,length):
    
    return (x - half_screen_width) / length

def y_transform(y, half_screen_height,length):
    
    return -y * length + half_screen_height

def transform_to_t_diagram(x, half_screen_width, half_screen_height, length):
    
    x = x_inverse_transform(x, half_screen_width, length)
    x = y_transform(x, half_screen_height, length)
    
    return x

def draw_vertical_line(line_layer, half_screen_width, half_screen_height, length, half_units,x_axis_value=1):
    
    line_layer.fill((0, 0, 0, 0))
    
    x_up, y_up  = x_transform(x_axis_value, half_screen_width, length),x_transform(half_units, half_screen_width, length)
    x_down, y_down = x_transform(x_axis_value, half_screen_width, length),x_transform(-half_units, half_screen_width, length)
    
    pygame.draw.aalines(line_layer, 'blue',  False, [(x_up, y_up), (x_down, y_down)])
    
       
def calc_spiral_coord(t=1 ,v=1, w=1, k=0) -> tuple:
    
    theta_0 = k * np.pi/2

    lin_space = (0, t)
    
    num = 3000

    T = np.linspace(*lin_space, num)
    
    angles = np.array([theta_0 + t * w for t in T])
    radiuses = np.array([v * t for t in T])
    
    x = radiuses * np.cos(angles)
    y = radiuses * np.sin(angles)

    return x, y, T 

def calc_y_intersects_t(t, w, k) -> list:
    
    is_bigger = False
    t_list = []
    
    
    if abs(w) == 0:
        is_bigger = True
  
    n = 1
    
    while not is_bigger:
        curr_t = get_nth_intersect(n, k, w)
        
        if curr_t <= t:
            t_list.append(curr_t)
            n += 1
        else:
            is_bigger = True
            
    return t_list


def calc_line_intersections_t(t_nth_list, x, v, w, k, correction_mech=False, f_binary=False, accuracy=5, i=200) -> list:
    
    t_mth_list = []
    for t in t_nth_list:
        curr_t_mth = get_mth_aproximation(t, x, v, w, k, correction_mech=correction_mech, i=i, f_binary=f_binary,accuracy=accuracy)
        t_mth_list.append(curr_t_mth)
        
    return t_mth_list


def calc_single_t_aproxim(v, w, k, t, half_screen_width, half_screen_height, length, transform=True):
    x = get_x_coord(v, w, k, t)
    y = get_y_coord(v, w, k, t)
    
    if transform:
        x = x_transform(x, half_screen_width, length)
        y = y_transform(y, half_screen_height, length)

    return x, y


def draw_spiral(spiral_layer, half_screen_width, half_screen_height,length,t=1, v=1,w=1,k=0, t_diagram_mode=False):
    
    spiral_layer.fill((0, 0, 0, 0))
    

    if w != 0:
        x_spiral, y_spiral, T = calc_spiral_coord(t=t ,v=v, w=w, k=k)

        x_spiral = [x_transform(x, half_screen_width, length) for x in x_spiral]
        y_spiral = [y_transform(y, half_screen_height, length) for y in y_spiral]

        for i in range(len(x_spiral) -1):
            curr_sp_point_x, curr_sp_point_y = x_spiral[i], y_spiral[i]
            
            if (0 <=abs(curr_sp_point_x)<=half_screen_width * 2) and \
               (0 <=abs(curr_sp_point_y)<=half_screen_height * 2): 
                
                next_sp_point_x, next_sp_point_y = x_spiral[i+1], y_spiral[i+1]
                if not t_diagram_mode:
                    pygame.draw.aalines(spiral_layer, 'red',  False, [(curr_sp_point_x, curr_sp_point_y), \
                                                                      (next_sp_point_x, next_sp_point_y)])
                else:
                 
                    curr_t_point = T[i]
                    curr_t_point = x_transform(curr_t_point, half_screen_width, length)
               
                    next_t_point = T[i+1]
                    next_t_point= x_transform(next_t_point, half_screen_width, length)
                    
                    backward_curr_sp_x = transform_to_t_diagram(curr_sp_point_x, half_screen_width, half_screen_height, length)
                    backward_next_sp_x = transform_to_t_diagram(next_sp_point_x, half_screen_width, half_screen_height, length)
                    
                    pygame.draw.aalines(spiral_layer, 'red',  False, [(curr_t_point, backward_curr_sp_x), \
                                                                      (next_t_point, backward_next_sp_x)])
             
                    pygame.draw.aalines(spiral_layer, 'blue',  False, [(curr_t_point, curr_sp_point_y), \
                                                                      (next_t_point, next_sp_point_y)])
        if t_diagram_mode:
            
            
            last_t = x_transform(T[-1], half_screen_width, length)
            
            last_rad_vec =  T[-1] * v
            last_rad_vec = y_transform(last_rad_vec, half_screen_height, length)
            
            # Draw hipotenuse
            start_point = (x_transform(T[0], half_screen_width, length), y_transform(0, half_screen_height, length))
            end_point = (last_t, last_rad_vec)
            pygame.draw.aalines(spiral_layer, 'green',  False, [start_point, end_point])
            
            # Draw spiral radius vector
            start_pos = (last_t, y_transform(0 , half_screen_height, length)) 
            end_pos = (last_t, last_rad_vec)
            
            draw_vector(spiral_layer,start_pos, end_pos, color='black' )
                                                                          
                
                
                
def draw_dots(layer, half_screen_width, half_screen_height, length, t_list, v, w, k, color, t_diagram=False):
    
    layer.fill((0, 0, 0, 0))
    if t_list:
        theta_0 = k * np.pi/2

        for t in t_list:
            angle = theta_0 + w * t
            radius_vec = v * t
            
            x = radius_vec * np.cos(angle)
            y = radius_vec * np.sin(angle)
            
            x = x_transform(x, half_screen_width, length)
            y = y_transform(y, half_screen_height, length)
            
            if not t_diagram:
            
                pygame.draw.circle(layer, color=color, center=(x, y), radius=4)
                
            else:
                
                t_trans = x_transform(t, half_screen_width, length)
                x_new = transform_to_t_diagram(x, half_screen_width, half_screen_height, length)
             
                pygame.draw.circle(layer, color=color, center=(t_trans, y), radius=4)
                pygame.draw.circle(layer, color=color, center=(t_trans, x_new), radius=4)                
    
        
def blit_layers(win, mode_statuses_dict, bg_color):
    win.fill(bg_color)
    
    for layer, boolean in mode_statuses_dict.values():
        if boolean and layer is not None:
            win.blit(layer, (0, 0))
        
def show_radius_vector_step(algorithm_layer, t_mth_aproxim_list, m, v, w, k,x_line,
                       half_screen_width, half_screen_height, length,
                       color, draw_leg_and_hip=False):
    
    curr_t = t_mth_aproxim_list[m]


    x, y = calc_single_t_aproxim(v, w, k, curr_t, half_screen_width, half_screen_height, length)

    start_pos, end_pos = (half_screen_width, half_screen_height), (x, y)

    draw_vector(algorithm_layer, start_pos, end_pos, color=color)
    
    # Shows the step to construct the current radius vector based on the previous radius vector
    if draw_leg_and_hip:
        
        if m+1 <= len(t_mth_aproxim_list):
        
            x_line = x_transform(x_line, half_screen_width, length)

            next_t = t_mth_aproxim_list[m+1]
            next_x, next_y = calc_single_t_aproxim(v, w, k, next_t, half_screen_width, half_screen_height, length)


            # Draw horizontal leg
            pygame.draw.aalines(algorithm_layer, '#F2D9B2',  False, [(x, y), (x_line, y)])

            # Draw a part of the hipotenuse
            pygame.draw.aalines(algorithm_layer, '#F2D9B2',  False, [(next_x, next_y), (x_line, y)])

            # A point on the spiral curve
            pygame.draw.circle(algorithm_layer, color='red', center=(next_x, next_y), radius=4)

            # A crosspoint between horizontal leg and the hipotenuse 
            pygame.draw.circle(algorithm_layer, color='blue', center=(x_line, y), radius=4)
        
        
def draw_algorithm_steps(algorithm_layer, t_nth_list, v, w, k, x, t_mth_aproxim_list, algorithm_variables_dict, 
                        half_screen_width, half_screen_height, length,
                         accuracy=5, curr_rad_vec_color='black', previous_rad_vec_color='lightgreen'):

    algorithm_layer.fill((0, 0, 0, 0))
    
    algorithm_variables_dict['total_n'] = len(t_nth_list) # Stores now many are the y-intersection points
  
    m = np.copy(algorithm_variables_dict['m'])

    if t_nth_list:
        
        if algorithm_variables_dict['n']  == 0:
            y_intersect_t = t_nth_list[0]
            algorithm_variables_dict['n']+=1
        else: 
            y_intersect_t = t_nth_list[algorithm_variables_dict['n'] -1]
        
        # Create list with interesection point aproximations and store it.
        if not t_mth_aproxim_list:
     
            zero_intersect_t = get_mth_aproximation(y_intersect_t, x, v, w, k, i=1, accuracy=accuracy, correction_mech=False, f_binary=False)
            t_mth_aproxim_list.append(zero_intersect_t)
            
            # Show current radius-vector
            show_radius_vector_step(algorithm_layer, t_mth_aproxim_list, m, v, w, k,x,
                               half_screen_width, half_screen_height, length,
                               curr_rad_vec_color)
        
        else:
            if m +1 > len(t_mth_aproxim_list):
                
                
                next_t = get_mth_aproximation(y_intersect_t, x, v, w, k, i=m+1, correction_mech=False, f_binary=False)
                t_mth_aproxim_list.append(next_t)
                
                # Show previous radius vector if it exists
                if m -1>= 0:
                
                    show_radius_vector_step(algorithm_layer, t_mth_aproxim_list, m-1, v, w, k,x,
                                       half_screen_width, half_screen_height, length,
                                       previous_rad_vec_color, draw_leg_and_hip=True)
                
 
                # Show current radius-vector
                show_radius_vector_step(algorithm_layer, t_mth_aproxim_list, m, v, w, k,x,
                                   half_screen_width, half_screen_height, length,
                                   curr_rad_vec_color)

                
            else:
              
                # Show previous radius vector if it exists
                if m -1>= 0:
                    show_radius_vector_step(algorithm_layer, t_mth_aproxim_list, m-1, v, w, k,x,
                                       half_screen_width, half_screen_height, length,
                                       previous_rad_vec_color, draw_leg_and_hip=True)
                    
                # Show current radius-vector
                show_radius_vector_step(algorithm_layer, t_mth_aproxim_list, m, v, w, k,x,
                                   half_screen_width, half_screen_height, length,
                                   curr_rad_vec_color)

            
            
    return t_mth_aproxim_list, algorithm_variables_dict

def draw_vector(layer, start_pos, end_pos, color=(255, 255, 255)):
  

    pygame.draw.aaline(layer, color, start_pos, end_pos)

    angle = np.arctan2(end_pos[1] - start_pos[1], end_pos[0] - start_pos[0])

    arrow_length = 10
    arrow_angle = np.pi / 6 


    arrow1 = (end_pos[0] - arrow_length * np.cos(angle - arrow_angle),
              end_pos[1] - arrow_length * np.sin(angle - arrow_angle))
    arrow2 = (end_pos[0] - arrow_length * np.cos(angle + arrow_angle),
              end_pos[1] - arrow_length * np.sin(angle + arrow_angle))

 
    pygame.draw.aaline(layer, color, end_pos, arrow1)
    pygame.draw.aaline(layer, color, end_pos, arrow2)

    