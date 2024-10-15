import inspect

from Data_classes.data_abstract import Data
from Data_classes.variables import Variables

half_screen_width = Variables.half_screen_width
half_screen_height = Variables.half_screen_height
length = Variables.length # The length of unit distance in the coordinate system in pixels

class Constants(Data):
    
    # Spiral and line constants. The angular velocity is also constant, even though it can have a value of -1.
    deg = 0 # Spiral degree
    t= 1 # Time
    v = 1 # Speed of the radius-vector
    w = 1 # Angular velocity
    k = 0 # Initial angle coefficient measured by pi/2
    x = 1 # Start position of the vertical line over x-axis
    c = [half_screen_width, half_screen_height] # Center of the coordinate system
    l = length
    
    def __init__(self):
        super().__init__()
        self.constants_dict = {}
        self.excluded_methods_names = [name[0] for name in inspect.getmembers(Constants, predicate=inspect.isfunction)] + ['_abc_impl']
        print('From constants: ', self.excluded_methods_names)
    
    def create_dict(self):        
        
        for name, value in Constants.__dict__.items():
            if not name.startswith('__') and name not in self.excluded_methods_names:
                
                self.constants_dict[name] = value
                