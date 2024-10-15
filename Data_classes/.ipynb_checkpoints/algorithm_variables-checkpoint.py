from Data_classes.data_abstract import Data
import inspect

class AlgorithmVariables(Data):
    
    n = 0
    m = 0
    total_n = 0
    
    def __init__(self):
        super().__init__()
        self.algorithm_vars_dict = {}
        self.excluded_methods_names = [name[0] for name in inspect.getmembers(AlgorithmVariables, predicate=inspect.isfunction)] + ['_abc_impl']

    
    def create_dict(self):        
        
        for name, value in AlgorithmVariables.__dict__.items():
            if not name.startswith('__') and name not in self.excluded_methods_names:
                
                self.algorithm_vars_dict[name] = value