import pygame 
import numpy as np
from scipy.integrate import quad

from formula_functions import *


def create_background(background_surface, screen_width, screen_height, length, center_point, bg_color, font_small):
    
    '''
    Creates and visualizes the coordinate system.
    '''
    
    background_surface.fill(bg_color)

    line_color = (200,200,200)
 
    # Coordinate x-line parameters
    x_line_start = 0
    x_line_end = screen_width
    
    #Coordinate y-line parameters
    y_line_start = 0
    y_line_end = screen_height
    
    # Height of the numbers lines
    y_line = center_point[1]
    
    # Width of the numbers lines
    x_line = center_point[0]
    

    
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
    
    # Positions of the numbers relative to the corresponding axis line.
    number_y = vertical_line_end + 15
    number_x = horizontal_line_end + 15
        
    
    # Number of numbers that need to be displayed on the screen.
    pos_x_axis_nums_count = int(np.ceil((screen_width - center_point[0])/length))
    neg_x_axis_nums_count = int(np.ceil(center_point[0]/length))
    pos_y_axis_nums_count = int(np.ceil(center_point[1]/length))
    neg_y_axis_nums_count = int(np.ceil(screen_height - center_point[1]/length))


    
    #Draw positive x-axis numbers
    if pos_x_axis_nums_count >= 0:    
        
        for i in range(pos_x_axis_nums_count):

            draw_x_axis_pos_values(background_surface, center_point[0], screen_width, screen_height,
                                   i, length, x_line_start,vertical_line_start, vertical_line_end,
                                   line_color, font_small, number_y)
            
    # Draw negative x-axis numbers 
    if neg_x_axis_nums_count >= 0:
           
        for i in range(neg_x_axis_nums_count):
            draw_x_axis_neg_values(background_surface, center_point[0], screen_width, screen_height,
                                i, length, x_line_start,vertical_line_start, vertical_line_end, line_color,
                               font_small, number_y)

        
    #Draw positive y-axis numbers
    if pos_y_axis_nums_count >= 0:
        
        for i in range(pos_y_axis_nums_count):
            
            draw_y_axis_pos_values(background_surface, center_point[1], screen_width, screen_height,
                                   i, length, y_line_start,horizontal_line_start, horizontal_line_end, 
                                   line_color,font_small,number_x)
        
    #Draw negative y-axis numbers
    if neg_y_axis_nums_count >=0:
        
        for i in range(neg_y_axis_nums_count):

            draw_y_axis_neg_values(background_surface, center_point[1], screen_width, screen_height,
                    i, length, y_line_start,horizontal_line_start,
                    horizontal_line_end, line_color,font_small, number_x) 

            
def draw_x_axis_pos_values(background_surface, center_point_x, screen_width, screen_height,
                i, length, x_line_start,vertical_line_start,
                vertical_line_end, line_color,font_small,number_y):
    
    font_height = font_small.get_height()
    
    
    vertical_line_x_pos = center_point_x + i*length
   
    
    if vertical_line_x_pos <= screen_width:
        
        #Draw unit lines for positive x-axis
        pygame.draw.line(background_surface, color = line_color, start_pos=(vertical_line_x_pos, vertical_line_start),
                     end_pos = (vertical_line_x_pos, vertical_line_end), width=1)  

        #Draw zero
        if i == 0:
            pos_number_text = font_small.render(f'{i}', True, line_color)
            background_surface.blit(pos_number_text, (vertical_line_x_pos-(font_height/1.73) ,number_y-(font_height/6.5)))

        else:
            #Draw positive numbers
            pos_number_text = font_small.render(f'{i}', True, line_color)
            background_surface.blit(pos_number_text, (vertical_line_x_pos-(font_height/5.2),number_y-(font_height/6.5)))



            
            
def draw_x_axis_neg_values(background_surface, center_point_x, screen_width, screen_height,
                            i, length, x_line_start,vertical_line_start, vertical_line_end, line_color,
                           font_small,number_y):
        
    font_height = font_small.get_height()
    
    vertical_line_x_neg = center_point_x - i*length

    
    if vertical_line_x_neg >= 0:
        #Draw unit lines for negative x-axis
        pygame.draw.line(background_surface, color = line_color, start_pos=(vertical_line_x_neg, vertical_line_start),
                     end_pos = (vertical_line_x_neg, vertical_line_end), width=1)  
        
        if i != 0:
            #Draw negative numbers
            neg_number_text = font_small.render(f'-{i}', True, line_color)
            background_surface.blit(neg_number_text, (vertical_line_x_neg-(font_height/2.16),number_y-(font_height/6.5))) 

    
    
def draw_y_axis_pos_values(background_surface, center_point_y, screen_width, screen_height,
                i, length, y_line_start,horizontal_line_start,
                horizontal_line_end, line_color,font_small, number_x):
    
    font_height = font_small.get_height()

    horizontal_line_y_pos = center_point_y - i*length

    #Draw unit lines for positive y-axis
    pygame.draw.line(background_surface, color = line_color, start_pos=(horizontal_line_start, horizontal_line_y_pos),
             end_pos = (horizontal_line_end, horizontal_line_y_pos), width=1)

    if i >=1:

        #Draw positive numbers
        neg_number_text = font_small.render(f'{i}', True, line_color)
        background_surface.blit(neg_number_text, (number_x-(font_height/0.56),horizontal_line_y_pos-(font_height/6.5)))
        
        
def draw_y_axis_neg_values(background_surface, center_point_y, screen_width, screen_height,
                i, length, y_line_start,horizontal_line_start,
                horizontal_line_end, line_color,font_small, number_x):
    
    font_height = font_small.get_height()
    
    horizontal_line_y_neg = center_point_y + i*length


    #Draw unit lines for negative y-axis
    pygame.draw.line(background_surface, color = line_color, start_pos=(horizontal_line_start, horizontal_line_y_neg),
             end_pos = (horizontal_line_end, horizontal_line_y_neg), width=1)


    if i >=1:
       
        #Draw negative numbers
        neg_number_text = font_small.render(f'-{i}', True, line_color)
        background_surface.blit(neg_number_text, (number_x-(font_height/0.56),horizontal_line_y_neg-(font_height/6.5))) 

        
        
            
def x_transform(x, curr_screen_width,length):
    
    return x* length + curr_screen_width


def x_inverse_transform(x, curr_screen_width,length):
    
    return (x - curr_screen_width) / length


def y_transform(y, curr_screen_height,length):
    
    return -y * length + curr_screen_height

def y_inverse_transform(y, curr_screen_height,length):
    
    return (y - curr_screen_height)/length

def transform_to_t_diagram(x, curr_screen_width, curr_screen_height, length):
    
    x = x_inverse_transform(x, curr_screen_width, length)
    x = y_transform(x, curr_screen_height, length)
    
    return x

def calc_x_derivative(t, v, w, k):
    
    theta = k* np.pi/2 + w * t
    
    return v*( np.cos(theta) - w* t * np.sin(theta))


def calc_y_derivative(t, v, w, k):
    
    theta = k* np.pi/2 + w * t
    
    return v*( np.sin(theta) + w* t * np.cos(theta))





def calc_spiral_length(t, v, w, k):

    a = 0

    def f(t):
       
        dx_dt = calc_x_derivative(t, v, w, k)
        dy_dt = calc_y_derivative(t, v, w, k)
        
        return np.sqrt(dx_dt**2 + dy_dt **2)

    length, _ = quad(f, a, t)
    
    return length

      
def calc_spiral_coord(deg=[0, 0], t=1 ,v=1, w=1, k=0) -> tuple:
    
    deg_x, deg_y = deg
    
    lin_space = (0, t)
    
    num = 300

    T = np.linspace(*lin_space, num)
    
    x = np.array([get_nth_deg_x_derivative(deg_x, t, v,w,k) for t in T])
    y = np.array([get_nth_deg_y_derivative(deg_y, t, v,w,k) for t in T])
    
    return x, y, T 

def calc_y_intersects_t(deg_x, deg_y , t, v, w, k, x_line, a, b, 
                        steps_change, zero_missing_point_mode,
                        general_solution) -> list:
    
    if not steps_change:
  
        is_bigger = False
        t_list = []
      
        if abs(w) == 0:
            is_bigger = True

        n = 0
 
        while not is_bigger:
            curr_t = get_nth_intersect(n, deg_x, deg_y, a, b, v, w, k, x_line, 
                                       zero_missing_point_mode, general_solution)
         
            if abs(curr_t) <= abs(t):
                t_list.append(curr_t)
     
                n += 1
            else:
                is_bigger = True

        return t_list
    
    return []

def calc_line_intersections_t(deg_x, deg_y, v, w, k, x_line, b_line, a_slope, accuracy,
                              steps_change, zero_missing_point_mode, general_solution, x_l_x_s_diff_mode, t_nth_list) -> list:
    
    if not steps_change:
        
        t_mth_list = []
        
        for index,t_nth in enumerate(t_nth_list):
   
            curr_t_mth = get_mth_approximation(deg_x, deg_y, v, w, k, x_line, b_line, a_slope, accuracy,
                                               zero_missing_point_mode, general_solution,x_l_x_s_diff_mode, t_nth, index)
                
            t_mth_list.append(curr_t_mth)

        return t_mth_list
    
    return []


def calc_single_t_aproxim(center_point_width, center_point_height, deg_x, deg_y, length, v, w, k, mth_t, transform=True):
  
    x = get_nth_deg_x_derivative(deg_x, mth_t, v, w, k)
    y = get_nth_deg_y_derivative(deg_y, mth_t, v, w, k)
    
    
    if transform:
        x = x_transform(x, center_point_width, length)
        y = y_transform(y, center_point_height, length)

    return x, y

def get_orthogonal_slope(slope):
    slope += 90
    slope *= np.pi/180
    return round(np.tan(slope), 13)

        
def draw_inclined_line(layer, slope_a, b, center_point_width, center_point_height, 
                     screen_width, screen_height, length, color):
    
    b_x = x_transform(0, center_point_width, length)
    b_y = y_transform(b, center_point_height, length)

    if slope_a != 0:            

        x_up_gen_line = center_point_width + b_y / slope_a
        x_down_gen_line = center_point_width  + (screen_height - b_y)/ -slope_a

        pygame.draw.aalines(layer, color,  False, [(x_up_gen_line, 0), (x_down_gen_line, screen_height)])

    else:

        pygame.draw.aalines(layer, color,  False, [(0, b_y), (screen_width, b_y)])
        
        
def draw_vertical_line(layer, x_axis_value, center_point_width, screen_height, length, color):

    x_up  = x_down = x_transform(x_axis_value, center_point_width, length)

    y_up  = y_transform(0, screen_height, length)
    y_down = y_transform(screen_height, 0, length)      


    pygame.draw.aalines(layer, color,  False, [(x_up, y_up), (x_down, y_down)])
        
        
def draw_line(line_layer, screen_height, screen_width, half_screen_width, half_screen_height, 
                a, b, x, length, center_point_width, center_point_height, slope_a,
                t_diagram, general_solution, rotated_background):

    line_layer.fill((0, 0, 0, 0))

    if not t_diagram:
        
        # Draw a vertical line if not general solution mode
        if not general_solution:

            color = 'blue'
            draw_vertical_line(line_layer, x, center_point_width, screen_height, length, color)

        # Draw line with a slope and a constant
        else:

            if rotated_background:
                
                # Draw rotated y-axis 

                color = (255, 255, 154) # Light yellow
                draw_inclined_line(line_layer, slope_a, 0, center_point_width, center_point_height, 
                     screen_width, screen_height, length, color)
                
                # Calculate the rotated x-axis                
                orthogonal_slope = get_orthogonal_slope(a)

                draw_inclined_line(line_layer, orthogonal_slope, 0, center_point_width, center_point_height, 
                     screen_width, screen_height, length, color)
            
            
            # Draw the line            
            draw_inclined_line(line_layer, slope_a, b, center_point_width, center_point_height, 
                         screen_width, screen_height, length, 'blue')


    else:
   
        y_left = y_right = y_transform(x, center_point_height, length)
        
        x_left, x_right = 0, screen_width
     
 
        pygame.draw.aalines(line_layer, 'blue',  False, [(x_left, y_left), (x_right, y_right)])
    
    

def draw_spiral(spiral_layer, half_screen_width, half_screen_height, 
                center_point_width, center_point_height, length,
                deg, t, v, w, k, spiral_coordinates, t_diagram):

    spiral_layer.fill((0, 0, 0, 0))


    x_spiral, y_spiral, T = calc_spiral_coord(deg=deg,t=t ,v=v, w=w, k=k)

    spiral_coordinates['x'] = x_spiral[-1]
    spiral_coordinates['y'] = y_spiral[-1]

    # Euclidеan distances list
    rad_vec_distances = np.sqrt(x_spiral**2 + y_spiral**2)
    rad_vec_distances = [y_transform(y, center_point_height, length) for y in rad_vec_distances]


    # Transform the x and y spiral coords into the screen coordinate system
    x_spiral = [x_transform(x, center_point_width, length) for x in x_spiral]
    y_spiral = [y_transform(y, center_point_height, length) for y in y_spiral]

    for i in range(len(x_spiral) -1):

        curr_sp_point_x, curr_sp_point_y = x_spiral[i], y_spiral[i]
        next_sp_point_x, next_sp_point_y = x_spiral[i+1], y_spiral[i+1]

        # Check if the points are within the screen boundaries.
        if not t_diagram:
            if (0 <=abs(curr_sp_point_x)<=half_screen_width * 2) and \
               (0 <=abs(curr_sp_point_y)<=half_screen_height * 2):

                pygame.draw.aalines(spiral_layer, 'red',  False, [(curr_sp_point_x, curr_sp_point_y), \
                                                                  (next_sp_point_x, next_sp_point_y)])
        else:

            curr_t_point = T[i]
            curr_t_point = x_transform(curr_t_point, center_point_width, length)

            next_t_point = T[i+1]
            next_t_point= x_transform(next_t_point, center_point_width, length)

            backward_curr_sp_x = transform_to_t_diagram(curr_sp_point_x, center_point_width, center_point_height, length)
            backward_next_sp_x = transform_to_t_diagram(next_sp_point_x, center_point_width, center_point_height, length)

            # Euclidean distances 
            curr_rad_vec_dist = rad_vec_distances[i]
            next_rad_vec_dist = rad_vec_distances[i+1]

            # Check if the points are within the screen boundaries.
            if (0 <=abs(curr_t_point)<=half_screen_width * 2) and \
               (0 <=abs(curr_sp_point_y) <=half_screen_height * 2 or \
                0 <=abs(backward_next_sp_x) <= half_screen_height * 2 or \
                0 <= abs(next_rad_vec_dist) <= half_screen_height * 2): 


                pygame.draw.aalines(spiral_layer, 'red',  False, [(curr_t_point, backward_curr_sp_x), \
                                                                  (next_t_point, backward_next_sp_x)])

                pygame.draw.aalines(spiral_layer, 'blue',  False, [(curr_t_point, curr_sp_point_y), \
                                                                  (next_t_point, next_sp_point_y)])

                pygame.draw.aalines(spiral_layer, 'green',  False, [(curr_t_point, curr_rad_vec_dist), \
                                                                   (next_t_point, next_rad_vec_dist)])
                    
                    
        if t_diagram:
            
            deg_x, deg_y = deg

            last_t = x_transform(T[-1], center_point_width, length)
            
            last_rad_vec =  T[-1] * v
            
            last_spiral_x = get_nth_deg_x_derivative(deg_x, T[-1], v,w, k)
            last_spiral_y = get_nth_deg_y_derivative(deg_y, T[-1], v,w, k)
            
            last_rad_vec = np.sqrt(last_spiral_x**2 + last_spiral_y ** 2)
            last_rad_vec = y_transform(last_rad_vec, center_point_height, length)

            
            # Draw spiral radius vector
            start_pos = (last_t, y_transform(0 , center_point_height, length)) 
            end_pos = (last_t, last_rad_vec)            
            draw_vector(spiral_layer,start_pos, end_pos, color='black')
                                                                          
                
                
                
def draw_dots(deg_x, deg_y, v, w, k, length,
              const_center_point, var_center_point,
              t_diagram, mode_statuses_dict, t_list, layer):
    
    color = 'black' if layer == 'Y-intersects' else 'purple'
    
    layer = mode_statuses_dict[layer][0]
    layer.fill((0, 0, 0, 0))
    
    center_point_width = const_center_point[0] + var_center_point[0]
    center_point_height = const_center_point[1] + var_center_point[1]
    
    if t_list:
        theta_0 = k * np.pi/2

        for t in t_list:
 
            x = get_nth_deg_x_derivative(deg_x, t, v, w, k)
            y = get_nth_deg_y_derivative(deg_y, t, v, w, k)
            
            x = x_transform(x, center_point_width, length)
            y = y_transform(y, center_point_height, length)
            
            if not t_diagram:
            
                pygame.draw.circle(layer, color=color, center=(x, y), radius=4)
                
            else:
                
                t_trans = x_transform(t, center_point_width, length)
                x_new = transform_to_t_diagram(x, center_point_width, center_point_height, length)
             
                pygame.draw.circle(layer, color=color, center=(t_trans, y), radius=4)
                pygame.draw.circle(layer, color=color, center=(t_trans, x_new), radius=4) 
    
def get_line_boundary_points(length, angle, x, y):
    
    x_leg = length * np.cos(angle) 
    y_leg = length * np.sin(angle)
    
    front_xx = x + x_leg 
    front_xy = y - y_leg
    
    back_xx = x - x_leg
    back_xy = y + y_leg
    
    return front_xx, front_xy, back_xx, back_xy    
    
                
def draw_derivatives(layer, center_point_width, center_point_height, 
                    length, deg_x, deg_y, t, v, w, k,
                    screen_width, screen_height, t_diagram,
                    derivative, derivative_slopes):  
    layer.fill((0, 0, 0, 0))
    if derivative:

        


        dx_dt_color = (255, 0, 0)
        dy_dt_color = (0, 0, 255)
        dy_dx_color = (0, 255, 0)

        theta = k*np.pi/2 + w*t
    
        # Current point spiral coords 
        x = get_nth_deg_x_derivative(deg_x, t, v, w, k)
        y = get_nth_deg_y_derivative(deg_y, t, v, w, k)
        
        # Position of the central point for the dy_dx 
        y_x = np.sqrt(x**2 + y ** 2)

        # Derivatives in this point 
        dx_dt = get_nth_deg_x_derivative(deg_x+1, t, v, w, k)
        dy_dt = get_nth_deg_y_derivative(deg_y+1, t, v, w, k)
        
        # Spiral derivative
        dy_dx = dy_dt/ E(dx_dt)
        

        x_der_angle = np.arctan(dx_dt)
        y_der_angle = np.arctan(dy_dt)
        
        spiral_der_angle = np.arctan(dy_dx)
        
        derivative_slopes['dx_dt'] = x_der_angle * 180/ np.pi
        derivative_slopes['dy_dt'] = y_der_angle * 180/ np.pi
        derivative_slopes['dy_dx'] = spiral_der_angle * 180/ np.pi

        x = x_transform(x, center_point_width, length)
        y = y_transform(y, center_point_height, length)

        ll = 3* length
        
        colors = iter([dx_dt_color, dy_dt_color, dy_dx_color])

        if t_diagram:
            t_trans = x_transform(t, center_point_width, length)
            x_new = transform_to_t_diagram(x, center_point_width, center_point_height, length)
            
            y_x = y_transform(y_x, center_point_height, length)
            
            y_points = iter([x_new, y, y_x])
            
            for angle in [x_der_angle, y_der_angle, spiral_der_angle]:

                front_xx, front_xy, back_xx, back_xy = get_line_boundary_points(ll, angle, t_trans, next(y_points))
                pygame.draw.aalines(layer, next(colors),  False, [(back_xx,  back_xy), (front_xx, front_xy)])

            pygame.draw.circle(layer, color=dx_dt_color, center=(t_trans, x_new), radius=4)
            pygame.draw.circle(layer, color=dy_dt_color, center=(t_trans, y), radius=4)
            pygame.draw.circle(layer, color=dy_dx_color, center=(t_trans, y_x), radius=4)
        


        else:            
            
            # Draw derivatives         
            for angle in [x_der_angle, y_der_angle, spiral_der_angle]:
            
                front_xx, front_xy, back_xx, back_xy = get_line_boundary_points(ll, angle, x, y)

                pygame.draw.aalines(layer, next(colors),  False, [(back_xx, back_xy), (front_xx, front_xy)])
                
            pygame.draw.circle(layer, color='purple', center=(x, y), radius=4)
            
def get_angle(slope, degrees = False):
    if slope == 'inf':
        if degrees:
            return 90
        return np.pi/2
    if degrees:
        return np.arctan(slope) * 180/np.pi
    return np.arctan(slope)

        
def show_radius_vector_step(algorithm_layer, center_point_width, center_point_height, 
                            screen_width, screen_height, deg_x, deg_y, length, v, w, k, x_line, a_slope, b_line, 
                            t_mth_aproxim_list, n, m, color, general_solution, x_l_x_s_diff_mode, draw_leg_and_hip=False):

    curr_t = t_mth_aproxim_list[m]

    x, y = calc_single_t_aproxim(center_point_width, center_point_height, deg_x, deg_y, length, v, w, k, curr_t)

    start_pos, end_pos = (center_point_width, center_point_height), (x, y)
    x_line_1 = np.copy(x_line)
    x_line = x_transform(x_line, center_point_width, length)

    draw_vector(algorithm_layer, start_pos, end_pos, color=color)
    
    # Shows the step to construct the current radius vector based on the previous radius vector
    if draw_leg_and_hip:
        
        next_t = t_mth_aproxim_list[m+1]

        next_x, next_y = calc_single_t_aproxim(center_point_width, center_point_height, deg_x, deg_y, length, v, w, k, next_t)
  
        if m+1 <= len(t_mth_aproxim_list):
          
            
            if not general_solution:
                if not x_l_x_s_diff_mode:
                   
                    rad_vec_x, rad_vec_y = calc_single_t_aproxim(center_point_width, center_point_height, deg_x, deg_y, length, v, w, k, curr_t, transform=False)
                    next_rad_vec_x, next_rad_vec_y = calc_single_t_aproxim(center_point_width, center_point_height, deg_x, deg_y, length, v, w, k, next_t, transform=False) 
                    
                    slope = next_rad_vec_y/E(next_rad_vec_x)
                    angle = get_angle(slope)
                    
                    long_side = abs(rad_vec_y)/np.cos(np.pi/2 - abs(angle))
                    long_side_x = next_rad_vec_x/abs(E(next_rad_vec_x))*   long_side * np.cos(abs(angle))
                    long_side_y = next_rad_vec_y/abs(E(next_rad_vec_y))*long_side * np.sin(angle)
                    
                    long_side_x = x_transform(long_side_x, center_point_width, length)
                    long_side_y = y_transform(long_side_y, center_point_height, length)
                    
                    # Draw horizontal leg
                    pygame.draw.aalines(algorithm_layer, '#F2D9B2',  False, [(x, y), (long_side_x, y)])

                    # Draw a part of the hipotenuse
                    pygame.draw.aalines(algorithm_layer, '#F2D9B2',  False, [(next_x, next_y), (long_side_x, y)])
                    
       
                  
                    # pygame.draw.circle(algorithm_layer, color='green', center=(long_side_x, y), radius=4)
                    

                else:
                  
                    if n == 0:
                        
                        x_1, y_1 = calc_single_t_aproxim(center_point_width, center_point_height, deg_x, deg_y, length, v, w, k, curr_t, transform=False)
                        angle = abs(np.arctan(y_1/x_1))                      
                        
                
                        shifted_y = y_1/abs(E(y_1)) * np.tan(angle) * abs(x_line_1) 
                        shifted_y = y_transform(shifted_y, center_point_height, length)
                
                    # Draw horizontal leg
                    pygame.draw.aalines(algorithm_layer, '#F2D9B2',  False, [(x, y), (x_line, shifted_y)])

                    # Draw a part of the hipotenuse
                    pygame.draw.aalines(algorithm_layer, '#F2D9B2',  False, [(next_x, next_y), (x_line, shifted_y)])
                   

                # A point on the spiral curve
                pygame.draw.circle(algorithm_layer, color='red', center=(next_x, next_y), radius=4)

                # A crosspoint between horizontal leg and the hipotenuse 
                pygame.draw.circle(algorithm_layer, color='blue', center=(x_line, shifted_y), radius=4)
                
            else:
                # print('4')
                x, y = calc_single_t_aproxim(center_point_width, center_point_height, deg_x, deg_y, length, v, w, k,    
                                             curr_t, transform=False)
                
                next_x, next_y = calc_single_t_aproxim(center_point_width, center_point_height, deg_x, deg_y, length, v, w, 
                                                       k, next_t, transform=False)
                curr_vec_slope = next_y/E(next_x)
                
                x_intersect = -b_line/E(a_slope- curr_vec_slope)
                y_intersect = curr_vec_slope * x_intersect
            
                x, x_intersect = x_transform(x, center_point_width,length), x_transform(x_intersect, 
                                             center_point_width,length)
                
                y, y_intersect = y_transform(y, center_point_height,length), y_transform(y_intersect, 
                                             center_point_height,length)
                
                next_x, next_y = x_transform(next_x, center_point_width,length), y_transform(next_y, 
                                             center_point_height,length)
                
                # Draw horizontal leg
                pygame.draw.aalines(algorithm_layer, '#F2D9B2',  False, [(x, y), (x_intersect, y_intersect)])
                
                # Draw a part of the hipotenuse
                pygame.draw.aalines(algorithm_layer, '#F2D9B2',  False, [(next_x, next_y), (x_intersect, y_intersect)])

                # A point on the spiral curve
                pygame.draw.circle(algorithm_layer, color='red', center=(next_x, next_y), radius=4)
                
                # A crosspoint between horizontal leg and the hipotenuse 
                pygame.draw.circle(algorithm_layer, color='blue', center=(x_intersect, y_intersect), radius=4)
        
        
def draw_algorithm_steps(algorithm_layer, total_n, n, m, center_point_width, center_point_height,
                         screen_width, screen_height, length, deg_x, deg_y, v, w, k, x_line, b_line, a_slope, accuracy,
                         zero_missing_point_mode, general_solution, x_l_x_s_diff_mode, t_nth_list, t_mth_aproxim_list,
                         curr_rad_vec_color='black', 
                         previous_rad_vec_color='lightgreen'):

    algorithm_layer.fill((0, 0, 0, 0))
    
    total_n = len(t_nth_list) # Stores how many are the y-intersection points

    if t_nth_list:
    
        if n> len(t_nth_list)-1:
        
            n -= 1
        y_intersect_t = t_nth_list[n]
    
    
        # Create list with interesection point aproximations and store it.
        if not t_mth_aproxim_list:
       
           
            first_intersect_t = get_mth_approximation(deg_x, deg_y, v, w, k, x_line, b_line, a_slope, accuracy,
                                                      zero_missing_point_mode, general_solution, x_l_x_s_diff_mode, y_intersect_t, 0, i=1)
            t_mth_aproxim_list.append(first_intersect_t)
            
            # Show current radius-vector
            show_radius_vector_step(algorithm_layer, center_point_width, center_point_height, 
                                    screen_width, screen_height, deg_x, deg_y, length, v, w, k, x_line, a_slope, b_line,  
                                    t_mth_aproxim_list,  n, m, curr_rad_vec_color, general_solution, x_l_x_s_diff_mode)
        else:
            if m +1 > len(t_mth_aproxim_list):
                
            
                next_t = get_mth_approximation(deg_x, deg_y, v, w, k, x_line, b_line, a_slope, accuracy,
                                               zero_missing_point_mode, general_solution, x_l_x_s_diff_mode, y_intersect_t, n, 
                                               i=m+1)
                t_mth_aproxim_list.append(next_t)
                
                # Show previous radius vector if it exists
                if m -1>= 0:
               
                    show_radius_vector_step(algorithm_layer, center_point_width, center_point_height,  
                                            screen_width, screen_height, deg_x, deg_y, length, v, w, k, x_line, a_slope, 
                                            b_line, t_mth_aproxim_list,  n, m-1, previous_rad_vec_color, general_solution, 
                                            x_l_x_s_diff_mode, draw_leg_and_hip=True)
       
                # Show current radius-vector
                show_radius_vector_step(algorithm_layer, center_point_width, center_point_height, 
                                        screen_width, screen_height, deg_x, deg_y, length, v, w, k, x_line, a_slope, b_line,                                                                   t_mth_aproxim_list,  n, m, curr_rad_vec_color, general_solution, x_l_x_s_diff_mode)
                
            else:
              
                # Show previous radius vector if it exists
                if m -1>= 0:
           
                    show_radius_vector_step(algorithm_layer, center_point_width, center_point_height, 
                                            screen_width, screen_height, deg_x, deg_y, length, v, w, k, x_line, a_slope, b_line,
                                            t_mth_aproxim_list,  n, m-1, previous_rad_vec_color, general_solution, x_l_x_s_diff_mode, draw_leg_and_hip=True)
         
                # Show current radius-vector
                show_radius_vector_step(algorithm_layer, center_point_width, center_point_height, 
                                        screen_width, screen_height, deg_x, deg_y, length, v, w, k, x_line,a_slope, b_line, 
                                        t_mth_aproxim_list,  n, m, curr_rad_vec_color, general_solution, x_l_x_s_diff_mode)

    return t_mth_aproxim_list, total_n




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
    
def draw_circle_and_vector(data_processing, font_small):
    
    circle_layer = data_processing.mode_statuses_dict['Circle layer'][0]
    circle_layer.fill((0, 0, 0, 0))
    
    if data_processing.mode_statuses_dict['Circle layer'][1]:
    
        center_point_width, center_point_height = data_processing.get_curr_param('c')

        length = data_processing.get_curr_param('l') 

        k = data_processing.get_curr_param('k')
        
        w = data_processing.get_curr_param('w')
        
        theta_0 = k * (np.pi/2)

        pygame.draw.circle(circle_layer, color='green', center=(center_point_width, center_point_height), 
                           radius=length, width=1)
        
        start_pos = (center_point_width, center_point_height)
        end_pos = (center_point_width+length*np.cos(theta_0), center_point_height-length*np.sin(theta_0)) 
        
        draw_vector(circle_layer, start_pos, end_pos,color='black')
        
        # delta_theta = get_delta_theta(w, k, zero_missing_point=True) - np.pi/2
        
        delta_theta = get_delta_theta(w, k, zero_missing_point=True)
        
        theta_0 += delta_theta
        
        end_pos = (center_point_width+length*np.cos(theta_0), center_point_height-length*np.sin(theta_0)) 
     
        draw_vector(circle_layer, start_pos, end_pos,color='red')

    