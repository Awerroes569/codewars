import copy

ORDER=[4,3,3,2,2,2,1,1,1,1]

def validate_battlefield(battleField):
    if field_sum_check(battleField):
        return False
    firstOrder=copy.deepcopy(ORDER)
    firstField=copy.deepcopy(battleField)
    firstField.T
    fireplace=[(firstField,firstOrder)]
    while(len(fireplace)):
        currField,currOrder=fireplace.pop()
        if not field_sum(currField) and not len(currOrder):
            return True
        else:
            size=currOrder[0]
            for i in detect_ship(currField,size):
                newField=erase_ship(currField,i)
                newOrder=copy.deepcopy(currOrder)
                newOrder.pop(0)
                fireplace.append((newField,newOrder))
    return False
                

def field_sum_check(field,default=20):
    if field_sum(field)==default:
        return False
    else:
        return True
    
def field_sum(field):
    return sum([sum(x) for x in field])


def detect_ship(field,size):
    result=[]
    for y in range(len(field)):
        for x in range(len(field[0])-size+1):
            if sum(field[y][x:x+size])==size:
                result.append((size,y,x,True))
    if size>1:
        newfield=[list(x) for x in zip(*field)]
        for y in range(len(field[0])):
            for x in range(len(field)-size+1):
                if sum(newfield[y][x:x+size])==size:
                    result.append((size,x,y,False))            
    return result

def erase_ship(field,details):
    field=copy.deepcopy(field)
    size,row,column,horizontal=details
    if horizontal:
        for i in range(size):
            field[row][column+i]=0
    else:
        for i in range(size):
            field[row+i][column]=0
    return field

