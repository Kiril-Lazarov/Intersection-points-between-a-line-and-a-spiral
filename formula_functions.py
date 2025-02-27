import numpy as np

def derivative_change(x_der_t0, x_der_y_zero):
    x_0_sign = x_der_t0 / abs(E(x_der_t0))

    x_t_sign = x_der_y_zero / abs(E(x_der_y_zero))

    sum_signs = x_0_sign + x_t_sign

    return (sum_signs) / E(sum_signs)


def get_nth_deg_x_derivative(deg, t, v, w, k):
    theta = k * np.pi / 2 + w * t
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)

    trig_derivatives_cycle = [sin_theta, cos_theta, -sin_theta, -cos_theta]
    nth_der = deg % 4
    next_nth = (deg + 1) % 4

    nth_cos_deriv = trig_derivatives_cycle[nth_der]
    nth_sin_deriv = trig_derivatives_cycle[next_nth]

    result = v * (E(w) ** (deg - 1)) * (deg * nth_cos_deriv + E(w) * t * nth_sin_deriv)

    return round(result, 13)


def get_nth_deg_y_derivative(deg, t, v, w, k):
    theta = k * np.pi / 2 + w * t
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)

    trig_derivatives_cycle = [sin_theta, cos_theta, -sin_theta, -cos_theta]
    nth_der = deg % 4
    prev_nth = (deg - 1) % 4

    nth_cos_deriv = trig_derivatives_cycle[nth_der]
    nth_sin_deriv = trig_derivatives_cycle[prev_nth]

    result = v * (E(w) ** (deg - 1)) * (deg * nth_sin_deriv + E(w) * t * nth_cos_deriv)

    return round(result, 13)


def get_rotation_coeff(b, x):
    product = (-1) * b * x

    return product / abs(E(product))


def get_delta_k_rotated(a, b, x):
    delta_k_coeff = get_rotation_coeff(b, x)
    a_coeff = a / abs(E(a))
    b_coeff = b / abs(E(b))
    a_turn_on = a / E(a)
    b_turn_on = b / E(b)
    slope_angle = abs(np.arctan(a))
    expr = delta_k_coeff * 2 * (np.pi / 2 - slope_angle) / np.pi
    

    result = -(1 - a_turn_on) + a_turn_on * expr + (1 - b_turn_on) * 2 * (
                np.pi/2 - np.arctan(a)) / np.pi + (1 - a_turn_on) * (1 - b_turn_on)

    return result

def get_n_coeff(n):
    return n / E(n)

def greater(x):
    return np.floor((1 + x/abs(E(x)))/2)

def less(x):
    return np.floor((1 - x/abs(E(x)))/2)




def XYSwitch(n, k, x_line, w, v, deg_x):

    delta_theta = get_delta_theta(w, k)
    
    x_rad_vec_t = (delta_theta + (n - 1) * np.pi + np.pi / 2) / abs(w)
    y_rad_vec_t = (delta_theta + n * np.pi) / abs(w)
    
    x_nth_coord = get_nth_deg_x_derivative(deg_x, x_rad_vec_t, v, w, k)

    x_signs_product =  x_line * x_nth_coord / abs(E(x_line * x_nth_coord))

    x_line_t = abs(x_line)/E(v)

    product = (x_line_t - x_rad_vec_t) * (y_rad_vec_t - x_line_t)
    product_sign = product/ abs(E(product))

    result = (np.floor((1 +  product_sign))/2) * (np.floor((1 +  x_signs_product))/2)
        
    return result



def W_bin(w):
    return (1 - w / abs(E(w))) / 2


def B_bin(k):
    return np.ceil(k) - np.floor(k)


def KWX_line(k, w, x_line):
    k_1_koeff = 1 - (k - 1) / E(k - 1)
    k_3_koeff = 1 - (k - 3) / E(k - 3)

    x_w_pos_sum = x_line / abs(E(x_line)) + w / abs(E(w))

    x_w_neg_sum = x_line / abs(E(x_line)) - w / abs(E(w))

    return k_1_koeff * (x_w_neg_sum / E(x_w_neg_sum)) + k_3_koeff * (x_w_pos_sum / E(x_w_pos_sum))


def K_sign(k, x_line):
    product = (k - 1) * (k - 3) * x_line
    kl = product / abs(E(product))
    return np.floor((1 + kl) / 2)


def x_max_line(deg_y, delta_theta, x_line, v, w, k):
    t = delta_theta / abs(E(w))

    first_rad_vec_length = get_nth_deg_y_derivative(deg_y, t, v, w, k)

    values_diff = abs(first_rad_vec_length) - abs(x_line)
    diff_sign = values_diff / abs(E(values_diff))

    return np.floor((1 + diff_sign) / 2)


def get_delta_theta_plus(k):
  

    return (np.pi / 2) * (np.floor(k + 1) - k + B_bin(np.floor(k)/2))

def get_delta_theta_minus(k):
    
    return (np.pi / 2) * ( k - np.floor(k) + B_bin(np.floor(k+1)/2))


def get_delta_theta(w, k, zero_missing_point=False):
    w_bin = w / abs(E(w))
    if not zero_missing_point:
        b_bin = B_bin(np.floor(k) / 2)

        k_1 = (k - 1) / E(k - 1)
        k_3 = (k - 3) / E(k - 3)

        function = w_bin * (np.floor(k + (1 + w_bin) / 2) - k)
        addition_term = b_bin * np.floor((1 + w_bin) / 2) + (1 - b_bin) * np.floor((1 - w_bin) / 2)

        final = k_1 * k_3 * (function + addition_term) + (1 - k_1 * k_3) * w / E(w) * 2
        return final * np.pi / 2

    delta_plus = get_delta_theta_plus(k)
    delta_minus = get_delta_theta_minus(k)
    
    WPos = greater(w)
    Wneg = less(w)

    return w_bin*(WPos*delta_plus + Wneg * delta_minus)


def E(x):
    return x ** (1 - 0 ** abs(x))



def WYX(x_line, w, y):
    product = x_line * w * y * (-1)

    return product / abs(E(product))


def ABSwitch(deg_x, deg_y, t_nth, w, v, k, x_line, rot_vector=False):
    curr_y = get_nth_deg_y_derivative(deg_y, t_nth, v, w, k)

    WYX_coeff = WYX(x_line, w, curr_y)

    rotated_rad_vec_t = t_nth + WYX_coeff * (np.pi / 2) / abs(w)

    rot_rad_vec_x = abs(get_nth_deg_x_derivative(deg_x, rotated_rad_vec_t, v, w, k)) + v * np.pi / 4 / abs(w)

    diff = abs(rot_rad_vec_x) - abs(x_line)

    result = np.floor((1 + (diff) / abs(E(diff))) / 2)
    if rot_vector:
        return rot_rad_vec_x
    return result

def get_nth_intersect(n, deg_x, deg_y, a, b, v, w, k, x_line, zero_missing_point_mode, general_solution, reduct_funcs_dict):
    if general_solution:
        k = np.copy(k)

        delta_k_rotated_angle = get_delta_k_rotated(a, b, x_line)

        k += delta_k_rotated_angle

    delta_theta = get_delta_theta(w, k, zero_missing_point=zero_missing_point_mode)

    if zero_missing_point_mode:
        if n == 0:
            n += 1

        return (delta_theta + (n - 1) * np.pi) / abs(E(w))

    zero_y_t = abs(x_line / E(v))

    kwx_coeff = KWX_line(k, w, x_line)
    k_sign = K_sign(k, x_line)
    
    reduct_funcs_dict['KWL'][0] = kwx_coeff
    reduct_funcs_dict['KL'][0] = k_sign
  

    n_coeff = get_n_coeff(n)
    opp_n_coeff = 1 - n_coeff

    # The x-derivative at t=0
    x_der_t0 = get_nth_deg_x_derivative(deg_x + 1, 0, v, w, k)

    # The x-derivative at the zero y-intersection point
    x_der_y_zero = get_nth_deg_x_derivative(deg_x + 1, zero_y_t, v, w, k)

    is_der_changed = derivative_change(x_der_t0, x_der_y_zero)
    
    reduct_funcs_dict['SCDD'][0] = is_der_changed

    # The length of the first y-intersection point radius vector
    x_max_dist = x_max_line(deg_y, delta_theta, x_line, v, w, k)
    
    reduct_funcs_dict['XMD'][0] = x_max_dist

    # The length of the nth y-component if the radius vector + pi/2 rotation
    XYSwitch_coeff = XYSwitch(n, k, x_line, w, v, deg_x)


    # result = x_max_dist * is_der_changed * (k_sign + kwx_coeff) * opp_n_coeff * zero_y_t \
    #          + n_coeff * ((delta_theta + (n - 1) * np.pi + XYSwitch_coeff *(abs(x_line))/E(v))) / abs(w)
    
    result = x_max_dist * is_der_changed * (k_sign + kwx_coeff) * opp_n_coeff * zero_y_t \
         + n_coeff * ((delta_theta + (n - 1) * np.pi + XYSwitch_coeff *np.pi/2)) / abs(w)
    
    # result = x_max_dist * is_der_changed * (k_sign + kwx_coeff) * opp_n_coeff * zero_y_t \
    #          + n_coeff * ((delta_theta + (n - 1) * np.pi)) / abs(w)

    return result



def get_mth_approximation(deg_x, deg_y, v, w, k, x_line, b_line, a_slope, accuracy,
                          zero_missing_point_mode, general_solution, x_l_x_s_diff_mode, reduct_funcs_dict, x_deriv_list, t_nth, n, i=200):
    
    if t_nth > 0:
        
        n_coeff = get_n_coeff(n)
        opp_n_coeff = 1 - n_coeff

        if general_solution:
            delta_k_rotated_angle = get_delta_k_rotated(a_slope, b_line, x_line)

            k += delta_k_rotated_angle
            
        XYSwitch_coeff = XYSwitch(n, k, x_line, w, v, deg_x)
        opp_XYSwitch_coeff = 1 - XYSwitch_coeff

        ABSwitch_coeff = ABSwitch(deg_x, deg_y, t_nth, w, v, k, x_line)

        t_0_main, t_0_zero_alg, combined_t = np.copy(t_nth), np.copy(t_nth), np.copy(t_nth)
        init_theta_angle = k * np.pi / 2

        init_x_derivative = get_nth_deg_x_derivative(deg_x + 1, combined_t, v, w, k)

        x_deriv_list = []
        x_deriv_list.append(init_x_derivative)

        last_t = np.copy(combined_t)

        for _ in range(1, i):

            curr_x = get_nth_deg_x_derivative(deg_x, combined_t, v, w, k)
            curr_y = get_nth_deg_y_derivative(deg_y, combined_t, v, w, k)

            ''' Angular Algorithm '''
            
            # The difference between the x-coordinate of the vertical line 
            # and the x-coordinate of the current spiral radius vector
            c = abs(x_line) - abs(curr_x)

            a = np.sqrt(x_line ** 2 + curr_y ** 2)

            # Current radius vector
            b = np.sqrt(curr_x ** 2 + curr_y ** 2)

            cos_delta_phi = (curr_y**2 + abs(x_line * curr_x)) / E(np.sqrt((curr_y**2 +x_line**2)*(curr_y**2 + curr_x**2)))

            if abs(cos_delta_phi) > 1:
                cos_delta_phi = 1

            delta_phi = np.arccos(cos_delta_phi)

            WYX_coeff = WYX(x_line, w, curr_y)

            curr_t = (WYX_coeff * delta_phi) / abs(E(w))
            
            x_l_x_s_diff_sign = c / abs(E(c))
            
            if not x_l_x_s_diff_mode:
                
                t_0_main +=  curr_t
                
            else:

                t_0_main += x_l_x_s_diff_sign * curr_t
            

            if not zero_missing_point_mode:
                ''' Vector-Length Algorithm '''

                phi = np.arctan(abs(curr_y/E(curr_x)))

                VL = abs(x_line)/ (np.cos(phi)* E(v))
 
                combined_t = opp_n_coeff * VL + opp_XYSwitch_coeff * n_coeff * ABSwitch_coeff * t_0_main + \
                             n_coeff * XYSwitch_coeff * VL
                # combined_t = opp_n_coeff * VL + n_coeff* (opp_XYSwitch_coeff* t_0_main + XYSwitch_coeff* VL)
                # combined_t = opp_n_coeff * VL + n_coeff* t_0_main 
                
                             

            else:
                combined_t = np.copy(t_0_main)

            statement = f'{combined_t:.{accuracy}f}' == f'{last_t:.{accuracy}f}'

            if statement:

                return combined_t, x_deriv_list

            last_t = np.copy(combined_t)

            if not zero_missing_point_mode:

                
                last_x_derivative = get_nth_deg_x_derivative(deg_x + 1, last_t, v, w, k)

                derivative_change_coeff = derivative_change(init_x_derivative, last_x_derivative)
               
                x_deriv_list.append(last_x_derivative)
                
                last_t *= derivative_change_coeff

                if last_t == 0:
                    
                    return last_t, x_deriv_list

        return last_t, x_deriv_list

    return t_nth, x_deriv_list




def whole_equation(n, m, v, w, k, x_line):
    
    XYSwitch_coeff = XYSwitch(n, k, x_line, w, v, 0)
    opp_XYSwitch_coeff = 1 - XYSwitch_coeff
    
    delta_theta = get_delta_theta(w, k)
    t = ((delta_theta + (n - 1) * np.pi + XYSwitch_coeff * np.pi / 2)) / abs(E(w))
    
    init_x_derivative = get_nth_deg_x_derivative(1, t, v, w, k)
    
    n_switch = get_n_coeff(n)
    opp_n_switch = 1 - n_switch
 
    KL = K_sign(k, x_line)
    KWL = KWX_line(k, w, x_line)
    
    x_der_t0 = get_nth_deg_x_derivative(1, 0, v, w, k)
    
    zero_y_t = abs(x_line / E(v))

    # The x-derivative at the zero y-intersection point
    x_der_y_zero = get_nth_deg_x_derivative(1, zero_y_t, v, w, k)

    SCDD = derivative_change(x_der_t0, x_der_y_zero)
    
    XMD = x_max_line(0, delta_theta, x_line, v, w, k)
    
    ABSwitch_coeff = ABSwitch(0, 0, t, w, v, k, x_line, rot_vector=False)
 
    for _ in range(m):
        
        curr_x = get_nth_deg_x_derivative(0, t, v, w, k)
        curr_y = get_nth_deg_y_derivative(0, t, v, w, k)
        
        c = abs(x_line) - abs(curr_x)

        a = np.sqrt(x_line ** 2 + curr_y ** 2)

            # Current radius vector
        b = np.sqrt(curr_x ** 2 + curr_y ** 2)
        
        cos_delta_phi = (curr_y**2 + abs(x_line * curr_x)) / E(np.sqrt((curr_y**2 +x_line**2)*(curr_y**2 + curr_x**2)))
        
        if abs(cos_delta_phi) > 1:
            cos_delta_phi = 1

        delta_phi = np.arccos(cos_delta_phi)

        WYX_coeff = WYX(x_line, w, curr_y)
        
        x_l_x_s_diff_sign = c / abs(E(c))
        
        AB_alg = t + x_l_x_s_diff_sign * WYX_coeff * (delta_phi/abs(E(w)))
        
        phi = np.arctan(abs(curr_y/E(curr_x)))

        LB_alg = abs(x_line)/ (np.cos(phi)* E(v))
        
            
        last_x_derivative = get_nth_deg_x_derivative(1, t, v, w, k)

        ISSCDD = derivative_change(init_x_derivative, last_x_derivative)
    
   
        
        t =  ISSCDD * (opp_n_switch * XMD * SCDD * (KWL + KL) * LB_alg + n_switch * \
                       (opp_XYSwitch_coeff*ABSwitch_coeff*AB_alg + XYSwitch_coeff* LB_alg))
        
    return t
        