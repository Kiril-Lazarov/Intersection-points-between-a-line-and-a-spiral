from Data_classes.data_abstract import Data
import inspect

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

    # Length of one unit along the coordinate axis, calculated as a function of the screen width and the number of    units.
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
        self.excluded_methods_names = [name[0] for name in inspect.getmembers(Variables, predicate=inspect.isfunction)] + ['_abc_impl']

    
    def create_dict(self):        
        
        for name, value in Variables.__dict__.items():
            if not name.startswith('__') and name not in self.excluded_methods_names:
                
                self.variables_dict[name] = value
                