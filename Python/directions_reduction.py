def dir_reduc(arr):
    arr=arr[:]
    while True:
        index=find_opposite_index(arr)
        if index == -1:
            return arr
        arr=reduction(arr,index)


OPPOSITES=[('NORTH', 'SOUTH'), ('EAST', 'WEST'), ('SOUTH', 'NORTH'), ('WEST', 'EAST')]

def is_opposite(dir1, dir2):
    return (dir1, dir2) in OPPOSITES

def find_opposite_index(arr):
    if len(arr) < 2:
        return -1
    for i in range(len(arr)-1):
        if is_opposite(arr[i], arr[i+1]):
            return i
    return -1

def reduction(arr,index):
    return arr[:index] + arr[index+2:] 
    

