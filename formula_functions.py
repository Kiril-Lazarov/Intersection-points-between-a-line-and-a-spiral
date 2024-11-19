import numpy as np
# from Data_classes.data_processing import DataProcessing

def D_bin(k):

    return (1 + (-1) ** np.floor(k+1))/2

def derivative_change(x_0, x_t):
    
    x_0_sign = x_0/abs(X_bin(x_0))
    
    if x_0_sign >0:
        x_0_sign = 1
    elif x_0_sign < 0:
        x_0_sign = -1
    else:
        x_0_sign = 0
        
        
    x_t_sign = x_t/abs(X_bin(x_t))
    
    if x_t_sign >0:
        x_t_sign = 1
    elif x_t_sign < 0:
        x_t_sign = -1
    else:
        x_t_sign = 0        

    return (x_0_sign + x_t_sign)/X_bin(x_0_sign + x_t_sign)


def W_bin(w):

    return (1 - w / abs(X_bin(w)))/2


def B_bin(k):
    
#     if int(k) == 1 or int(k) == 3:
    
#         if len(str(k)) > 2:
#             k = float(str(k)[:-1])

    return np.ceil(k) - np.floor(k)


def calc_power(k, w):
    
    k_1 = (1- (k-1)/(X_bin(k-1)))
    k_3 = (1- (k-3)/(X_bin(k-3)))
    
    w_1= (1 - (w)/ abs(X_bin(w)))/2
    w_neg_1 = (1 + (w)/ abs(X_bin(w)))/2
    
    power = k_3*w_1 + k_1 * w_neg_1
    
    if power<1:
        power = 0

    return power


def KWX_line(k, w, x_line):
    
#     if len(str(k)) > 2:
#         k = float(str(k)[:-1])
        
#     if len(str(w)) > 2:
#         w = float(str(w)[:-1])
        
    k_coeff = ((k-1)/abs(X_bin(k-1)) * ((3-k)/abs(X_bin(3-k))))                         
    
    if k_coeff > 0:
        k_coeff = 1
    elif k_coeff < 0:
        k_coeff = -1
    else:
        k_coeff = 0

    k13_coeff = (1 - abs(k_coeff))

    w_coeff = w / abs(X_bin(w))
    
    if w_coeff > 0:
        w_coeff = 1
    elif w_coeff < 0:
        w_coeff = -1
    else:
        w_coeff = 0
        
    # power = calc_power(k, w)
        
    # w_special_cases = w_coeff ** (power)
    
    # print('k: ', k, 'w_coeff: ', w_coeff, 'power: ',power, 'w_special_cases: ',w_special_cases)
    x_line_coeff = x_line/(abs(X_bin(x_line)))
    
    if x_line_coeff > 0:
        x_line_coeff = 1
    elif x_line_coeff < 0:
        x_line_coeff = -1
    else:
        x_line_coeff = 0  
  
    return np.floor((1 - k13_coeff *w_coeff*x_line_coeff)/2) 
    # return k13_coeff

def swap_result(value, constant, direction=False):
    
    v_c_sum = value - constant
    
    x_bin = X_bin(v_c_sum) if not direction else abs(X_bin(v_c_sum))

    return 1- ((v_c_sum)/x_bin)


def special_cases_factor(n, k, w):
    
    if len(str(k)) > 2:
        k = float(str(k)[:-1])
        
    if len(str(w)) > 2:
        w = float(str(w)[:-1])
    # print()
    n_koeff = swap_result(n, 1)
    # print('k: ', k)
    k_1_koeff = swap_result(k, 1)
    # print('k: ', k, 'k_1_koeff: ', k_1_koeff)
    w_koeff = swap_result(w, 1) 

    k_3_koeff =swap_result(k, 3)

    neg_w_koeff = swap_result(w, -1)
    # print('neg_w_koeff: ', neg_w_koeff)
    factor = (1-n_koeff*k_1_koeff*w_koeff) + (1-n_koeff*k_3_koeff*neg_w_koeff) 
    
    factor = np.floor(factor/2)

    return factor


def K_sign(k, x_line):
    
#     if len(str(k)) > 2:
#         k = float(str(k)[:-1])
    
    k_coeff = ((k-1)/abs(X_bin(k-1))) * ((k-3)/abs(X_bin(k-3)))
   
    
    if k_coeff > 0:
        k_coeff = 1
    elif k_coeff < 0:
        k_coeff = -1
    else:
        k_coeff = 0

    x_line_coeff = x_line/abs(X_bin(x_line))
    
    if x_line_coeff > 0:
        x_line_coeff = 1
    elif x_line_coeff < 0:
        x_line_coeff = -1
        
    else:
        x_line_coeff = 0

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


def get_delta_theta_plus(k):
    
    D_coeff = D_bin(k)
    
    return (np.pi/2) * (np.floor(k+1) - k + D_coeff)
    
    

def get_delta_theta(w, k):

    b_bin = B_bin(np.floor(k)/2)
    w_bin= w/abs(X_bin(w))

    k_1 = (k-1)/ X_bin(k-1)
    k_3 = (k-3)/ X_bin(k-3)
    # print(k_1*k_3)

    function = w_bin*(np.floor(k+ (1 + w_bin)/2) - k)
    addition_term = b_bin * np.floor((1 + w_bin)/2) + (1 - b_bin) * np.floor((1 - w_bin)/2)
    print()
    print('function: ', function)
    print('addition_term: ', addition_term)

    # exclude_coeff = np.floor((1-B_bin(np.floor(k)/2) + w/abs(X_bin(w)))/2)
    final = k_1*k_3*(function + addition_term) + (1-k_1*k_3) *w/X_bin(w)* 2
    return final * np.pi/2 
    # return  W_coeff * B_coeff * (np.pi - 2 * delta_plus) + delta_plus
    
    

def X_bin(x):
    # return (x ** (0 ** abs(x) - 1)) ** -1
    return x ** (1 - 0**abs(x))

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

def get_nth_intersect(data_processing, n, w,k, final_solution = False):

    delta_theta = get_delta_theta(w, k)
    
    if not final_solution:
        return (delta_theta + (n-1) * np.pi) / abs(w)
    
    
   
    v = data_processing.get_curr_param('v')
    x_line = data_processing.get_curr_param('x')
    
    zero_y_t =  abs(x_line/v)
    
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
    
    special_cases = special_cases_factor(n, k, w)
    
    # print('special_cases: ',special_cases)
  
    # print()
    print('k: ',k, 'w: ', w, 'x: ',x_line)
    print('delta theta: ', delta_theta)
    print('k_sign: ',k_sign)
    print('kwx_coeff: ',kwx_coeff)
    print('x_max_dist* is_der_changed* (k_sign + kwx_coeff): ', x_max_dist* is_der_changed* (k_sign + kwx_coeff))
    print('(k_sign + kwx_coeff): ', (k_sign + kwx_coeff))
    print('is_der_changed: ', is_der_changed)
    print('x_max_dist: ',x_max_dist)
#     # # print()
    result = x_max_dist* is_der_changed* (k_sign + kwx_coeff)*(1 - n/X_bin(n)) * zero_y_t\
                             + (n/X_bin(n))*(delta_theta + (n-1) * np.pi) / abs(w)
    # print(f'Special cases factor at n = {n}, w={X_bin(w)}, k = {k} : ', special_cases)

    return  result



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
                
            last_x_derivative = get_nth_deg_x_derivative(deg_x+1, last_t, v, w, k)
            derivative_change_coeff = derivative_change(init_x_derivative, last_x_derivative)

            last_t *= derivative_change_coeff
            if last_t == 0:
                return last_t
            
        return last_t
    
    return t_nth