import random

def generate_array(minval,maxval,numofelements):
    return [random.randint(minval,maxval) for _ in numofelements]
