import pygame 
from numpy import tan, arctan, cos, pi

from Data_classes.variables import Variables
from Data_classes.constants import Constants
from Data_classes.booleans import Booleans
from Data_classes.algorithm_variables import AlgorithmVariables
from Animation_layers.animation_layers import AnimationLayers

from formula_functions import X_bin


class DataProcessing():

    bg_color = (255, 255, 255)
    

    def __init__(self):
        self.variables = Variables()
        self.variables.create_dict()
        
        self.constants = Constants()
        self.constants.create_dict()
        
        self.booleans = Booleans()
        self.booleans.create_dict()
        
        self.algorithm_vars = AlgorithmVariables()
        self.algorithm_vars.create_dict()
        
        self.animation_layers = AnimationLayers()
        self.animation_layers.create_dict()
        
        self.derivative_slopes = {'dx_dt': 0, 'dy_dt': 0, 'dy_dx': 0}
        self.spiral_coordinates = {'x': 0, 'y': 0}
        self.initialize_mode_status_dict()
         
        self.variable_dict_objects = [self.variables, self.booleans, self.constants, self.algorithm_vars]

    def blit_layers(self, win):

        win.fill(self.bg_color)

        for layer, boolean in self.mode_statuses_dict.values():
            if boolean and layer is not None:
                win.blit(layer, (0, 0))

    def get_curr_param(self, param):
        
        if param in ['c', 'deg']:
            return [self.constants.constants_dict[param][0] + self.variables.variables_dict[param][0],
                    self.constants.constants_dict[param][1] + self.variables.variables_dict[param][1]]
        
        elif param in ['a', 'b']:
            
            return self.constants.line_constants_dict[param] + self.variables.variables_dict[param]
        
        elif self.mode_statuses_dict['General solution'][1] and param == 'x':
            a = self.slope
            b = self.constants.line_constants_dict['b'] + self.variables.variables_dict['b']
            
            a_turn_on = a/X_bin(a)
            b_turn_on = b/X_bin(b)
        
            return (1- a_turn_on)* b + a_turn_on *b_turn_on* cos(pi/2 - arctan(a)) * (X_bin(-b))/X_bin(a)
        
        result = self.constants.constants_dict[param] + self.variables.variables_dict[param]
        return float(f'{result:.{self.constants.accuracy + 9}f}')
    
    def initialize_mode_status_dict(self):
        
         print(self.variables.variables_dict)
        
         self.mode_statuses_dict = {'Coordinates':[self.animation_layers.layers_dict['background_surface'],
                                         self.booleans.booleans_dict['background_mode']],
                          
                                    'Algorithm mode': [self.animation_layers.layers_dict['algorithm_layer'],
                                             self.booleans.booleans_dict['algorithm_mode']],
                          
                                    'Algorithm data mode': [self.animation_layers.layers_dict['show_algorithm_data_layer'],
                                                  self.booleans.booleans_dict['algorithm_data_mode']],
                          
                                    'T-diagram': [None,  self.booleans.booleans_dict['t_diagram_mode']],

                                    'Vertical line': [self.animation_layers.layers_dict['vertical_line_layer'],
                                                    self.booleans.booleans_dict['vertical_line_mode']],

                                    'Spiral': [self.animation_layers.layers_dict['spiral_layer'],
                                             self.booleans.booleans_dict['spiral_mode']],

                                    'Y-intersects': [self.animation_layers.layers_dict['y_axis_intersects_layer'],
                                                   self.booleans.booleans_dict['y_axis_intersects_mode']],

                                    'Line-intersects': [self.animation_layers.layers_dict['line_intersects_layer'],
                                                      self.booleans.booleans_dict['line_intersects_mode']],

                                    'Parameters': [self.animation_layers.layers_dict['params_layer'],
                                                 self.booleans.booleans_dict['parameters_mode']],

                                    'Modes layer': [self.animation_layers.layers_dict['show_modes_layer'],
                                                 True],

                                    'Derivatives': [self.animation_layers.layers_dict['derivatives_layer'],
                                                 self.booleans.booleans_dict['derivatives_mode']],
                                    
                                    'Steps change': [None, self.booleans.booleans_dict['steps_change_mode']],
                                    
                                    'General solution': [None, self.booleans.booleans_dict['general_solution_mode']],
                                    
                                    'Rotated background': [None, self.booleans.booleans_dict['rotated_background_mode']],
                                    
                                    'Zero missing point': [None, self.booleans.booleans_dict['zero_missing_point_mode']]
                                   }

    def reset_dicts(self):
        
        for obj in self.variable_dict_objects:
            obj.reset_dict()
            
        '''
        Logic for retaining the 'general solution' in its current state despite the reinitialization of mode_statuses_dict.
        '''
        curr_status_gen_solution = self.mode_statuses_dict['General solution'][1]
        self.initialize_mode_status_dict()
        self.mode_statuses_dict['General solution'][1] = curr_status_gen_solution
        
           
    def switch_mode(self, mode):
        self.mode_statuses_dict[mode][1] = not self.mode_statuses_dict[mode][1]
        
    @property
    def slope(self):
        
        current_a_param = self.get_curr_param('a')
        current_a_param = current_a_param * pi/180
        slope = tan(current_a_param)
        
        return round(slope, 14)

  
