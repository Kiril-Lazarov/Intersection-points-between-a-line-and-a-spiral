import matplotlib.pyplot as plt
import numpy as np

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
    
    # Преместване на лейбълите на осите отстрани 
    ax.xaxis.set_label_coords(1.05, 0.5)
    ax.yaxis.set_label_coords(0.5, 1.05) 
    
    plt.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.2)
    
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
    if slope == 'inf' or slope == 0:
        return constant

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

def get_y_intersection_points(spiral_radius_velocity, spiral_angle_velocity, init_spiral_angle, y_lim):
    y_intersection_points = []

    if init_spiral_angle >= 2*np.pi:
        while init_spiral_angle >= 2*np.pi:
            init_spiral_angle-=2*np.pi

    
    start_angle = 0

    if np.pi/2 <=  init_spiral_angle < 3*np.pi/2:

        angle_diff = 3*np.pi /2 - init_spiral_angle
        start_angle = 3*np.pi /2
    elif init_spiral_angle >= 3*np.pi/2:

        angle_diff = np.pi /2 + (2 * np.pi  - init_spiral_angle)
        start_angle = np.pi /2
    elif 0<=init_spiral_angle<np.pi/2:

        angle_diff = np.pi/2 - init_spiral_angle
        start_angle = np.pi /2
        
    t = angle_diff / spiral_angle_velocity
    spiral_radius_magnitude = t * spiral_radius_velocity
    y_intersection_points.append([0, spiral_radius_magnitude * np.sin(start_angle)])

    if spiral_radius_magnitude< np.mean([abs(y_lim[0]), abs(y_lim[1])]):

        while spiral_radius_magnitude< np.mean([abs(y_lim[0]), abs(y_lim[1])]):
       
            start_angle += np.pi
            t = np.pi / spiral_angle_velocity
            spiral_radius_magnitude += t * spiral_radius_velocity
            y_intersection_points.append([0, spiral_radius_magnitude * np.sin(start_angle)])

      
    return y_intersection_points

def calc_angles_sequence_limit(b, input_spiral_vector, spiral_radius_velocity, 
                                    init_spiral_angle, spiral_angle_velocity, min_distance):
       
        init_spiral_x = input_spiral_vector * np.cos(input_spiral_vector/ spiral_radius_velocity* spiral_angle_velocity)
        init_spiral_y = input_spiral_vector * np.sin(input_spiral_vector/ spiral_radius_velocity * spiral_angle_velocity)

        original_const_vector_length = np.copy(input_spiral_vector)


        const_vector_angle = init_spiral_angle + (original_const_vector_length / spiral_radius_velocity) * spiral_angle_velocity

        while True:
      
            last_spiral_vector = np.copy(input_spiral_vector)
            delta_angle = np.arctan(min_distance/input_spiral_vector)
            # print('Delta angle: ', delta_angle*180/np.pi)
            
            if delta_angle <= np.pi/2:

                length_to_add = delta_angle / spiral_angle_velocity * spiral_radius_velocity

                if b > 0:
                    if init_spiral_y <0:
                        delta_angle *= -1
                        length_to_add *= -1
                elif b <0:
                    if init_spiral_y > 0:
                        delta_angle *= -1
                        length_to_add *= -1


                curr_vector_angle = const_vector_angle - delta_angle

                input_spiral_vector = original_const_vector_length - length_to_add

                rotate_t = (curr_vector_angle/ spiral_angle_velocity)    

                new_x = input_spiral_vector * np.cos(rotate_t * spiral_angle_velocity)
                new_y = input_spiral_vector * np.sin(rotate_t * spiral_angle_velocity)

                new_spiral_vec_len = get_streched_unit_vector(new_x, new_y)


                input_spiral_vector = new_spiral_vec_len * np.cos(delta_angle)


                if input_spiral_vector == last_spiral_vector:
                    if new_spiral_vec_len >= min_distance:
                        return new_x, new_y
                    return 0, 0
            else:
                return 0, 0
            

def calc_vertical_line_intersects(x_distance, input_spiral_vector_len, spiral_radius_velocity, 
                                    init_spiral_angle, spiral_angle_velocity):
    
    original_const_vector_length = np.copy(input_spiral_vector_len)
    
    init_angle =init_spiral_angle +  abs(input_spiral_vector_len) / spiral_radius_velocity*spiral_angle_velocity

    delta_angle = np.arctan(x_distance/input_spiral_vector_len)

    while True:
     
        last_spiral_vector = np.copy(abs(input_spiral_vector_len))

        delta_angle = np.arctan(x_distance/input_spiral_vector_len)
        curr_angle = init_angle - delta_angle
        length_to_add = delta_angle / spiral_angle_velocity * spiral_radius_velocity

        new_spiral_vector_len = abs(original_const_vector_length) - length_to_add
        rotate_t = curr_angle/spiral_angle_velocity


        new_x = new_spiral_vector_len * np.cos(curr_angle)
        new_y = new_spiral_vector_len * np.sin(curr_angle)

        new_spiral_vector_len = get_streched_unit_vector(new_x, new_y)

        if original_const_vector_length <0:
            input_spiral_vector_len = -new_spiral_vector_len*np.cos(delta_angle)

        elif original_const_vector_length >0:
            input_spiral_vector_len = new_spiral_vector_len*np.cos(delta_angle)
        if abs(input_spiral_vector_len) == last_spiral_vector:
                if new_spiral_vector_len >= abs(x_distance):
                    print(new_x, new_y)
                    break
                
def rotate_y_intersection_points(a, b, y_intersects,angle, init_spiral_angle, spiral_radius_velocity, spiral_angle_velocity, min_distance):
        
        updated_y_intersection_points = []
        
        real_intersection_points = []
        
        angle_diff = angle - np.pi/2
        t = angle_diff / spiral_angle_velocity
        

        
        for point in y_intersects:
            
            spiral_radius_magnitude = abs(point[1]) + t * spiral_radius_velocity
            new_t = spiral_radius_magnitude / spiral_radius_velocity
            curr_angle = init_spiral_angle + new_t * spiral_angle_velocity
            
            x = spiral_radius_magnitude * np.cos(curr_angle)
            y = spiral_radius_magnitude * np.sin(curr_angle)
        
            
            updated_y_intersection_points.append([x, y])
     
            index = y_intersects.index(point)
        
            spiral_vec_length = get_streched_unit_vector(x, y)

                
            new_x, new_y = calc_angles_sequence_limit(b, spiral_vec_length, spiral_radius_velocity, 
                                init_spiral_angle, spiral_angle_velocity, min_distance)

            plt.scatter(new_x, new_y, color= 'purple', s = 20)

            spiral_vec_length = get_streched_unit_vector(new_x, new_y)
            # real_intersection_points.append([new_x, new_y])

   
            real_intersection_points.append([0, 0])
                
        return updated_y_intersection_points, real_intersection_points
    