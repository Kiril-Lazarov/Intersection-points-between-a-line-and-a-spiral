import pygame 
import numpy as np

from formula_functions import *


def create_background(background_surface,screen_width, screen_height, units, length, bg_color, font_small, after_stop = False):
    


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

def y_transform(y, half_screen_height,length):
    
    return -y * length + half_screen_height


def draw_vertical_line(line_layer, half_screen_width, half_screen_height, length, half_units,x_axis_value=1):
    
    line_layer.fill((0, 0, 0, 0))
    
    x_up, y_up  = x_transform(x_axis_value, half_screen_width, length),x_transform(half_units, half_screen_width, length)
    x_down, y_down = x_transform(x_axis_value, half_screen_width, length),x_transform(-half_units, half_screen_width, length)
    
    pygame.draw.aalines(line_layer, 'blue',  False, [(x_up, y_up), (x_down, y_down)])
    
    
       
def calc_spiral_coord(t=1 ,v=1, w=1, k=0):
    
    theta_0 = k * np.pi/2

    lin_space = (0, t)
    
    num = 3000

    T = np.linspace(*lin_space, num)
    
    angles = np.array([theta_0 + t * w for t in T])
    radiuses = np.array([v * t for t in T])
    
    x = radiuses * np.cos(angles)
    y = radiuses * np.sin(angles)
    
    
    
    return x, y 

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

def draw_spiral(spiral_layer, half_screen_width, half_screen_height,length,t=1, v=1,w=1,k=0):
    
    spiral_layer.fill((0, 0, 0, 0))
    
    if w != 0:
        x_spiral, y_spiral = calc_spiral_coord(t=t ,v=v, w=w, k=k)

        x_spiral = [x_transform(x, half_screen_width, length) for x in x_spiral]
        y_spiral = [y_transform(y, half_screen_height, length) for y in y_spiral]

        for i in range(len(x_spiral) -1):
            curr_sp_point_x, curr_sp_point_y = x_spiral[i], y_spiral[i]
            
            if (0 <=abs(curr_sp_point_x)<=half_screen_width * 2) and \
               (0 <=abs(curr_sp_point_y)<=half_screen_height * 2): 
                
                next_sp_point_x, next_sp_point_y = x_spiral[i+1], y_spiral[i+1]
                pygame.draw.aalines(spiral_layer, 'red',  False, [(curr_sp_point_x, curr_sp_point_y), (next_sp_point_x, next_sp_point_y)])
                
                
                
def draw_dots(y_axis_intersects_layer, half_screen_width, half_screen_height, length, t_list, v, w, k):
    
    y_axis_intersects_layer.fill((0, 0, 0, 0))
    if t_list:
        theta_0 = k * np.pi/2

        for t in t_list:
            angle = theta_0 + w * t
            radius_vec = v * t
            
            x = radius_vec * np.cos(angle)
            y = radius_vec * np.sin(angle)
            
            x = x_transform(x, half_screen_width, length)
            y = y_transform(y, half_screen_height, length)
            
            pygame.draw.circle(y_axis_intersects_layer, color='black', center=(x, y), radius=4)
    
        
def blit_layers(win, layers_list, bg_color):
    win.fill(bg_color)
    for layer in layers_list:
        win.blit(layer, (0, 0))