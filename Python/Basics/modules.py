def greeting(name):
    print(f"Good Morning {name}")


def con_kg_to_g(weight):
    gram= weight*1000
    print(f"{weight}kg= {gram}g")

def con_g_to_kg(weight):
    k_gram= float(weight)/1000
    print(f"{weight}g= {k_gram}kg")


def findmax(number):
    max=number[0]
    for i in  range(1, len(number)):
        if(number[i]>max):
            max=number[i]
    
    print(f"Largest= {max}")