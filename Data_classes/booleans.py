from numpy import copy
from Data_classes.data_abstract import Data
import inspect

class Booleans(Data):
    
    background_mode = True
    algorithm_mode = False
    vertical_line_mode = True
    derivatives_mode = False
    spiral_mode = True
    y_axis_intersects_mode = True
    line_intersects_mode = True
    algorithm_data_mode = True
    parameters_mode = True 
    t_diagram_mode = False
    
    update_screen = False
    update_spiral = False
    update_line = False
    reset_background = False
    is_t_diagram_change = False
    is_turn_off = None
    
    def __init__(self):
        
        super().__init__()
        self.booleans_dict = {}
        self.update_booleans_dict = {}
        self.excluded_methods_names = [name[0] for name in inspect.getmembers(Booleans, predicate=inspect.isfunction)]\
                                    + ['_abc_impl'] + ['class_init_values']
        
    @property    
    def class_init_values(self):
        
        # return [self.background_mode, self.algorithm_mode, self.vertical_line_mode, self.derivatives_mode,
        #                  self.spiral_mode, self.y_axis_intersects_mode, self.line_intersects_mode, self.algorithm_data_mode,
        #                  self.parameters_mode, self.t_diagram_mode]
        
        return [True, False, True, False, True, True, True, True, True, False]
  
    def create_dict(self, update_dict=True):        
        
        for name, value in Booleans.__dict__.items():            
            if not name.startswith('__') and name not in self.excluded_methods_names:
                
                if 'mode' in name:                    
                    self.booleans_dict[name] = value
                    
                else:
                    if update_dict:
                        self.update_booleans_dict[name] = value
                        
    def reset_dict(self):
        
        index = 0
        
        for key in self.booleans_dict.keys():
            
            self.booleans_dict[key] = self.class_init_values[index]
            index += 1

        
    
    def reset_to_false(self):
        
        for name, _ in self.update_booleans_dict.items():
            if name not in ['is_t_diagram_change', 'is_turn_off']:
                self.update_booleans_dict[name] = False