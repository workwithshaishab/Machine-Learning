#  A package is a way to organize multiple modules into a folder
#  container for different module

"""
    import mypackage.conversions
    mypackage.conversions.kg_to_g
    print(mypackage.conversions.kg_to_g(1))
"""

"""
from mypackage import conversions 
✅ valid, it imports the conversions module from the mypackage.

from conversions import kg_to_g 
❌ invalid, because Python doesn’t know conversions by itself (it lives inside mypackage).
"""
from mypackage.conversions import kg_to_g
print(kg_to_g(34))

"""
from mypackage import kg_to_g
We can do this as we have already import those functions in __init__.py
"""