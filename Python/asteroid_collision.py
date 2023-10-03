def if_collision(asteroids):
    left,right=asteroids
    if left>0 and right<0:
        return True
    else:
        return False
    
def after_collision(asteroids):
    left,right=asteroids
    if abs(left)==abs(right):
        return ()
    elif abs(left)>abs(right):
        return (left,)
    else:
        return (right,)
    
def find_collision(asteroids):
    for i in range(len(asteroids)-1):
        if if_collision(asteroids[i:i+2]):
            return i
    return None



def asteroid_collision(asteroids):
    asteroids=asteroids[:]
    while True:
        if not asteroids:
            return []
        if len(asteroids)==1:
            return asteroids[:]
        i=find_collision(asteroids)
        if i is None:
            return asteroids[:]
        asteroids=asteroids[:i]+list(after_collision(asteroids[i:i+2]))+asteroids[i+2:]

