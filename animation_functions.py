import pygame 
import numpy as np


def create_background(background_surface,screen_width, screen_height, units, length, bg_color, font_small, after_stop = False):

    line_color = (200,200,200)
    center_point = (screen_width/2, screen_height/2)

    markers = []   
    
    
    # Coordinate x-line parameters
    x_line_start = 0
    x_line_end = screen_width
    
    #Coordinate y-line parameters
    y_line_start = 0
    y_line_end = screen_height
    
    # Height of the numbers lines
    y_line = screen_height/2
    
    x_line = screen_width/2
    
    markers.append({
        'receiver_x': x_line_end,
        'receiver_y': y_line,
    })
    
    
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
        
    screen_objects = {
    'x_line_start': x_line_start,
    'vertical_line_start': vertical_line_start,
    'vertical_line_end': vertical_line_end,
    'x_line_end': x_line_end,
    'y_line': y_line,
    'vertical_line_x': [],
    'numbers': [],
    'signals_start_positions': {},
    'spaceship_last_position': None
    }
  
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

    return background_surface, markers, screen_objects



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
    
    #Draw negative numbers
    neg_number_text = font_small.render(f'-{neg_number}', True, line_color)
    background_surface.blit(neg_number_text, (vertical_line_x_neg-12,number_y-4)) 
    
    #Draw positive numbers
    pos_number_text = font_small.render(f'{pos_number}', True, line_color)
    background_surface.blit(pos_number_text, (vertical_line_x_pos-12,number_y-4))

    
    
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
        if i <10:
            #Draw negative numbers
            neg_number_text = font_small.render(f'-{pos_number}', True, line_color)
            background_surface.blit(neg_number_text, (number_x-50,horizontal_line_y_neg)) 

            #Draw positive numbers
            neg_number_text = font_small.render(f'{pos_number}', True, line_color)
            background_surface.blit(neg_number_text, (number_x-50,horizontal_line_y_pos))

        else:
            #Draw negative numbers
            neg_number_text = font_small.render(f'-{pos_number}', True, line_color)
            background_surface.blit(neg_number_text, (number_x-57,horizontal_line_y_neg)) 

            #Draw positive numbers
            neg_number_text = font_small.render(f'{pos_number}', True, line_color)
            background_surface.blit(neg_number_text, (number_x-57,horizontal_line_y_pos))
            
def x_transform(x, screen_width,length):
    return x* length + screen_width/2

def y_transform(y, screen_height,length):
    return -y * length + screen_height /2


def draw_vertical_line(line_layer, screen_width, screen_height, length, units,x_axis_value=1):
    half_units = units/2
    x_up, y_up  = x_transform(x_axis_value, screen_width, length),x_transform(half_units, screen_width, length)
    x_down, y_down = x_transform(x_axis_value, screen_width, length),x_transform(-half_units, screen_width, length)
    
    pygame.draw.aalines(line_layer, 'blue',  False, [(x_up, y_up), (x_down, y_down)])
    
    
       
def calc_spiral_coord(screen_width, screen_height, length, units, v=1, w=1, k=0):
    
    theta_0 = k * np.pi/2
    
    half_units = units /2
    
    # N = half_units/(v*2*np.pi)
    
    # Needed time t for one rotation
    rotation_t = 2 * np.pi/(abs(w))
    
    
    
    one_rotation_rad_vec_len = v * rotation_t
    
    N = half_units / one_rotation_rad_vec_len
    
    max_spiral_vector_length = np.sqrt(screen_width ** 2 + screen_height ** 2)/length
    
#     print('max_spiral_vector_length: ', max_spiral_vector_length)
#     print('max_spiral_vector_t: ', max_spiral_vector_length,max_spiral_vector_length/v )
    
#     print('rotation_t: ', rotation_t)
#     print('one_rotation_rad_vec_len: ', one_rotation_rad_vec_len)
    max_t = max_spiral_vector_length/N
    # print('Max t: ', max_t)
    lin_space = (0, max_t)
    
    num = int(max_t*100)
    
    # print('num: ', num)
    # print('N: ', N)
    T = np.linspace(*lin_space, num)
    # print('Len T before: ', len(T))
    T = np.array([t for t in T if t * v < max_spiral_vector_length])
    # print('Len T after: ', len(T))
    # print('lin_space: ', lin_space)
    # print('Len lin_space: ', len(lin_space))
    # print('len T: ', len(T))
    # print(T)
    
    angles = np.array([theta_0 + t * w for t in T])
    radiuses = np.array([v * t for t in T])
    
    x = radiuses * np.cos(angles)
    y = radiuses * np.sin(angles)
    
    return x, y

def draw_spiral(spiral_layer, screen_width, screen_height,length,units, v=1,w=1,k=0):
    
    x_spiral, y_spiral = calc_spiral_coord(screen_width, screen_height,length,units, v=v,w=w,k=k)
    
    x_spiral = [x_transform(x, screen_width, length) for x in x_spiral]
    y_spiral = [y_transform(y, screen_height, length) for y in y_spiral]
    
    for i in range(len(x_spiral) -1):
        curr_sp_point_x, curr_sp_point_y = x_spiral[i], y_spiral[i]
        next_sp_point_x, next_sp_point_y = x_spiral[i+1], y_spiral[i+1]
        pygame.draw.aalines(spiral_layer, 'red',  False, [(curr_sp_point_x, curr_sp_point_y), (next_sp_point_x, next_sp_point_y)])