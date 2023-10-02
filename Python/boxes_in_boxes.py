def produce_box(size):
    boxes = [[[1]]]
    counter=1
    while counter<size+1:
        new_box = glue(boxes[:])
        boxes.append(fill(new_box[:]))
        counter+=1
    return boxes[size-1][:]

def glue(boxes):
    size=max(boxes[-1][-1])+1
    result=[[size]*size]+[line[:] for box in boxes for line in box]
    return result[:]

def fill(box):
    content=max(box[-1])+1
    box=box[:]
    for line in box:
        diff=content-len(line)
        if diff>0:
            line+=[content]*diff
    return box[:]

def produce_top(size):
    return ' '+ ' '.join('_'*size)+' \n'

def produce_bottom(size):
    return '|' + '|'.join('_'*size)+'|'

def decode_box(size,box):
    last_box=box[:]
    height=len(last_box)
    width=size

    decoded=produce_top(size)

    for row in range(0,height-1):
        decoded_line='|'
        for column in range(width-1,-1,-1):

            if last_box[row][column]==last_box[row+1][column]:
                decoded_line+=' '
            else:
                decoded_line+='_' 
            if column and last_box[row][column] == last_box[row][column-1]:
                decoded_line+=' '
            else:
                decoded_line+='|'
        decoded_line+='\n'
        decoded+=decoded_line
    decoded+=produce_bottom(width)

    return decoded

def draw(size):
    box=produce_box(size)
    return decode_box(size,box)
