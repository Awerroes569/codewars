raw="7 15 4 100 15 25 2 175 2 25 5 175 2 25 5"
raw2 = '10 35 500000000 200 500000000'

def decode(rle):
    rle=(x for x in rle.split(' '))
    columns=int(next(rle))
    matrix=[]
    while True:
        try:
            next_value=next(rle)
            next_counts=next(rle)
            for _ in range(int(next_counts)):
                matrix.append(next_value)
        except StopIteration:
            ##print('iteration stopped')
            break
    result=[]
    while matrix:
        result.append(matrix[:columns])
        matrix=matrix[columns:]
    return result[:]
        

def to_rle(data):
    #print(f'data: {data[0]}')
    column=len(data[0])
    data=data[:]
    gen_data=(y for x in data for y in x)
    #gen_data=(x for x in data)
    value=next(gen_data)
    next_value=next(gen_data)
    count=1
    result=[]
    while True:
        try:
            if value==next_value:
                count+=1
            else:
                result.append(value)  
                result.append(count)
                count=1
            value=next_value
            next_value=next(gen_data) 
        except StopIteration:
            #print('stop iteration')
            result.append(value)
            result.append(count)
            break
    return str(column)+' '+' '.join(str(x) for x in result).rstrip()

def calculate_diff(row,column,matrix):
    value=int(matrix[row][column])
    DIRECTIONS=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    result=0
    for direction in DIRECTIONS:
        try:
            r,c=direction
            if row+r>-1 and column+c>-1:
                neighbour=int(matrix[row+r][column+c])
                #print(f'neighbour: {neighbour}')
                diff=abs(value-neighbour)
                result=max(result,diff)
        except IndexError:
            continue
    return result

def transform(matrix):
    r,c=len(matrix),len(matrix[0])
    result=[[0 for column in range(c)] for row in range(r) ]
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            result[row][column]=(calculate_diff(row,column,matrix))
    return result[:]

def edge_detection(raw):
    data=decode(raw)
    print(f'after decode: {data}')

    transformed=transform(data)
    print(f'after transformed: {transformed}')
    return to_rle(transformed)

def decode2(data):
    data=(x for x in data.split(' '))
    column=int(next(data))
    count=0
    results=[]
    while True:
        try:
            value=int(next(data))
            counter=int(next(data))
            count+=counter
            results.append((value,count))
        except StopIteration:
            break
    return results[:]

for item in decode2(raw2):
    print(item)

def detect_zero(data, columns):
    rows=data[1]//columns
    return rows

def is_row_full(counter, columns):
    return counter%columns

def columns_to_fill(counter, columns):
    return columns-counter%columns

def generate_decoded(data, columns):
    data=decode2(data)
    result=[]
    counter=0

def count_new_values(data, columns):
    result=[]
    for column in data[1]:
        result.append(calculate_diff(1,column,data))

def create_row(data, columns):
    for i in range(columns):
        yield next(data)
    result=[]
    for column in range(columns):
        result.append(calculate_diff(1,column,data))
    return result[:]
        


print(decode2(raw2))

print(detect_zero((38,500), 7))

