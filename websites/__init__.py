import os
from os import listdir

__all__ = []


module_list = os.listdir(os.getcwd()+"/websites")

for language in module_list:
    module_name = language[:-3]
    if module_name != "__init__" and module_name != "__pycach" and module_name != "debug":
           __all__.append(module_name)


