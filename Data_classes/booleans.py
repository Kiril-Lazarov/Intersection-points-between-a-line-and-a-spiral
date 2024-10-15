from Data_classes.data_abstract import Data
import inspect

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
    
    '''methods = inspect.getmembers(MyClass, predicate=inspect.isfunction)'''
    
    
    
    def __init__(self):
        super().__init__()
        self.booleans_dict = {}
        self.excluded_methods_names = [name[0] for name in inspect.getmembers(Booleans, predicate=inspect.isfunction)] + ['_abc_impl']
    
    def create_dict(self):        
        
        for name, value in Booleans.__dict__.items():
            if not name.startswith('__') and name not in self.excluded_methods_names:
                
                self.booleans_dict[name] = value
                
    def switch_mode(self, mode):
        self.booleans_dict[mode] = not self.booleans_dict[mode]