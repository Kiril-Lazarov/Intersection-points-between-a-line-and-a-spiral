import pygame 

from Data_classes.variables import Variables
from Data_classes.constants import Constants
from Data_classes.booleans import Booleans
from Data_classes.algorithm_variables import AlgorithmVariables
from Animation_layers.animation_layers import AnimationLayers


class DataProcessing(Variables, Constants, Booleans, 
                     AlgorithmVariables, AnimationLayers):
    
    bg_color = (255, 255, 255)
    
    variables = Variables()
    variables.create_dict()
  
    constants = Constants()
    constants.create_dict()
    
    booleans = Booleans()
    booleans.create_dict()

    algorithm_vars = AlgorithmVariables()
    algorithm_vars.create_dict()
    
    animation_layers = AnimationLayers()
    animation_layers.create_dict()
    
    variable_dict_objects = [variables, booleans, constants,algorithm_vars]
    
    mode_statuses_dict = {'Coordinates':[animation_layers.layers_dict['background_surface'],
                                         booleans.booleans_dict['background_mode']],
                          
                          'Algorithm mode': [animation_layers.layers_dict['algorithm_layer'],
                                             booleans.booleans_dict['algorithm_mode']],
                          
                          'Algorithm data mode': [animation_layers.layers_dict['show_algorithm_data_layer'],
                                                  booleans.booleans_dict['algorithm_data_mode']],
                          
                          'T-diagram': [None,  booleans.booleans_dict['t_diagram_mode']],
                          
                          'Vertical line': [animation_layers.layers_dict['vertical_line_layer'],
                                            booleans.booleans_dict['vertical_line_mode']],
                          
                          'Spiral': [animation_layers.layers_dict['spiral_layer'],
                                     booleans.booleans_dict['spiral_mode']],
                          
                          'Y-intersects': [animation_layers.layers_dict['y_axis_intersects_layer'],
                                           booleans.booleans_dict['y_axis_intersects_mode']],
                          
                          'Line-intersects': [animation_layers.layers_dict['line_intersects_layer'],
                                              booleans.booleans_dict['line_intersects_mode']],
                          
                          'Parameters': [animation_layers.layers_dict['params_layer'],
                                         booleans.booleans_dict['parameters_mode']],
                          
                          'Modes layer': [animation_layers.layers_dict['show_modes_layer'],
                                         True],
                          
                          'Derivatives': [animation_layers.layers_dict['derivatives_layer'],
                                         booleans.booleans_dict['derivatives_mode']]
                           }

    def blit_layers(self, win):

        win.fill(self.bg_color)

        for layer, boolean in self.mode_statuses_dict.values():
            if boolean and layer is not None:
                win.blit(layer, (0, 0))

    def get_curr_param(self, param):
        
        if param == 'c':
            return [self.constants.constants_dict[param][0] + self.variables.variables_dict[param][0],
                    self.constants.constants_dict[param][1] + self.variables.variables_dict[param][1]]
        
        return self.constants.constants_dict[param] + self.variables.variables_dict[param]

    def reset_dicts(self):
        
        for obj in self.variable_dict_objects:
            obj.reset_dict()
  
