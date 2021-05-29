import copy

arrows=(
        #up
        (0,-1),
        #upright
        (1,-1),
        #right
        (1,0),
        #rightdown
        (1,1),
        #down
        (0,1),
        #downleft
        (-1,1),
        #left
        (-1,0),
        #leftup
        (-1,-1)
        )
def safe_getter (universe, x,y,arrow):
  try:
    return universe[y+arrow[1]][x+arrow[0]]
  except IndexError:
    return 0

def creating_next_generation(universe):
    result=prepareTemplate(universe)
    for i in range(len(universe)):
        for j in range(len(universe[0])):
            total=0
            for k in arrows:
                total+=safe_getter(universe,j,i,k)
            result[i][j]=is_alive(universe[i][j],total)
    return result   

def extend_universe(universe):
    result=[]
    y=0
    x=len(universe)
    print(x)
    if x:
        y=len(universe[0])
        print(y)
    else:
        return [[]]
    result.append([0]*(y+2))
    for i in universe:
        toAdd=[0]
        toAdd.extend(i)
        toAdd.append(0)
        result.append(toAdd)  
    result.append([0]*(y+2))
    return result

def cut_top(universe):
    while(len(universe)):
        if not sum(universe[0]):
            universe=universe[1:]
        else:
            break
    return universe

def shrink_universe(universe):
    universe=cut_top(universe)
    universe.reverse()
    universe=cut_top(universe)
    universe.reverse()
    zipped=list(zip(*universe[:]))
    zipped=cut_top(zipped)
    zipped.reverse()
    zipped=cut_top(zipped)
    zipped.reverse()
    unzipped=list(zip(*zipped[:]))
    return [list(x) for x in unzipped]

def is_alive(current,total):
    if current:
        if total==2 or total==3:
            return 1
        else:
            return 0
    elif total==3:
        return 1
    else:
        return 0
        
def prepareTemplate(universe):
    result=[]
    try:
        line=[0]*len(universe[0])
        for i in range(len(universe)):
            result.append(copy.deepcopy(line))
        return result
    except IndexError:
        return [[]]

def get_generation(cells, generations):
    universe=cells
    for i in range(generations):
        universe=extend_universe(universe)
        universe=shrink_universe(creating_next_generation(universe))
    return universe