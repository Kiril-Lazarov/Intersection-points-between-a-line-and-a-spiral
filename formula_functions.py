import numpy as np
# from Data_classes.data_processing import DataProcessing



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



def get_nth_intersect(data_processing, n, w,k, final_solution = False):

    delta_theta = get_delta_theta(w, k)
    
    if not final_solution:
        return (delta_theta + (n-1) * np.pi) / abs(w)
    
    
   
    v = data_processing.get_curr_param('v')
    x_line = data_processing.get_curr_param('x')
    
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
    first_y_t = delta_theta/abs(w)
    first_y_rad_vec = get_nth_deg_y_derivative(deg_y, first_y_t, v, w, k)
    
    x_max_dist = x_max_line(first_y_rad_vec, x_line)

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



def x_max_line(rad_vec, x_line):
    
    values_diff = abs(rad_vec) - abs(x_line)
    diff_sign = values_diff/ abs(X_bin(values_diff))
    
    if diff_sign>0:
        diff_sign = 1
    elif diff_sign < 0:
        diff_sign = -1
        
    else:
        diff_sign= 0
        
    return np.floor((1+diff_sign)/2)

    

def get_delta_theta(w, k):

    b_bin = B_bin(np.floor(k)/2)
    w_bin= w/abs(X_bin(w))

    k_1 = (k-1)/ X_bin(k-1)
    k_3 = (k-3)/ X_bin(k-3)


    function = w_bin*(np.floor(k+ (1 + w_bin)/2) - k)
    addition_term = b_bin * np.floor((1 + w_bin)/2) + (1 - b_bin) * np.floor((1 - w_bin)/2)

    final = k_1*k_3*(function + addition_term) + (1-k_1*k_3) *w/X_bin(w)* 2
    return final * np.pi/2 

    
    

def X_bin(x):

    return x ** (1 - 0**abs(x))

def get_y_coord(v, w, k, prev_t):
    return v * prev_t * np.sin(k*np.pi/2 + w*prev_t)



def get_x_coord(v, w, k, prev_t):
    return v * prev_t * np.cos(k*np.pi/2 + w*prev_t)




    

def A_coeff(x_line, w, v, k, y):

    x_coeff = X_bin(x_line)
    w_coeff = X_bin(w)
    y_coeff = X_bin(y)

    return (-1) * (x_line/abs(x_coeff)) * (w / abs(w_coeff)) * (y/abs(y_coeff))





def get_mth_aproximation(data_processing, t_nth, i=200, accuracy=5, down_direction = False, correction_mech=False, f_binary=False):

    if t_nth > 0:
        
        deg_x, deg_y = data_processing.get_curr_param('deg')
        v = data_processing.get_curr_param('v')
        w = data_processing.get_curr_param('w')
        k = data_processing.get_curr_param('k')
        x_line = data_processing.get_curr_param('x')
        
        n = data_processing.algorithm_vars.algorithm_vars_dict['n']

        t_0 = np.copy(t_nth)
        init_theta_angle = k * np.pi/2

        init_y = get_nth_deg_y_derivative(deg_y, t_0, v, w, k)
        
        init_x_derivative = get_nth_deg_x_derivative(deg_x+1, t_0, v, w, k)
        
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

                cos_delta_phi = (a ** 2 + b**2 - c ** 2)/X_bin((2 * a * b))



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
                
            last_x_derivative = get_nth_deg_x_derivative(deg_x+1, last_t, v, w, k)
            derivative_change_coeff = derivative_change(init_x_derivative, last_x_derivative)

            last_t *= derivative_change_coeff
            if last_t == 0:
                return last_t
            
        return last_t
    
    return t_nth