import pygame
import inspect

from Data_classes.data_abstract import Data
from Data_classes.constants import Constants

screen_width = Constants.screen_width
screen_height = Constants.screen_height

class AnimationLayers(Data):

    # Layers
    win = pygame.display.set_mode((screen_width, screen_height)) # Main animation layer
    background_surface = pygame.Surface((screen_width, screen_height))

    ''' Dynamic layers - those that are connected with changeable spiral and line variables '''

    derivatives_layer = pygame.Surface((screen_width, screen_height),pygame.SRCALPHA)
    vertical_line_layer = pygame.Surface((screen_width, screen_height),pygame.SRCALPHA)
    spiral_layer = pygame.Surface((screen_width, screen_height),pygame.SRCALPHA)
    y_axis_intersects_layer = pygame.Surface((screen_width, screen_height),pygame.SRCALPHA)
    line_intersects_layer = pygame.Surface((screen_width, screen_height),pygame.SRCALPHA)


    ''''Mode layers'''
    # A layer that visualizes the consecutive steps of the algorithm for finding the intersection point between the spiral and the line. 
    algorithm_layer = pygame.Surface((screen_width, screen_height),pygame.SRCALPHA)
    
    circle_layer = pygame.Surface((screen_width, screen_height),pygame.SRCALPHA)
    
    equation_layer = pygame.Surface((screen_width, screen_height),pygame.SRCALPHA)

    '''Data layers'''

    # Layer that shows the current status of the spiral and the line parameters 
    params_layer = pygame.Surface((screen_width, screen_height),pygame.SRCALPHA) 

    # Shows current status of the switch modes variables
    show_modes_layer = pygame.Surface((screen_width, screen_height),pygame.SRCALPHA) 

    show_algorithm_data_layer = pygame.Surface((screen_width, screen_height),pygame.SRCALPHA)
    
    explanations_layer = pygame.Surface((screen_width, screen_height),pygame.SRCALPHA)
    
    
    
    def __init__(self):
        super().__init__()
        self.layers_dict = {}
        self.excluded_methods_names = [name[0] for name in inspect.getmembers(AnimationLayers,       
                                        predicate=inspect.isfunction)] + ['_abc_impl']
    
    def create_dict(self):        
        
        for name, value in AnimationLayers.__dict__.items():
            if not name.startswith('__') and name not in self.excluded_methods_names:
                
                self.layers_dict[name] = value

        