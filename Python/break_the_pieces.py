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
allowed=('|','-')

hv_arrows=(
        #up
        (0,-1),
        #right
        (1,0),
        #down
        (0,1),
        #left
        (-1,0)
        )
        
def break_pieces(shape):  
    result=list()
    extremies=dict()
    index=1
    bcshape=[list(x) for x in shape.split('\n')]
    columns=detect_max_row(bcshape)
    rows=len(bcshape)
    cshape=normalization(bcshape,columns)
    if rows<3 or columns<3:
        return None
    while(True):
        a,b=detect_empty(cshape,rows,columns)
        if a<0 and b<0:
            break
        cshape[a][b]=str(index)
        change_area(cshape,rows,columns,index)
        index+=1      
    for i in range(1,index):
        extremies[i]=detect_extremies(cshape,rows,columns,i)
    for i,j in extremies.items():
        rawdiamond=plus_remover(cut_shape(cshape,j,i))
        diamond=None
        if validate_pluses(rawdiamond):
            diamond=making_final_string(rawdiamond)
        if diamond:
            if validator(diamond):
                result.append(diamond)
    if len(result):
        return sorted(result)
    return None

def validate_pluses(shape):
    if shape==None:
        return False
    for i in range(len(shape)):
        for j in range(len(shape[0])):
            if shape[i][j]=="+":
                number=0
                for k in hv_arrows:
                    try:
                        if shape[i+k[1]][j+k[0]] in allowed and i+k[1]!=-1 and j+k[0]!=-1:
                            number+=1
                    except IndexError:
                        pass
                if number!=2:
                    return False
    return True

def validator(string):
    for i in string:
        if i.isnumeric():
            return False
    if '+' not in string:
            return False
    return True

def making_final_string(shape):
    if shape==None:
        return None
    return "\n".join(["".join(x).rstrip() for x in shape])
      

def cut_shape(cshape,coord,index):
    try:
        outcome=emptying_shape([cshape[y][coord[0][1]-1:coord[1][1]+2] for y in range(coord[0][0]-1,coord[1][0]+2)],index)
        return outcome
    except IndexError:
        return None
def emptying_shape(shape,index):
    cshape=copy.deepcopy(shape)
    for i in range(len(shape)):
        for j in range(len(shape[0])):
            if not detect_index(shape,i,j,index) or shape[i][j]==str(index):
                cshape[i][j]=" "
    return cshape

def plus_remover(shape):
    if shape==None:
        return shape
    for i in range(len(shape)):
        for j in range(1,len(shape[0])-1):
            if shape[i][j]=='+' and shape[i][j-1]=='-' and shape[i][j+1]=='-':
               shape[i][j]='-' 
    for j in range(len(shape[0])):
        for i in range(1,len(shape)-1):
            if shape[i][j]=='+' and shape[i-1][j]=='|' and shape[i+1][j]=='|':
               shape[i][j]='|' 
    return shape
    
def detect_extremies(shape,rows,columns,index):
    min_row=rows+1
    min_column=columns+1
    max_row=-10
    max_column=-10
    
    for i in range(rows):
        for j in range(columns):
            if shape[i][j]==str(index):
                if i>max_row:
                    max_row=i
                if i<min_row:
                    min_row=i
                if j>max_column:
                    max_column=j
                if j<min_column:
                    min_column=j
    return [(min_row,min_column),(max_row,max_column)]
    
    
def detect_empty(shape,rows,columns):
    for i in range(rows):
        for j in range(columns):
            if shape[i][j]==" ":
                return i,j
    return -1,-1

def detect_index(shape,rows,columns,index):
    for i in arrows:
        if safe_getter (shape,columns,rows,i)==str(index):
            return True
    return False

def change_cell(shape,rows,columns,index):
    try:
        if shape[rows][columns]==" " and detect_index(shape,rows,columns,index):
            shape[rows][columns]=str(index)
            return 1
    except IndexError:
        pass
    return 0
        
def change_area(shape,rows,columns,index):
    checker=1
    while checker:
        checker=0
        for i in range(rows):
            for j in range (columns):
                checker+=change_cell(shape,i,j,index)    
        if checker<1:
            return
        
def safe_getter (universe, x,y,arrow):
  try:
    return universe[y+arrow[1]][x+arrow[0]]
  except IndexError:
    return 0

def detect_max_row(shape):
    return max([len(x)for x in shape])

    
def normalization(shape,maxrow):
    return [x+[" "]*(maxrow-len(x))for x in shape] 
