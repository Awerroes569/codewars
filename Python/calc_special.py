def calc_special( lastDigit,base ):
    counter=2
    while(True):
        candidate=calculate_candidate(lastDigit,counter,base)
        to_check=candidate//lastDigit
        to_compare=moving_front_last(prepare_parasite(candidate,base))
        if to_check*lastDigit==candidate and prepare_parasite(to_check,base)==to_compare:
            return to_compare
        counter+=1

def prepare_parasite(number,base):
    to_verify=""
    if base==16:
        to_verify=str(hex(number))[2:].upper()
    elif base==8:
        to_verify=str(oct(number))[2:]
    else:
        to_verify=str(number)
    return to_verify
    
def moving_front_last(number):
    digits=[x for x in str(number)]
    result="".join(digits[1:]+digits[:1])
    return result

def calculate_candidate(number,lenght,base):
    result=(number*int(pow(base,lenght))-number*number)//(base*number-1)+number*int(pow(base,lenght))
    return result
  
#print(calculate_candidate4(4,2,16))
#print(hex(1040))
print(calc_special(3,16))
#print(1012658227848*8)
#102040816326530612244897959183673469387755
#102040816326530620192914811671465122856965
#print(to_decimal(8,16))
#print(verify_parasite(21,8))

    