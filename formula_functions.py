import numpy as np


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
    
    

def X_bin(x_line):
    return (x_line ** (0 ** abs(x_line) - 1)) ** -1

def get_y_coord(v, w, k, prev_t):
    return v * prev_t * np.sin(k*np.pi/2 + w*prev_t)



def get_x_coord(v, w, k, prev_t):
    return v * prev_t * np.cos(k*np.pi/2 + w*prev_t)

    

def A_coeff(x_line, w, v, k, y):

    x_coeff = X_bin(x_line)

    return (-1) * (x_line/abs(x_coeff)) * (w / abs(w)) * (y/abs(y))



def get_nth_intersect(n, k, w):
    delta_theta = get_delta_theta(w, k)
    
    return (delta_theta + (n-1) * np.pi) / abs(w)



def get_mth_aproximation(t_nth, x_line, v, w, k, i=200, accuracy=5):
    
    t_0 = np.copy(t_nth)
    init_theta_angle = k * np.pi/2
    
    init_y = get_y_coord(v, w, k, t_0)
    
    a_coeff = A_coeff(x_line, w, v, k, init_y)

    
    x_coeff = X_bin(x_line)

    
    last_t = np.copy(t_0)
    

    
    for m in range(1, i+1):

        curr_x = get_x_coord(v, w, k, t_0)
        curr_y = get_y_coord(v, w, k, t_0)

        
        c = abs(curr_x - x_line)
        
        a = np.sqrt(x_line**2 + curr_y**2)
        
        b = v*t_0
        
        cos_delta_phi = (a ** 2 + b**2 - c ** 2)/(2 * a * b)
        
        delta_phi = np.arccos(cos_delta_phi)
   
        t_0 += (a_coeff * delta_phi)/ abs(w)
    
        if f'{t_0:.{accuracy}f}' == f'{last_t:.{accuracy}f}':
       
            return t_0
        last_t = np.copy(t_0)
