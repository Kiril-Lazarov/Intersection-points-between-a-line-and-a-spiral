import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np
import math

def distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Create coordinate system
def create_field(figsize = (7,7), x_lim = (-20, 20), y_lim= (-20, 20)):
    plt.figure(figsize =figsize)  

    ax = plt.gca()
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['top'].set_visible(False)   
    
    ax.spines['right'].set_visible(False)
    ax.set_aspect('equal')
    plt.axis('equal')
    
    plt.xlim(*x_lim)
    plt.ylim(*y_lim)
    
    plt.xlabel('X')
    plt.ylabel('Y')
    
   
    ax.xaxis.set_label_coords(1.05, 0.5)
    ax.yaxis.set_label_coords(0.5, 1.05) 
    
    plt.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.2)
    
    return ax
    
def create_line(a,b, x_lim):
    x = np.linspace(*x_lim,500)
    y = a*x + b
    return x, y

def create_spiral(r_incr_velocity = 1, angle_velocity=1, init_angle=0):
    
    max_spiral_vector_length = np.sqrt(2* 20 ** 2)
    max_t = max_spiral_vector_length / r_incr_velocity
    lin_space = (0, max_t)
    
    T = np.linspace(*lin_space, 2000)
    
    x = [r_incr_velocity * time * np.cos(init_angle + time * angle_velocity) for time in T]
    y = [r_incr_velocity * time * np.sin(init_angle + time * angle_velocity) for time in T]
    
    return x, y

def get_line_vector_magnitude(x, a, b):
    y = a*x + b
    vec_magnitude = distance((0, 0), (x, y))
    
    return vec_magnitude

def get_angle(slope, degrees = False):
    if slope == 'inf':
        if degrees:
            return 90
        return np.pi/2
    if degrees:
        return np.arctan(slope) * 180/np.pi
    return np.arctan(slope)

# Calculates the minimum distance between the linear function and the center of the spiral.
def get_little_radius_vec(slope, constant):
    if slope == 'inf':
        return 0, np.pi/2
    if slope == 0:
        return constant, 0
    # The value of the x at y = 0
    x = -constant/slope
    angle = get_angle(slope)
    
 
    return abs(x * np.cos(np.pi/2 - abs(angle))), angle

def get_streched_unit_vector(x_length, s):
    return np.sqrt(x_length ** 2 + s **2)

def get_spiral_vec_coords(spiral_vec_magnitude,spiral_vec_velocity, angle_velocity, init_angle=0):
    # Т e времето за което спиралният вектор е достигнал съответната големина.
    # Чрез него ще намерим съответстващият ъгъл на завъртане на спиралата за тази големина на вектора
    T = spiral_vec_magnitude / spiral_vec_velocity
    spiral_angle = init_angle + T * angle_velocity
    
    x = spiral_vec_magnitude * np.cos(spiral_angle)
    y = spiral_vec_magnitude * np.sin(spiral_angle)
    
    # Връща началните координати на вектора - 0,0 - и крайните координати - x,y
    return 0, 0, x, y

def get_spiral_coords(t, spiral_radius_velocity, spiral_angle_velocity, init_spiral_angle):
    x = t * spiral_radius_velocity * np.cos(init_spiral_angle + t * spiral_angle_velocity)
    y = t * spiral_radius_velocity * np.sin(init_spiral_angle + t * spiral_angle_velocity)
    return x, y

def get_y_intersection_points_t(first_y_intersection_point, spiral_radius_velocity, 
                              spiral_angle_velocity, angle_diff,
                              y_lim):
    max_points_length = np.sqrt(y_lim[0]**2 + y_lim[1] ** 2)
    
    y_intersection_points_t = []

    first_intsc_point_t = abs(first_y_intersection_point)/spiral_radius_velocity

    
    additional_t = np.pi/ abs(spiral_angle_velocity)

    
    y_intersection_points_t.append(first_intsc_point_t)
    
    is_break = False
    
    while not is_break:
        first_intsc_point_t += additional_t

        if first_intsc_point_t * spiral_radius_velocity > max_points_length:
            is_break = True
        y_intersection_points_t.append(first_intsc_point_t)

    return y_intersection_points_t

def get_delta_coeff(a, b, y):
    return a / abs(a) * b / abs(b) * y/ abs(y) * -1



def calc_spiral_line_intersection_points(a, b, t, 
                               spiral_radius_velocity, 
                               init_spiral_angle, spiral_angle_velocity, 
                               min_distance, accuracy=5):
       
        
        input_spiral_vector = t * spiral_radius_velocity
        
        init_spiral_x = input_spiral_vector * np.cos(init_spiral_angle + t* spiral_angle_velocity)
        init_spiral_y = input_spiral_vector * np.sin(init_spiral_angle + t * spiral_angle_velocity)
        
        directional_coeff =get_delta_coeff(a, b, init_spiral_y)

        original_const_vector_length = np.copy(input_spiral_vector)


        const_vector_angle = init_spiral_angle + (original_const_vector_length / spiral_radius_velocity) * spiral_angle_velocity

        while True:
      
            last_spiral_vector = np.copy(float(f'{input_spiral_vector:.{accuracy}f}'))
            delta_angle = np.arctan(min_distance/input_spiral_vector) * directional_coeff if input_spiral_vector != 0 else None
            
            if delta_angle is not None and delta_angle <= np.pi/2:
                
                length_to_add = delta_angle / spiral_angle_velocity * spiral_radius_velocity
                
                curr_vector_angle = const_vector_angle - delta_angle

                input_spiral_vector = original_const_vector_length - length_to_add

                rotate_t = (curr_vector_angle/ spiral_angle_velocity)    

                new_x = input_spiral_vector * np.cos(rotate_t * spiral_angle_velocity)
                new_y = input_spiral_vector * np.sin(rotate_t * spiral_angle_velocity)

                new_spiral_vec_len = get_streched_unit_vector(new_x, new_y)


                input_spiral_vector = float(f'{new_spiral_vec_len * np.cos(delta_angle):.{accuracy}f}')


                if input_spiral_vector == last_spiral_vector:
          
                    if new_spiral_vec_len >= min_distance:
                        return new_x, new_y
                    return None, None
            else:
                return None, None

            
def rotate_y_intersection_points(a, b, y_intersection_points_t,spiral_radius_velocity, spiral_angle_velocity):
        
        rotated_y_intersection_points = []
        
        directional_coeff = a / abs(a)
        
        help_angle_to_y_axis =directional_coeff * np.pi/2 - get_angle(a)
    
        delta_t = help_angle_to_y_axis/ spiral_angle_velocity

        for t in y_intersection_points_t:
            new_t = t - delta_t
            rotated_y_intersection_points.append(new_t)
    
        return rotated_y_intersection_points
    
def get_quadrant(angle):
    if angle >= 2 * np.pi:
        raise ValueError('Angle must be between 0 and 2pi')
        
    if 0 <= angle < np.pi/2 or angle == 2 * np.pi:
        return 1
    if np.pi/2 <= angle < np.pi:
        return 2
    if np.pi<= angle < 3 *np.pi/2:
        return 3
    if 3 *np.pi/2 <= angle < 2 * np.pi:
        return 4

def get_initial_angle_to_y_axis(quadrant, spiral_angle_velocity, init_spiral_angle):
    start_angle = 0
    
    # Специални случаи за началният ъгъл, които изискват допълнителна логика
    if init_spiral_angle == 2 * np.pi:
        init_spiral_angle = 0
        
    if init_spiral_angle == np.pi/2 and spiral_angle_velocity <0:
        init_spiral_angle = -np.pi/2
        
    if init_spiral_angle == 3 * np.pi/2 and spiral_angle_velocity <0:
        init_spiral_angle = 5 * np.pi/2
        
    if init_spiral_angle == np.pi/2 and spiral_angle_velocity <0:

        init_spiral_angle = 3 * np.pi/2
    
    # Обикновени случаи
    if quadrant == 1:
        if spiral_angle_velocity > 0:
            angle_diff = np.pi/2 - init_spiral_angle

        elif spiral_angle_velocity < 0:
            angle_diff = np.pi/2 + init_spiral_angle

        
    elif quadrant == 2:
        if spiral_angle_velocity > 0:
            angle_diff = np.pi/2 +  (np.pi - init_spiral_angle)

            
        elif spiral_angle_velocity < 0:
            angle_diff = init_spiral_angle - np.pi/2

        
    elif quadrant == 3:
        if spiral_angle_velocity > 0:
            angle_diff = 3 * np.pi/2 - init_spiral_angle

            
        elif spiral_angle_velocity < 0:
            angle_diff = init_spiral_angle - np.pi/2

        
    else:
        if spiral_angle_velocity > 0:
            angle_diff = np.pi/2 + 2 * np.pi - init_spiral_angle

        
        elif spiral_angle_velocity <0:
            angle_diff = init_spiral_angle - 3*np.pi/2

            
    return angle_diff


def get_first_y_intersection_point(init_spiral_angle, spiral_angle_velocity, spiral_radius_velocity):

        quadrant = get_quadrant(init_spiral_angle)

        # Начален ъгъл и ъглова разлика между този начален ъгъл и игрек координатата. Тази начална ъглова
        # разлика ще се използва за определяне на времето t, за което спиралният вектор се завърта,
        # за да докосне за първи път ординатната ос.  
        angle_diff = get_initial_angle_to_y_axis(quadrant, spiral_angle_velocity, init_spiral_angle)

        t = angle_diff / spiral_angle_velocity
        directional_constant = abs(t)/ t

        y = t* spiral_radius_velocity * np.sin(directional_constant * init_spiral_angle + t * spiral_angle_velocity)
        
        return y, angle_diff
    
def get_rad_vec_params(x, y, w, init_angle):

    rad_vec_angle = np.arctan(y/x)

    rad_vec_t = rad_vec_angle/w - init_angle
    
    return rad_vec_angle, rad_vec_t



def draw_v_line(x, y):

    plt.plot([x, x], [0, y], color='blue', linestyle='-', linewidth=1)
    
    
    
def draw_h_line(x,y):
    plt.plot([0, x], [y, y], color='blue', linestyle='-', linewidth=1)
    
    

def draw_intersects(x, y):

    plt.scatter(x,0,c='blue',s=20)
    plt.scatter(0,y,c='blue',s=30)
    plt.scatter(x,y,c='blue',s=30)
    
    
    
def plot_objects(a, b, spiral_radius_velocity, 
                 spiral_angle_velocity, init_spiral_angle,
                 x_y_lim=((-20, 20),(-20, 20)),
                 only_line=False):
                 
    if init_spiral_angle < 0:
        raise ValueError('Init spiral angle must be non-negative value')
    if spiral_radius_velocity <= 0:
        raise ValueError('Spiral radius velocity must be positive value')
        
    y_lim = (-20, 20)
    
    min_distance, angle_to_line = get_little_radius_vec(a, b)
 
    create_field(x_lim=x_y_lim[0], y_lim=x_y_lim[1])
   
    x_line, y_line = create_line(a, b, (-20, 20))
  
    x_help_line, y_help_line = create_line(a, 0, y_lim)

    x_spiral, y_spiral = create_spiral(r_incr_velocity = spiral_radius_velocity, 
                                       init_angle = init_spiral_angle,
                                       angle_velocity = spiral_angle_velocity)
    
    line_angle = get_angle(a, degrees= False) + np.pi
   
    # Plot linear function
    plt.plot(x_line, y_line, color='blue', linewidth=1, linestyle='-')
    
    # Plot spiral
    plt.plot(x_spiral, y_spiral, color = 'red', linewidth = 1, linestyle = '-')
    
    if not only_line:
        
        # Help line
        plt.plot(x_help_line, y_help_line, color='green', linewidth=1, linestyle='-')

        if b >0:
            angle_to_line += np.pi/2

        elif b <0:
            angle_to_line -= np.pi/2

        first_y_intersection_point, angle_diff =  get_first_y_intersection_point(init_spiral_angle, spiral_angle_velocity, spiral_radius_velocity)

        y_intersection_points_t = get_y_intersection_points_t(first_y_intersection_point, 
                                                          spiral_radius_velocity, spiral_angle_velocity, 
                                                          angle_diff, y_lim)

        rotated_y_intscs_t = rotate_y_intersection_points(a, b, y_intersection_points_t,spiral_radius_velocity, spiral_angle_velocity)

        for t in y_intersection_points_t:
            plt.scatter(*get_spiral_coords(t, spiral_radius_velocity, spiral_angle_velocity, init_spiral_angle), color='black', s=20)

        real_intersects = []

        for t in rotated_y_intscs_t:
            plt.scatter(*get_spiral_coords(t, spiral_radius_velocity, spiral_angle_velocity, init_spiral_angle), color='green', s=20)
            curr_spiral_vector_length = t * spiral_radius_velocity
            x, y = calc_spiral_line_intersection_points(a, b, t, spiral_radius_velocity, 
                                        init_spiral_angle, spiral_angle_velocity, 
                                        min_distance, accuracy = 5)
            print('Index: ', rotated_y_intscs_t.index(t), end=' -> ')
            if (x, y) != (None, None):
                real_intersects.append([x, y])
            print(x, y)
        for x, y in real_intersects:
                plt.scatter(x, y, color='purple', s=20)

    plt.show()
    
    
def draw_algorithm(x, y, v, w, init_angle,ax,
                        include_axis_lines=True,
                        include_intersects=True,
                        draw_rad_vec=True,
                        only_result = False,
                        linspace_count = 2000,
                        steps_count=2,
                        x_text_coef = 2.5,
                        show_text = True):
    
    init_y = np.copy(y)
    
    a = 2.5
    
    plt.text(-0.6, -0.6, r'$O$', ha='center', va='top', color='black')
    
    if steps_count <2:
        raise ValueError('Steps count must be greater than one')
        
    if only_result == True:
        include_axis_lines, include_intersects, draw_rad_vec= False, False, False
                    
    plt.text(x, -init_y*0.1, r'$x_i = {:.2f}$'.format(x), ha='center', va='top', color='black')

    for i in range(steps_count):
     
        rad_vec_angle, rad_vec_t = get_rad_vec_params(x, y, w, init_angle)
        
        
        x_spiral_intersect = v * rad_vec_t * np.cos(rad_vec_angle)
        y_spiral_intersect = v * rad_vec_t * np.sin(rad_vec_angle)

        if i == 0 and steps_count ==2:
             
            arc = Arc((0, 0), 1.5*2, 1.5*2, angle=0, theta1=0, theta2=rad_vec_angle*180/np.pi, edgecolor='black')
            ax.add_patch(arc)
            
            theta_deg = rad_vec_angle * 180 / np.pi
            
            plt.text(1.8, 1.1, r'$\theta$', ha='right', va='center', color='black')
            plt.text(1, 3,r'$\vec{{R}}$', ha='right', va='center', color='black')
            plt.text(x_spiral_intersect, y_spiral_intersect+0.5,r'$I$', ha='right', va='center', color='black')
            plt.text(x_text_coef * x, init_y /2.1, rf'$\theta = ${theta_deg:.9f}', ha='right', va='center', color='black')


        if include_axis_lines:
        
            draw_h_line(x, y)
            draw_v_line(x, y)
            
        if include_intersects:
            draw_intersects(x, y)
            if i <4:
                letter = f'A_{{{i}}}'
                y_point = f'y_{{{i}}}'
                
                plt.text(x+0.7, y, rf'${letter}$', ha='right', va='center', color='black')
                plt.text(-0.7, y, rf'${y_point}$={y}', ha='right', va='center', color='black')

        if i < steps_count-1:
            
            if not only_result:
                plt.scatter(x_spiral_intersect,y_spiral_intersect,c='black',s=30)

            if draw_rad_vec:
                plt.quiver(0,0,x_spiral_intersect,y_spiral_intersect,angles = "xy", scale_units = "xy", scale = 1, linewidth = 0.01,color='green')
                plt.plot([x_spiral_intersect, x], [y_spiral_intersect, y], color='green', linestyle='dashed', linewidth=1)
                
        y = y_spiral_intersect
        
    if only_result:
        
        last_angle = rad_vec_angle *180/np.pi
        rad_vec_mag = rad_vec_t * v
        
        draw_v_line(x, init_y)
        draw_h_line(x, init_y)
        
        draw_h_line(x, y_spiral_intersect)
        
        draw_intersects(x, init_y)
        draw_intersects(x, y_spiral_intersect)
        
        plt.quiver(0,0,x,y_spiral_intersect,angles = "xy", scale_units = "xy", scale = 1, linewidth = 0.01,color='green')
        plt.scatter(x,y_spiral_intersect,c='black',s=30)
        
        if show_text:
   
            plt.text(-init_y*0.2, init_y, rf'$y_0$={init_y}', ha='right', va='center', color='black')

            plt.text(-init_y*0.2, y, rf'$y_{{{steps_count}}}$={y_spiral_intersect}', ha='right', va='center', color='black')

            plt.text(x_text_coef * x, init_y /2.1, rf'$\theta_{{{steps_count}}} = ${last_angle:.9f}', ha='right', va='center', color='black')

            plt.text(x_text_coef * x, init_y /2.6, rf'$t = ${rad_vec_t:.9f}', ha='right', va='center', color='black')

            plt.text(x_text_coef * x, init_y /3.2, rf'$\vec{{R}} = ${rad_vec_mag:.9f}', ha='right', va='center', color='black')

            plt.text(x_text_coef * x, init_y /4.2, rf'$y_{{{steps_count}}} = {y_spiral_intersect:.9f}$', ha='right', va='center', color='black')
        
    
def show_spiral_and_circle():    
    angle_velocity = 1/(2* np.pi)
    spiral_velocity = 2 / (2*np.pi)

    f = 6
    l = 2
    create_field(figsize=(f, f), x_lim=(-l, l), y_lim=(-l, l))
    v = 1 / (2*np.pi)
    w = 1/(2* np.pi)
    d_angles = np.linspace(0, 2*np.pi, 360, endpoint=False)
    t = d_angles / w
    x_circle = np.cos(t * w)
    y_circle = np.sin(t * w)

    x_spiral = np.cos(d_angles)+(d_angles*w ) * np.cos(d_angles)
    y_spiral = np.sin(d_angles)+(d_angles*w ) * np.sin(d_angles)

    plt.plot(x_circle, y_circle,  color = 'blue', linewidth = 1, linestyle = '-')
    plt.plot(x_spiral, y_spiral,  color = 'red', linewidth = 1, linestyle = '-')

#     const_time = (26.396396396396362 + 90) * np.pi/180 * w
#     x = (const_time* v) * np.cos(const_time * w)
#     y = ( const_time * v) * np.sin(const_time * w)

#     plt.scatter(x, y, color= 'black', s= 20)


    plt.show()