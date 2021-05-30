def parse_molecule (formula):
    
    starts=('[','{','(')
    ends=(']','}',')')
    elements=[]
    index=0
    result={}
    
    for item in formula:
        if item in starts:
            if len(elements):
                if elements[-1][0].isalpha():
                    elements.append(['1',index,1])
            index+=1
            elements.append(['(',index,0])
        elif item in ends:
            if elements[-1][0].isalpha():
                elements.append(['1',index,1])
            index-=1
            elements.append([')',index,0])
        elif item.isupper():
            if len(elements):
                if elements[-1][0].isalpha():
                    elements.append(['1',index,1])
            elements.append([item,index,0])
        elif item.islower():
            elements[-1][0]=elements[-1][0]+item
        elif item.isdigit():
            if elements[-1][0].isdigit():
                elements[-1][0]=elements[-1][0]+item
                elements[-1][2]=int(elements[-1][0])
            else:
                elements.append([item,index,int(item)])

    if elements[-1][0].isalpha():
        elements.append(['1',0,1])
    
    for i in range(len(elements)-1,1,-1):
        if elements[i][0].isdigit() and elements[i-1][0]==')':
            i_index=elements[i][1]
            multiplier=elements[i][2]
            isPeak=False
            for j in range(i-1,-1,-1):
                if isPeak and elements[j][1]==i_index:
                    break
                if elements[j][1]==i_index+1:
                    isPeak=True
                    elements[j][2]*=multiplier
                    
    
    for i in range(len(elements)):
        if elements[i][0].isalpha():
            if elements[i][0] in result.keys():
                result[elements[i][0]]+=elements[i+1][2]
            else:
                result[elements[i][0]]=elements[i+1][2]
    return dict(sorted(result.items(), key=lambda item: item[0]))