import numpy as np
from Data_classes.data_abstract import Data
import inspect


class Variables(Data):
    
    '''{'deg': 0, 't': 0, 'v': 0, 'w': 0, 'x': 0, 'k': 0, 'l': 0, 'c': [0, 0]'''
   
    # Variables for parameter changes.
    deg_additional =  [0, 0]
    t_additional =  0
    v_additional =  0
    w_additional =  0
    x_additional =  0
    k_additional =  0
    l_additional =  0
    a_additional = 0
    b_additional = 0
    c_additional = [0, 0] # Center point additional values - [width, height]

    t_factor = 1
    v_factor = 1
    w_factor = 1
    x_factor = 1
    k_factor = 1
    l_factor = 1
    a_factor = 1
    b_factor = 1

    def __init__(self):
        super().__init__()
        
        self.variables_dict = {}
        self.factors_dict = {}
        self.excluded_methods_names = [name[0] for name in inspect.getmembers(Variables, predicate=inspect.isfunction)]\
                                    + ['_abc_impl'] + ['class_init_values']

    @property
    def class_init_values(self):
        
        return ([self.deg_additional, self.t_additional, self.v_additional, 
                self.w_additional, self.x_additional, self.k_additional, 
                self.l_additional, self.a_additional, self.b_additional, self.c_additional],
                
                [None, self.t_factor, self.v_factor, self.w_factor, self.x_factor, self.k_factor, self.l_factor, self.a_factor, self.b_factor, None])
    
    
    def create_dict(self):        
        
        for name, value in Variables.__dict__.items():
            if not name.startswith('__') and name not in self.excluded_methods_names:
      
                if '_additional' in name:
                    reduced_name = name.split('_additional')[0]
                    self.variables_dict[reduced_name] = value
                    
                elif '_factor' in name:
                    reduced_name = name.split('_factor')[0]
                    self.factors_dict[reduced_name] = value
                
                
    def reset_dict(self):

        index = 0
        for key in self.variables_dict.keys():

            if key == 'c' or key == 'deg':

                self.variables_dict[key] = [0, 0]
            else:

                self.variables_dict[key] = self.class_init_values[0][index]
                self.factors_dict[key] = self.class_init_values[1][index]

            index += 1


