# https://stackoverflow.com/questions/19140589/linear-congruential-generator-in-python

def seedLCG(initVal):
    global rand
    rand = initVal

def lcg(seed):
    a = 1140671485
    c = 128201163
    m = 2**24
    global rand
    rand = (a*rand + c) % m
    return rand / m

def runLCG(n):
    nums_list = []
    for i in range(n):
        nums_list.append(lcg())
    return nums_list