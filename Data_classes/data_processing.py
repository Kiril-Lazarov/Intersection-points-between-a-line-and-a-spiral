from Data_classes.variables import Variables
from Data_classes.constants import Constants
from Data_classes.booleans import Booleans
from Data_classes.additional_variables import AdditionalVariables
from Data_classes.algorithm_variables import AlgorithmVariables
from Animation_layers.animation_layers import AnimationLayers


class DataProcessing(Variables, Constants, Booleans, 
                     AdditionalVariables, AlgorithmVariables, AnimationLayers):
    
    bg_color = (255, 255, 255)
    
    variables = Variables()
    variables.create_dict()
  
    constants = Constants()
    constants.create_dict()
    
    booleans = Booleans()
    booleans.create_dict()
    
#     add_vars = AdditionalVariables()
#     add_vars.create_dict()
    
    algorithm_vars = AlgorithmVariables()
    algorithm_vars.create_dict()
    
    animation_layers = AnimationLayers()
    animation_layers.create_dict()
    
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
                                           booleans.booleans_dict['y_axis_intersects']],
                          
                          'Line-intersects': [animation_layers.layers_dict['line_intersects_layer'],
                                              booleans.booleans_dict['line_intersects']],
                          
                          'Parameters': [animation_layers.layers_dict['params_layer'],
                                         booleans.booleans_dict['parameters_mode']],
                          
                          'Modes layer': [animation_layers.layers_dict['show_modes_layer'],
                                         True],
                          
                          'Derivatives': [animation_layers.layers_dict['derivatives_layer'],
                                         booleans.booleans_dict['derivatives_mode']]
                           }
    
    '''Variables dict: {'screen_width': 1500, 'screen_height': 800, 'half_screen_width': 750.0, 'half_screen_height': 400.0, 'coord_origin': [750.0, 400.0], 'FPS': 24, 'units': 20, 'half_units': 10.0, 'length': 75.0, 'l_step': 3, 'deg_step': 1, 't_step': 0.025, 'v_step': 0.025, 'w_step': 0.025, 'k_step': 0.025, 'x_step': 0.03, 'c_step': 10}

Constants dict: {'deg': 0, 't': 1, 'v': 1, 'w': 1, 'k': 0, 'vert_line_x': 1}

Booleans dict: {'background_mode': True, 'algorithm_mode': False, 'vertical_line_mode': True, 'derivatives_mode': False, 'spiral_mode': True, 'y_axis_intersects': True, 'line_intersects': True, 'algorithm_data_mode': True, 'parameters_mode': True, 't_diagram_mode': False, 'switch_mode': <function Booleans.switch_mode at 0x000001C640942310>}

Add_vars dict: {'deg_additional': 0, 't_additional': 0, 'v_additional': 0, 'w_additional': 0, 'x_additional': 0, 'k_additional': 0, 'l_additional': 0, 'coord_additional': [0, 0]}

Algorithm_vars dict: {'n': 0, 'm': 0, 'total_n': 0}

Animation_layers dict: {'win': <Surface(Dead Display)>, 'background_surface': <Surface(1500x800x32 SW)>, 'derivatives_layer': <Surface(1500x800x32 SW)>, 'vertical_line_layer': <Surface(1500x800x32 SW)>, 'spiral_layer': <Surface(1500x800x32 SW)>, 'y_axis_intersects_layer': <Surface(1500x800x32 SW)>, 'line_intersects_layer': <Surface(1500x800x32 SW)>, 'algorithm_layer': <Surface(1500x800x32 SW)>, 'params_layer': <Surface(1500x800x32 SW)>, 'show_modes_layer': <Surface(1500x800x32 SW)>, 'show_algorithm_data_layer': <Surface(1500x800x32 SW)>}

dict_keys(['Coordinates', 'Algorithm mode', 'Algorithm data mode', 'T-diagram', 'Vertical line', 'Spiral', 'Y-intersects', 'Line-intersects', 'Parameters', 'Modes layer', 'Derivatives'])'''
