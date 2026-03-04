from pathlib import Path

"""
path=Path("Logical Programs")
print(path.exists())
"""

"""
path= Path("noob")
print(path.mkdir())   #make directory named noob 
#print(path.rmdir())  rem   ove directory named noob
"""

path = Path(".") #current directory
for file in path.glob('*.py'):
    print(file)

"""
If you want to see Python files in subfolders of demo as well, you’d use:
    for file in path.rglob("*.py"):
    print(file)
"""