def snail(snail_map):
    result=[]
    
    def isEmpty(current_map):
        return len(current_map)<1 or len(current_map[0])<1
    
    while True:
        
        #to right
        if isEmpty(snail_map):
            break
        result.extend(snail_map[0])
        snail_map.pop(0)
        #to down
        if isEmpty(snail_map):
            break
        for item in snail_map:
            result.append(item[-1])
            item.pop(-1)
        #to left
        if isEmpty(snail_map):
            break
        for i in range(len(snail_map[-1])-1,-1,-1):
            result.append(snail_map[-1][i])
        snail_map.pop(-1)
        #to up
        if isEmpty(snail_map):
            break
        for i in range(len(snail_map)-1,-1,-1):
            result.append(snail_map[i][0])
            snail_map[i].pop(0)
    return result