def separate(poly):
    border=0
    for i in poly:
        if i.isalpha():
            break
        border+=1   
    number=poly[:border]
    if len(number)<2:
        number=number+"1"
    variables="".join(sorted(poly[border:]))
    return int(number),variables

def simplify(poly):
    result={}
    final=[]
    if poly[0] != "-":
        poly="+"+poly
    poly=poly.replace("+","&+")
    poly=poly.replace("-","&-")
    elements=poly.split("&")
    transformed=[separate(x) for x in [x for x in elements if x != ""]]
    for i in transformed:
        if i[1] in result.keys():
            result[i[1]]+=i[0]
        else:
            result[i[1]]=i[0]
    sorted_result = {key: val for key, val in sorted(result.items(), key = lambda ele: (len(ele[0]),ele[0]))}
    for i in sorted_result.keys():
        current=sorted_result[i]
        if current>0:
            final.append("+")
            if current != 1:
                final.append(str(current))
        elif current==0:
            continue
        else:
            final.append("-")
            if current != -1:
                final.append(str(-current))
        final.append(i)
        ultimate="".join(final)
        if ultimate[0] == "+":
            ultimate=ultimate.replace("+","",1)
    return ultimate