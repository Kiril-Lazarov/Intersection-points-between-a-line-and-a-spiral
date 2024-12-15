import numpy as np
# from Data_classes.data_processing import DataProcessing
# from animation_functions import 



def derivative_change(x_der_t0, x_der_y_zero):
    
    x_0_sign = x_der_t0/abs(X_bin(x_der_t0))

    x_t_sign = x_der_y_zero/abs(X_bin(x_der_y_zero))


    return (x_0_sign + x_t_sign)/X_bin(x_0_sign + x_t_sign)



def get_nth_deg_x_derivative(deg,t, v,w,k):
    theta = k*np.pi/ 2 + w * t
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)
    
    trig_derivatives_cycle = [sin_theta, cos_theta, -sin_theta, -cos_theta]
    nth_der = deg%4
    next_nth = (deg+1)%4
    
    nth_cos_deriv = trig_derivatives_cycle[nth_der]
    nth_sin_deriv = trig_derivatives_cycle[next_nth]
    
    result = v * (X_bin(w) ** (deg-1)) * (deg * nth_cos_deriv + w*t * nth_sin_deriv)

    return round(result, 13)


def get_nth_deg_y_derivative(deg, t, v, w, k):
    theta = k*np.pi/ 2 + w * t
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)
    
    trig_derivatives_cycle = [sin_theta, cos_theta, -sin_theta, -cos_theta]
    nth_der = deg%4
    prev_nth = (deg-1)%4

    nth_cos_deriv = trig_derivatives_cycle[nth_der]
    nth_sin_deriv = trig_derivatives_cycle[prev_nth]
    
    result = v * (X_bin(w) ** (deg-1)) * ( deg *  nth_sin_deriv + w * t * nth_cos_deriv)

    return  round(result, 13)

def get_rotation_coeff(b, x):
    product = (-1) * b * x
    
    return product/abs(X_bin(product))

def get_delta_k_rotated(a, b, x):
    
    delta_k_coeff = get_rotation_coeff(b, x)
    a_coeff = a/abs(X_bin(a))
    b_coeff = b/abs(X_bin(b))
    a_turn_on = a/X_bin(a)
    b_turn_on = b/X_bin(b)
    slope_angle = abs(np.arctan(a))
    expr = delta_k_coeff * 2 * (np.pi/2 - a_coeff*delta_k_coeff*slope_angle)/np.pi
    
    return (1-a_turn_on)*(-1) + a_turn_on*b_turn_on*expr + (1-b_turn_on)* 2 * (np.pi/2 - a_coeff*slope_angle)/np.pi\
            + (1-a_turn_on) * (1-b_turn_on)

def get_n_coeff(n):
    return n/X_bin(n)

def get_nth_intersect(data_processing, n, w,k, final_solution = False):
    
    a = data_processing.slope
    b = data_processing.get_curr_param('b')
    v = data_processing.get_curr_param('v')
    x_line = data_processing.get_curr_param('x')
    
    missing_point_mode = data_processing.mode_statuses_dict['Missing point'][1]
    
   
    if data_processing.mode_statuses_dict['General solution'][1]:
        k = np.copy(k)

        delta_k_rotated_angle = get_delta_k_rotated(a, b, x_line)

        k += delta_k_rotated_angle

    delta_theta = get_delta_theta(w, k, missing_point=missing_point_mode)
    
    if missing_point_mode:
        if n == 0:
            n+=1
  
        return (delta_theta + (n-1) * np.pi) / abs(X_bin(w))
    
    
    zero_y_t =  abs(x_line/X_bin(v))
    
    deg_x, deg_y  =  data_processing.get_curr_param('deg')

    kwx_coeff = KWX_line(k, w, x_line)
    k_sign = K_sign(k, x_line)
    
    # The x-derivative at t=0
    x_der_t0 = get_nth_deg_x_derivative(deg_x+1, 0, v, w, k)
    
    
    # The x-derivative at the zero y-intersection point
    x_der_y_zero = get_nth_deg_x_derivative(deg_x+1, zero_y_t, v, w, k)
    
    
    is_der_changed = derivative_change(x_der_t0, x_der_y_zero)
    
    # The length of the first y-intersection point radius vector
    x_max_dist = x_max_line(deg_y, delta_theta, x_line,v, w, k)
 

    result = x_max_dist* is_der_changed* (k_sign + kwx_coeff)*(1 - n/X_bin(n)) * zero_y_t\
                             + (n/X_bin(n))*(delta_theta + (n-1) * np.pi) / abs(w)
 
    return  result




def W_bin(w):
    return (1 - w / abs(X_bin(w)))/2


def B_bin(k):
    return np.ceil(k) - np.floor(k)



def KWX_line(k, w, x_line):
  
    k_1_koeff = 1 - (k-1)/X_bin(k-1)
    k_3_koeff = 1 - (k-3)/X_bin(k-3)
    
    x_w_pos_sum = x_line/abs(X_bin(x_line)) + w/abs(X_bin(w))
    
    x_w_neg_sum = x_line/abs(X_bin(x_line)) - w/abs(X_bin(w))

    return k_1_koeff * (x_w_neg_sum/X_bin(x_w_neg_sum)) + k_3_koeff * (x_w_pos_sum/X_bin(x_w_pos_sum))



def K_sign(k, x_line):
    k_coeff = ((k-1)/abs(X_bin(k-1))) * ((k-3)/abs(X_bin(k-3)))

    x_line_coeff = x_line/abs(X_bin(x_line))

    return np.floor((1 + k_coeff*x_line_coeff)/2)



def x_max_line(deg_y, delta_theta, x_line, v,w, k):
    
    t = delta_theta/abs(X_bin(w))
    
    first_rad_vec_length = get_nth_deg_y_derivative(deg_y, t, v, w, k)
    

    values_diff = abs(first_rad_vec_length) - abs(x_line)
    diff_sign = values_diff/ abs(X_bin(values_diff))
    
    return np.floor((1+diff_sign)/2)

def get_delta_theta_plus(k):
    
    D_coeff = (1 + (-1) ** np.floor(k+1))/2
    
    return (np.pi/2) * (np.floor(k+1) - k + D_coeff)

    

def get_delta_theta(w, k, missing_point=False):

    if not missing_point:
        b_bin = B_bin(np.floor(k)/2)
        w_bin= w/abs(X_bin(w))

        k_1 = (k-1)/ X_bin(k-1)
        k_3 = (k-3)/ X_bin(k-3)


        function = w_bin*(np.floor(k+ (1 + w_bin)/2) - k)
        addition_term = b_bin * np.floor((1 + w_bin)/2) + (1 - b_bin) * np.floor((1 - w_bin)/2)

        final = k_1*k_3*(function + addition_term) + (1-k_1*k_3) *w/X_bin(w)* 2
        return final * np.pi/2 
    
    # Delta angle with missing zero point
    W_coeff = W_bin(w)
    B_coeff = B_bin(k)


    delta_plus = get_delta_theta_plus(k)

    
    return W_coeff * B_coeff * (np.pi - 2 * delta_plus) + delta_plus

    
    

def X_bin(x):

    return x ** (1 - 0**abs(x))



def get_delta_theta_plus(k):
    
    D_coeff =(1 + (-1) ** np.floor(k+1))/2
    
    return (np.pi/2) * (np.floor(k+1) - k + D_coeff)
    



def A_coeff(x_line, w, y):
    
    product = x_line * w  * y * (-1)
    
    return product/abs(X_bin(product))


def A_coeff_not_general(x_line, w, y):

    x_coeff = X_bin(x_line)

    return (-1) * (x_line/abs(x_coeff)) * (w / abs(w)) * (y/abs(y))



def get_mth_approximation(data_processing, t_nth, index, i=200, accuracy=5):

    if t_nth > 0:
        
        missing_point_mode = data_processing.mode_statuses_dict['Missing point'][1] 
        
        deg_x, deg_y = data_processing.get_curr_param('deg')
        v = data_processing.get_curr_param('v')
        w = data_processing.get_curr_param('w')
        k = np.copy(data_processing.get_curr_param('k'))
        x_line = data_processing.get_curr_param('x')
        # a_line = data_processing.slope
        b_line = data_processing.get_curr_param('b')
        
        n_coeff = get_n_coeff(index)

        
        if data_processing.mode_statuses_dict['General solution'][1]:
            a_slope = data_processing.slope

            delta_k_rotated_angle = get_delta_k_rotated(a_slope, b_line, x_line)

            k += delta_k_rotated_angle

        t_0_main, t_0_zero_alg, combined_t = np.copy(t_nth), np.copy(t_nth), np.copy(t_nth)
        init_theta_angle = k * np.pi/2

        # init_y = get_nth_deg_y_derivative(deg_y, combined_t, v, w, k)
        
        init_x_derivative = get_nth_deg_x_derivative(deg_x+1, combined_t, v, w, k)

        last_t = np.copy(combined_t)


        for _ in range(1,i):

            curr_x = get_nth_deg_x_derivative(deg_x, combined_t, v, w, k)
            curr_y= get_nth_deg_y_derivative(deg_y, combined_t, v, w, k)
            
            ''' Main algorithm '''
            # The difference between the x-coordinate of the vertical line 
            # and the x-coordinate of the current spiral radius vector
            c = abs(x_line) - abs(curr_x)

            a = np.sqrt(x_line**2 + curr_y**2)

            # Current radius vector
            b = np.sqrt(curr_x ** 2 + curr_y**2)

            cos_delta_phi = (a ** 2 + b**2 - c ** 2)/X_bin((2 * a * b))



            if abs(cos_delta_phi) > 1:

                cos_delta_phi = 1

            delta_phi = np.arccos(cos_delta_phi)

            a_coeff = A_coeff(x_line, w, curr_y)



            curr_t = (a_coeff * delta_phi) / abs(X_bin(w))

            t_0_main += (c/abs(X_bin(c)))*curr_t    
            
            if not missing_point_mode:
                ''' Zero point algorithm '''

                t_0_zero_alg = abs(x_line) * np.sqrt(1 + (curr_y/X_bin(curr_x))**2)

                combined_t = (1-n_coeff) * t_0_zero_alg + n_coeff * t_0_main
                
            else:
                combined_t = np.copy(t_0_main)


            statement = f'{combined_t:.{accuracy}f}' == f'{last_t:.{accuracy}f}'
            
            if statement:
                return combined_t
            
            last_t = np.copy(combined_t)
            
            if not missing_point_mode:
            
                last_x_derivative = get_nth_deg_x_derivative(deg_x+1, last_t, v, w, k)
                derivative_change_coeff = derivative_change(init_x_derivative, last_x_derivative)

                last_t *= derivative_change_coeff

                if last_t == 0:
                    return last_t
            
        return last_t
    
    return t_nth