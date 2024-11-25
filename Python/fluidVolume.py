"""
heightmap:
  8 8 8 8 6 6 6 6
  8 0 0 8 6 0 0 6
  8 0 0 8 6 0 0 6
  8 8 8 8 6 6 6 0
"""
raw = [[8, 8, 8, 8, 6, 6, 6, 6],
         [8, 0, 0, 8, 6, 0, 0, 6],
         [8, 0, 0, 8, 6, 0, 0, 6],
         [8, 8, 8, 8, 6, 6, 6, 0]]

DIRECTIONS=[(0, 1), (0, -1), (1, 0), (-1, 0)]

def convertToDict(heightmap):
    result = {}
    for row in range(len(heightmap)):
        for column in range(len(heightmap[row])):
            result[(row, column)] = heightmap[row][column]
    return result

def findMins(heightmap):
    minimum = min(heightmap.values())
    return minimum

def collectMins2(heightmap, minimum):
    result = []
    for row in range(len(heightmap)):
        for column in range(len(heightmap[row])):
            if heightmap[row][column] == minimum:
                result.append((row, column))
    return result

def collectMins(heightmap, minimum):
    result = []
    for key in heightmap:
        if heightmap[key] == minimum:
            result.append(key)
    return result

def findGroup2(minimums, start):
    group=[]
    minimums.remove(start)
    furnace=[start]
    while furnace:
        current=furnace.pop(0)
        group.append(current)
        for direction in DIRECTIONS:
            try:
                new=(current[0]+direction[0], current[1]+direction[1])
            except:
                continue
            if new in minimums:
                minimums.remove(new)
                furnace.append(new)
    return group

def findGroup(minimums, start):
    group=[]
    minimums.remove(start)
    furnace=[start]
    while furnace:
        current=furnace.pop(0)
        group.append(current)
        for direction in DIRECTIONS:
            new=(current[0]+direction[0], current[1]+direction[1])
            if new in minimums:
                minimums.remove(new)
                furnace.append(new)
    return group

def findGroups(minimums):
    minimums=minimums[:]
    groups=[]
    while minimums:
        group=findGroup(minimums, minimums[0])
        groups.append(group)
    return groups

def volume(heightmap):
    return 0

mapDict = convertToDict(raw)
minimum = findMins(mapDict)
minimums = collectMins(raw, minimum)
groups = findGroups(minimums)
print(groups)



