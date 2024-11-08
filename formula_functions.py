import numpy as np
# from Data_classes.data_processing import DataProcessing

def D_bin(k):
    return (1 + (-1) ** np.floor(k+1))/2


def W_bin(w):
    return (1 - w / abs(w))/2


def B_bin(k):
    return np.ceil(k) - np.floor(k)

def L_bin(x_line, w, v, k):
    
    zero_point_t = abs(x_line)/v
    curr_theta_angle = k * np.pi/2 + w * zero_point_t
    curr_x = v* zero_point_t * np.cos(curr_theta_angle)
    
    curr_x_sign = curr_x / abs(X_bin(curr_x))    
    curr_x_sign = 1 if curr_x_sign > 0 else -1
    
    x_line_sign = x_line/abs(X_bin(x_line))    
    x_line_sign = 1 if x_line_sign > 0 else -1
    
    x_product = curr_x_sign * x_line_sign

    return 0 ** (1 - x_product)


def get_delta_theta_plus(k):
    
    D_coeff = D_bin(k)
    
    return (np.pi/2) * (np.floor(k+1) - k + D_coeff)
    
    

def get_delta_theta(w, k):
    
    W_coeff = W_bin(w)
    B_coeff = B_bin(k)
    
    delta_plus = get_delta_theta_plus(k)
    
    return W_coeff * B_coeff * (np.pi - 2 * delta_plus) + delta_plus
    
    

def X_bin(x):
    return (x ** (0 ** abs(x) - 1)) ** -1

def get_y_coord(v, w, k, prev_t):
    return v * prev_t * np.sin(k*np.pi/2 + w*prev_t)



def get_x_coord(v, w, k, prev_t):
    return v * prev_t * np.cos(k*np.pi/2 + w*prev_t)



def get_nth_deg_x_derivative(deg,t, v,w,k):
    theta = k*np.pi/ 2 + w * t
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)
    
    trig_derivatives_cycle = [sin_theta, cos_theta, -sin_theta, -cos_theta]
    nth_der = deg%4
    next_nth = (deg+1) % 4
    
    nth_cos_deriv = trig_derivatives_cycle[nth_der]
    nth_sin_deriv = trig_derivatives_cycle[next_nth]
    
    return v * w ** (deg-1) * (deg * nth_cos_deriv + w*t * nth_sin_deriv)
    # return cos_theta

def get_nth_deg_y_derivative(deg, t, v, w, k):
    theta = k*np.pi/ 2 + w * t
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)
    
    trig_derivatives_cycle = [sin_theta, cos_theta, -sin_theta, -cos_theta]
    nth_der = deg%4
    prev_nth = (deg-1) % 4

    nth_cos_deriv = trig_derivatives_cycle[nth_der]
    nth_sin_deriv = trig_derivatives_cycle[prev_nth]
    
    return  v * w ** (deg-1) * ( deg *  nth_sin_deriv + w * t * nth_cos_deriv)
    

def A_coeff(x_line, w, v, k, y):

    x_coeff = X_bin(x_line)

    return (-1) * (x_line/abs(x_coeff)) * (w / abs(w)) * (y/abs(y))

# def rad_vec_magnitude(deg_x, deg_y, w, v, k, t)

#     theta = k * np.pi/2 + w * t 
    
#     x = get_nth_deg_x_derivative(deg_x, t_0, v, w, k)
#     y= get_nth_deg_y_derivative(deg_y, t_0, v, w, k)
    
    
    
    


def get_nth_intersect(data_processing, n, k, w):

    delta_theta = get_delta_theta(w, k)
  
    return (delta_theta + (n-1) * np.pi) / abs(w)





def get_mth_aproximation(data_processing, t_nth, i=200, accuracy=5, down_direction = False, correction_mech=False, f_binary=False):


    deg_x, deg_y = data_processing.get_curr_param('deg')
    v = data_processing.get_curr_param('v')
    w = data_processing.get_curr_param('w')
    k = data_processing.get_curr_param('k')
    x_line = data_processing.get_curr_param('x')
    
    t_0 = np.copy(t_nth)
    init_theta_angle = k * np.pi/2

    init_y = get_nth_deg_y_derivative(deg_y, t_0, v, w, k)

    # a_coeff = float(round(A_coeff(x_line, w, v, k, init_y),5))
    a_coeff = A_coeff(x_line, w, v, k, init_y)


    last_t = np.copy(t_0)



    for _ in range(1,i):

        curr_x = get_nth_deg_x_derivative(deg_x, t_0, v, w, k)
        curr_y= get_nth_deg_y_derivative(deg_y, t_0, v, w, k)

        if not down_direction:
            c = abs(x_line) - abs(curr_x)

            a = np.sqrt(x_line**2 + curr_y**2)

            # b = v*t_0 # Current radius vector
            b = np.sqrt(curr_x ** 2 + curr_y**2)

            cos_delta_phi = (a ** 2 + b**2 - c ** 2)/(2 * a * b)



            if abs(cos_delta_phi) > 1:

                cos_delta_phi = 1

            delta_phi = np.arccos(cos_delta_phi)

            curr_t = (a_coeff * delta_phi) / abs(w)

            if c == 0:

                t_0 +=curr_t*(-1)

            else:
                '(x_line/abs(x_line))*'
                t_0 += (c/abs(c))*curr_t 

            statement = f'{t_0:.{accuracy}f}' == f'{last_t:.{accuracy}f}'

            if statement:

                return t_0

            last_t = np.copy(t_0)

        else:
     
            phi_0 = np.arctan(curr_y/curr_x)

      
            new_y =  np.tan(phi_0) *x_line

            new_rad_vec_length = np.sqrt(x_line ** 2 + new_y ** 2)

            t_0 = new_rad_vec_length / v

            
            statement = f'{t_0:.{accuracy}f}' == f'{last_t:.{accuracy}f}'

            if statement:

                return t_0

            last_t = np.copy(t_0)
            # curr_x = get_nth_deg_x_derivative(deg_x, t_0, v, w, k)
            
    return last_t