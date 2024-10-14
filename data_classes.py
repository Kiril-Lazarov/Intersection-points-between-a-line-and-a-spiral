from abc import ABC, abstractmethod

class Data(ABC):
    
    @abstractmethod
    def create_dict(self):
        pass

class Variables(Data):
    """
    Global animation variables

    """ 

    screen_width = 1500
    screen_height = 800
    half_screen_width = screen_width / 2
    half_screen_height = screen_height / 2

    coord_origin = [half_screen_width, half_screen_height]

    FPS = 24


    '''
    Global spiral and line variables
    '''

    # Total number of units on the x-axis – both positive and negative.
    units =20
    half_units = units/2

    # Length of one unit along the coordinate axis, calculated as a function of the screen width and the number of units.
    length = screen_width/ units
    l_step = 3 # pixels

    # The step for changing the values of the spiral and line parameters.
    deg_step = 1
    t_step = 0.025
    v_step = 0.025
    w_step = 0.025
    k_step = 0.025
    x_step = 0.03

    c_step = 10 # pixels
    
    def __init__(self):
        super().__init__()
        self.variables_dict = {}

    
    def create_dict(self):        
        
        for name, value in Variables.__dict__.items():
            if not name.startswith('__') and name != 'create_dict' and name != '_abc_impl':
                
                self.variables_dict[name] = value
                
                   
class Constants(Data):
    
    # Spiral and line constants. The angular velocity is also constant, even though it can have a value of -1.
    deg = 0 # Spiral degree
    t= 1 # Time
    v = 1 # Speed of the radius-vector
    w = 1 # Angular velocity
    k = 0 # Initial angle coefficient measured by pi/2
    vert_line_x = 1 # Start position of the vertical line over x-axis
    
    def __init__(self):
        super().__init__()
        self.constants_dict = {}

    
    def create_dict(self):        
        
        for name, value in Constants.__dict__.items():
            if not name.startswith('__') and name != 'create_dict' and name != '_abc_impl':
                
                self.constants_dict[name] = value
    
class Booleans(Data):
    
    background_mode = True
    algorithm_mode = False
    vertical_line_mode = True
    derivatives_mode = False
    spiral_mode = True
    y_axis_intersects = True
    line_intersects = True
    algorithm_data_mode = True
    parameters_mode = True 
    t_diagram_mode = False
    
    def __init__(self):
        super().__init__()
        self.booleans_dict = {}

    
    def create_dict(self):        
        
        for name, value in Booleans.__dict__.items():
            if not name.startswith('__') and name != 'create_dict' and name != '_abc_impl':
                
                self.booleans_dict[name] = value
    
class AdditionalVariables(Data):
    
    # Variables for parameter changes.
    deg_additional =  0
    t_additional =  0
    v_additional =  0
    w_additional =  0
    x_additional =  0
    k_additional =  0
    l_additional =  0
    coord_additional = [0, 0]
    
    def __init__(self):
        super().__init__()
        self.add_vars_dict = {}

    
    def create_dict(self):        
        
        for name, value in AdditionalVariables.__dict__.items():
            if not name.startswith('__') and name != 'create_dict' and name != '_abc_impl':
                
                self.add_vars_dict[name] = value
                
class AlgorithmVariables(Data):
    
    n = 0
    m = 0
    total_n = 0
    
    def __init__(self):
        super().__init__()
        self.algorithm_vars_dict = {}

    
    def create_dict(self):        
        
        for name, value in AlgorithmVariables.__dict__.items():
            if not name.startswith('__') and name != 'create_dict' and name != '_abc_impl':
                
                self.algorithm_vars_dict[name] = value
    
class DataDictionary(Constants, Variables, Booleans, AdditionalVariables, AlgorithmVariables):
    
    variables = Variables()
    variables.create_dict()
  
    constants = Constants()
    constants.create_dict()
    
    booleans = Booleans()
    booleans.create_dict()
    
    add_vars = AdditionalVariables()
    add_vars.create_dict()
    
    algorithm_vars = AlgorithmVariables()
    algorithm_vars.create_dict()