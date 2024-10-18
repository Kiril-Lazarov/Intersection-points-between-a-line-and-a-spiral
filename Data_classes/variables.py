import numpy as np
from Data_classes.data_abstract import Data
import inspect


class Variables(Data):
    
    '''{'deg': 0, 't': 0, 'v': 0, 'w': 0, 'x': 0, 'k': 0, 'l': 0, 'c': [0, 0]'''
   
    # Variables for parameter changes.
    deg_additional =  0
    t_additional =  0
    v_additional =  0
    w_additional =  0
    x_additional =  0
    k_additional =  0
    l_additional =  0
    c_additional = [0, 0] # Center point additional values - [width, height]

    
    def __init__(self):
        super().__init__()
        self.variables_dict = {}
        self.excluded_methods_names = [name[0] for name in inspect.getmembers(Variables, predicate=inspect.isfunction)]\
                                    + ['_abc_impl'] + ['class_init_values']

    @property
    def class_init_values(self):
        
        return [self.deg_additional, self.t_additional, self.v_additional, 
                self.w_additional, self.x_additional, self.k_additional, 
                self.l_additional, self.c_additional]
    
    
    def create_dict(self):        
        
        for name, value in Variables.__dict__.items():
            if not name.startswith('__') and name not in self.excluded_methods_names:
                
                reduced_name = name.split('_additional')[0]
                self.variables_dict[reduced_name] = value
                
    def reset_dict(self):

        index = 0
        for key in self.variables_dict.keys():

            if key == 'c':

                self.variables_dict[key] = [0, 0]
            else:

                self.variables_dict[key] = self.class_init_values[index]

            index += 1


