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
            b = self.get_curr_param('b')
            
            a_turn_on = a/X_bin(a)
            b_turn_on = b/X_bin(b)
        
            return (1- a_turn_on)* b + a_turn_on *b_turn_on* cos(pi/2 - abs(arctan(a))) * (X_bin(-b))/X_bin(a)
        
        result = self.constants.constants_dict[param] + self.variables.variables_dict[param]
        return float(f'{result:.{self.constants.accuracy + 9}f}')
    
    def initialize_mode_status_dict(self):

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
    
    @property
    def background_params(self):
        
        background_surface = self.animation_layers.layers_dict['background_surface']
        screen_width = self.constants.screen_width
        screen_height = self.constants.screen_height
        length = self.get_curr_param('l')

        center_point = self.get_curr_param('c')
        
        return [background_surface, screen_width, screen_height, length, center_point, self.bg_color]
    
    @property
    def line_params(self):
        
        line_layer = self.animation_layers.layers_dict['vertical_line_layer']
        screen_height = self.constants.screen_height
        screen_width = self.constants.screen_width
        half_screen_width = self.constants.half_screen_width
        half_screen_height = self.constants.half_screen_height
        
        a = self.get_curr_param('a')
        b = self.get_curr_param('b')
        x = self.get_curr_param('x')
        length = self.get_curr_param('l')
        center_point_width, center_point_height = self.get_curr_param('c')
        slope_a = self.slope
        
        t_diagram = self.mode_statuses_dict['T-diagram'][1]
        general_solution = self.mode_statuses_dict['General solution'][1]
        rotated_background = self.mode_statuses_dict['Rotated background'][1]
        
        return [line_layer, screen_height, screen_width, half_screen_width, half_screen_height, 
                a, b, x, length, center_point_width, center_point_height, slope_a,
                t_diagram, general_solution, rotated_background]
    
    @property
    def derivatives_params(self):
        
        layer, derivative = self.mode_statuses_dict['Derivatives']
    
        center_point_width, center_point_height = self.get_curr_param('c')

        length = self.get_curr_param('l')

        deg_x, deg_y = self.get_curr_param('deg')
        t = self.get_curr_param('t')
        v = self.get_curr_param('v')
        w = self.get_curr_param('w')
        k = self.get_curr_param('k')
        
        screen_width = self.constants.screen_width
        screen_height = self.constants.screen_width
        
        derivative_slopes = self.derivative_slopes
        
        t_diagram = self.mode_statuses_dict['T-diagram'][1]
        
        return [layer, center_point_width, center_point_height, 
                length, deg_x, deg_y, t, v, w, k,
                screen_width, screen_height, t_diagram,
                derivative, derivative_slopes]
    
    @property
    def spiral_params(self):
        
        spiral_layer = self.animation_layers.layers_dict['spiral_layer']

        half_screen_width = self.constants.half_screen_width
        half_screen_height = self.constants.half_screen_height
  
        center_point_width, center_point_height = self.get_curr_param('c')
        length = self.get_curr_param('l')
        deg = self.get_curr_param('deg')
        t = self.get_curr_param('t')
        v = self.get_curr_param('v')
        w = self.get_curr_param('w')
        k = self.get_curr_param('k')
        
        spiral_coordinates = self.spiral_coordinates
        
        t_diagram = self.mode_statuses_dict['T-diagram'][1]
        
        return [spiral_layer, half_screen_width, half_screen_height, 
                center_point_width, center_point_height, length,
                deg, t, v, w, k, spiral_coordinates, t_diagram] 
    
    @property
    def y_intersects_t_params(self):
        
        deg_x, deg_y  =  self.get_curr_param('deg')
        
        k = self.get_curr_param('k')
        w = self.get_curr_param('w')
        t = self.get_curr_param('t')
        v = self.get_curr_param('v')
        x_line = self.get_curr_param('x')

        a = self.slope
        b = self.get_curr_param('b')
        
        steps_change = self.mode_statuses_dict['Steps change'][1]
        zero_missing_point_mode = self.mode_statuses_dict['Zero missing point'][1]
        general_solution = self.mode_statuses_dict['General solution'][1]
        
        return [deg_x, deg_y , t, v, w, k, x_line, a, b, 
                steps_change, zero_missing_point_mode,
                general_solution]
    
    @property
    def draw_dots_params(self):
        
        const_center_point = self.constants.constants_dict['c']
        var_center_point = self.variables.variables_dict['c']

        length = self.get_curr_param('l')

        deg_x, deg_y = self.get_curr_param('deg')
        v = self.get_curr_param('v')
        w = self.get_curr_param('w')
        k = self.get_curr_param('k')

        t_diagram = self.mode_statuses_dict['T-diagram'][1]
        
        mode_statuses_dict = self.mode_statuses_dict
        
        return [deg_x, deg_y, v, w, k, length,
                const_center_point, var_center_point,
                t_diagram, mode_statuses_dict]
        
   
  
