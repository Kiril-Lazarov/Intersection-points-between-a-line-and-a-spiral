import numpy as np
# from Data_classes.data_processing import DataProcessing

def D_bin(k):
    return (1 + (-1) ** np.floor(k+1))/2


def W_bin(w):
    return (1 - w / abs(w))/2


def B_bin(k):
    return np.ceil(k) - np.floor(k)


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



def get_nth_intersect(n, k, w):
    delta_theta = get_delta_theta(w, k)
    
    return (delta_theta + (n-1) * np.pi) / abs(w)





def get_mth_aproximation(data_processing, t_nth, i=200, accuracy=5, correction_mech=False, f_binary=False):


    deg = data_processing.get_curr_param('deg')
    v = data_processing.get_curr_param('v')
    w = data_processing.get_curr_param('w')
    k = data_processing.get_curr_param('k')
    x_line = data_processing.get_curr_param('x')
    
    t_0 = np.copy(t_nth)
    init_theta_angle = k * np.pi/2

    init_y = get_nth_deg_y_derivative(deg, t_0, v, w, k)

    # a_coeff = float(round(A_coeff(x_line, w, v, k, init_y),5))
    a_coeff = A_coeff(x_line, w, v, k, init_y)


    last_t = np.copy(t_0)



    for _ in range(1,i):

        curr_x = get_nth_deg_x_derivative(deg,t_0, v,w,k)
        curr_y= get_nth_deg_y_derivative(deg,t_0, v,w,k)


        if f_binary:
            x_bin = X_bin(abs(x_line) - abs(curr_x))


            t_ternary = T_ternary(abs(x_line), abs(curr_x), x_bin)
            g_bin = G_bin(t_ternary)
            f_bin = F_bin(abs(x_line), abs(curr_x), g_bin)
            c = f_bin
        else:
            if correction_mech:
                if abs(curr_x) > abs(x_line):
                    curr_x = np.copy(x_line)


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

    return last_t