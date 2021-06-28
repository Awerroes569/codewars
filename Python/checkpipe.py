class Pipe(object):
    UPS=(9495,9475,9507,9547,9499,9515,9531)
    DOWNS=(9491,9487,9475,9507,9515,9523,9547)
    RIGHTS=(9495,9487,9473,9507,9523,9531,9547)
    LEFTS=(9491,9499,9473,9515,9523,9531,9547)
    
    def __init__(self):
        self._up = False
        self._right = False
        self._down = False
        self._left = False
        self._water = False
        
    def specify_pipe(self,code):
        if code in Pipe.UPS:
            self._up=True
        if code in Pipe.DOWNS:
            self._down=True
        if code in Pipe.RIGHTS:
            self._right=True
        if code in Pipe.LEFTS:
            self._left=True
        
def first_fill(pipes):
    max_row=max([x[0]for x in pipes.keys() ])
    max_column=max([x[1]for x in pipes.keys() ])
    for key,value in pipes.items():
        if (key[0]==0 and value._up) or (key[0]==max_row and value._down) or (key[1]==0 and value._left) or (key[1]==max_column and value._right):
            value._water=True
    
def next_fill(pipes):
    result=True
    full=[x for x,y in pipes.items() if y._water]
    for i in full:
        if not fill_neighbours(i,pipes):
            result=False
            break
    return (result,len(full))        

def decode_map(pipe_map):
    signs=[list(x) for x in pipe_map]
    return [[ord(y) for y in x] for x in signs]

def create_pipes(pipe_map):
    rows=len(pipe_map)
    columns=len(pipe_map[0])
    pipes={}
    for y in range(rows):
        for x in range(columns):
            key=(y,x)
            pipe=Pipe()
            pipes[key]=pipe
    return pipes

def connect_pipes(pipe_map,pipes):
    rows=len(pipe_map)
    columns=len(pipe_map[0])
    for y in range(rows):
        for x in range(columns):
            code=pipe_map[y][x]
            key=(y,x)
            pipes[key].specify_pipe(code)
            
def fill_neighbours(key,pipes):
    current=pipes[key]
    up,right,down,left=find_neighbours(key)
    if current._up:
        if pipes.get(up):
            if pipes[up]._down:
                pipes[up]._water=True
            else:
                return False
    if current._right:
        if pipes.get(right):
            if pipes[right]._left:
                pipes[right]._water=True
            else:
                return False
    if current._down:
        if pipes.get(down):
            if pipes[down]._up:
                pipes[down]._water=True
            else:
                return False
    if current._left:
        if pipes.get(left):
            if pipes[left]._right:
                pipes[left]._water=True
            else:
                return False
    return True

def find_neighbours(key):
    y=key[0]
    x=key[1]
    up=(y-1,x)
    right=(y,x+1)
    down=(y+1,x)
    left=(y,x-1)
    return (up,right,down,left)
            
def check_pipe(pipe_map):
    draft=decode_map(pipe_map) 
    pipes=create_pipes(draft)    
    connect_pipes(draft,pipes)
    first_fill(pipes)
    before=0
    while(True):
        hermetic,after=next_fill(pipes)
        if not hermetic:
            return False
        if after==before:
            return True
        before=after

    

