from itertools import combinations

raw = [[[3, -4],'blue'], 
       [[-7, -1], 'red'],
       [[7, -6], 'yellow'], 
       [[2, 5], 'yellow'],
       [[1, -5], 'red'], 
       [[-1, 4], 'red'],
       [[1, 7], 'red'], 
       [[-3, 5], 'red'],
       [[-3, -5], 'blue'], 
       [[4, 1], 'blue']]


def detectColours(input_):
    result = {x[1] for x in input_}
    return result

def collectColoursPoints(input_, colour):
    result = [x[0] for x in input_ if x[1] == colour]
    return result

def createPointsDict(input_):
    result = {x[1]:[] for x in input_}
    for x in input_:
        result[x[1]].append(x[0])
    return result

def verifyPoints(points):
    if len(points) != 3:
        return False
    if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
        return False
    if points[0][0] == points[1][0] == points[2][0]:
        return False
    if points[0][1] == points[1][1] == points[2][1]:
        return False
    if not (points[0][0]*(points[1][1]-points[2][1]) + points[1][0]*(points[2][1]-points[0][1]) + points[2][0]*(points[0][1]-points[1][1])):
        return False
    return True

def createTriangles(points):
    result = []
    for item in combinations(points, 3):
        if verifyPoints(item):
            result.append(item)
    return result

def createTrianglesDict(input_):
    result = {x:[] for x in input_}
    for x in input_:
        result[x] = createTriangles(input_[x])
    return result

def count_col_triang(input_):
    colorPointsBase = createPointsDict(input_)
    colorTrianglesBase = createTrianglesDict(colorPointsBase)
    totalPoints = len(input_)
    totalColours = len(colorPointsBase)
    totalTriangles = sum([len(x) for x in colorTrianglesBase.values()])
    highestColour = max([len(x) for x in colorTrianglesBase.values()])
    highestColours = sorted([x for x in colorPointsBase if len(colorTrianglesBase[x]) == highestColour])
    def createColourAnswer():
        result = []
        if highestColour > 0:
            for x in highestColours:
                result.append(x)
            result.append(highestColour)
        return result
    
    return [totalPoints, totalColours, totalTriangles, createColourAnswer()]
    

