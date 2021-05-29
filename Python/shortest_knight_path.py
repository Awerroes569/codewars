horizontals={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}

moves=[[x,y] for x in (-2,2)for y in (-1,1)]+[[x,y] for x in (-1,1)for y in (-2,2)]

def decode_coordinates(coordinate):
    return (horizontals[coordinate[0]],8-int(coordinate[1]))    

def input_next_move(start,value):#,board):
    poss=[(start[0]+i[0],start[1]+i[1])for i in moves ]
    real_poss=[(i[0],i[1]) for i in poss if (i[0]>-1 and i[1]>-1 and i[0]<8 and i[1]<8)]
    return real_poss

def knight(p1, p2):
     if p1==p2:
         return 0
     start={decode_coordinates(p1)}
     end=decode_coordinates(p2)
     counter=0
     while(True):
         counter+=1
         addings=set()
         for i in start:
             new_positions=input_next_move(i,1)
             if end in new_positions:
                 return counter
             addings.update(new_positions)
         start.update(addings)