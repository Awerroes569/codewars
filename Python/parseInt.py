NUMBERS={
            "zero":0,
            "one":1,
            "two":2,
            "three":3,
            "four":4,
            "five":5,
            "six":6,
            "seven":7,
            "eight":8,
            "nine":9,
            "ten":10,
            "eleven":11,
            "twelve":12,
            "thirteen":13,
            "fourteen":14,
            "fifteen":15,
            "sixteen":16,
            "seventeen":17,
            "eighteen":18,
            "nineteen":19,
            "twenty":20,
            "thirty":30,
            "forty":40,
            "fifty":50,
            "sixty":60,
            "seventy":70,
            "eighty":80,
            "ninety":90,
            "hundred":100,
            "thousand":1000,
            "million":1000000
            }

def parse_int(string):
    string=string.replace("-"," ")
    string=string.replace(" and"," ")
    elements=string.split()
    indices=[-1,-1,-1]
    try:
        indices[0]=len(elements) - 1 - elements[::-1].index("million")
    except ValueError:
        pass
    try:
        indices[1]=len(elements) - 1 - elements[::-1].index("thousand")
    except ValueError:
        pass
    try:
        indices[2]=len(elements) - 1 - elements[::-1].index("hundred")
    except ValueError:
        pass
    numbers=[]
    for i in elements:
        numbers.append(NUMBERS[i])
    if indices[1]<indices[0]:
        indices[1]=-1
    if indices[2]<indices[0] or indices[2]<indices[1]:
        indices[2]=-1
    curr_index=0  
    result=0
    for i in indices:
        if i>-1:
            partial_result=calculate_part(numbers[curr_index:i+1])
            result+=partial_result
            curr_index=i+1
    left=calculate_part(numbers[curr_index:len(numbers)])
    result+=left    
    return result

def calculate_part(part):
    if len(part)<1:
        return 0
    result=part.pop(0)
    for i in part:
        if result>i:
            result+=i
        else:
            result*=i
    return result