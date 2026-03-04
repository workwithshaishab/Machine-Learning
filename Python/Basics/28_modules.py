#  Modules are files that contain Python code — functions, classes, and variables — 
#  which you can reuse in your programs.

import modules
from modules import con_kg_to_g, con_g_to_kg

# Using function with full module name
# if only import modules was done
print(modules.greeting("Leo"))


# Using directly (since imported separately)
con_kg_to_g(2.5)
con_g_to_kg(3466)
