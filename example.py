"'Welcome to Python World'"

def sample():
    print('Welcome to Module')
    
def add(*a):
    s = 0
    for i in a:
        s += i
    return s