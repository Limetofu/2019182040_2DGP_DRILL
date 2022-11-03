# layer 0: Background
# layer 1: middle
# layer 2: Foreground

world = [[], [], []]

def add_object(o, depth):
    world[depth].append(o)
    
def add_objects(ol, depth):
    world[depth] += ol

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            del o
            return
    raise ValueError('Trying destroy non existing object')

def all_objects():
    for layer in world:
        for o in layer:
            yield o

def clear():
    for o in all_objects():
        del o
    for layer in world:
        layer.clear()

    

