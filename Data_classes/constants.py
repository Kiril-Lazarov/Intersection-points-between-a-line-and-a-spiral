from numpy import copy, pi
import inspect
from Data_classes.data_abstract import Data


class Constants(Data):
    
    """
    Global animation variables

    """ 
    
    
    screen_width = 1500
    screen_height = 800
    half_screen_width = screen_width / 2
    half_screen_height = screen_height / 2

    coord_origin = [half_screen_width, half_screen_height]

    FPS = 24
    
    text_unit = screen_width/75

    '''
    Global spiral and line variables
    '''

    
    # Total number of units on the x-axis – both positive and negative.
    units =20
    half_units = units/2

    # Length of one unit along the coordinate axis, calculated as a function of the screen width and the number of    units.
    accuracy = 5
    length = screen_width/ units
    l_step = 3 # pixels
    
    max_step = 1000
    min_step = 0.00001

    # The step for changing the values of the spiral and line parameters.
    deg_step = 1
    t_step = 0.01
    v_step = 0.01
    w_step = 0.01
    k_step = 0.01
    x_step = 0.01
    c_step = 10 # pixels
    a_step = 1
    b_step = 0.1
    
    steps_constants_list = ['deg_step', 't_step', 'v_step', 'w_step', 'k_step', 'x_step', 'c_step', 'l_step', 'a_step', 'b_step']
    
    
    '''Spiral and line constants. The angular velocity is also constant, even though it can have a value of -1.'''
    
    deg = [0, 0] # Spiral components degrees
    t= 1 # Time
    v = 1 # Speed of the radius-vector
    w = 1 # Angular velocity
    k = 0 # Initial angle coefficient measured by pi/2
    x = 1 # Start position of the vertical line over x-axis
    c = [half_screen_width, half_screen_height] # Center of the coordinate system
    l = length
    
    params_constants_list = ['deg','t','v', 'w', 'k', 'l', 'x', 'c']
    
    # line constants
    a = 45
    b = 0
    
    line_constants_list = ['a', 'b']
  
    
    def __init__(self):
        
        super().__init__()
        self.constants_dict = {}
        self.line_constants_dict = {}
        self.steps_constants_dict = {}
        self.excluded_methods_names = [name[0] for name in inspect.getmembers(Constants, predicate=inspect.isfunction)]\
                                    + ['_abc_impl'] + ['class_init_values']
         

    def create_dict(self):        
        
        for name, value in Constants.__dict__.items():
            
            if not name.startswith('__') and name not in self.excluded_methods_names:
                
                if name in self.steps_constants_list:
                    
                    reduced_name = name.split('_step')[0]
                    self.steps_constants_dict[reduced_name] = value
                    
                elif name in self.params_constants_list:    
                    self.constants_dict[name] = value
                    
                elif name in self.line_constants_list:
                    self.line_constants_dict[name] = value
                    
    def reset_dict(self):
        self.constants_dict['w'] = self.w
        self.line_constants_dict['a'] = self.a
        self.line_constants_dict['b'] = self.b
        
                