import string

alpha = string.ascii_uppercase+string.ascii_lowercase

def prepare_candidates(strings,shift):
    DONT_CHANGE = ".,?! "
    decrypted = [alpha[alpha.find(x)-shift].lower() if x not in DONT_CHANGE else ' ' for x in strings]
    return ''.join(decrypted).split()

def calculate_score(candidates,words):
    score = 0
    for candidate in candidates:
        if candidate in words:
            score+=1
    return score

def check_shifts(candidates, words,max_shift=25):
    table={x:0 for x in range(0,max_shift+1)}
    for shift in range(0,max_shift+1):
        table[shift]=calculate_score(prepare_candidates(candidates,shift),words)
    findings=sorted(zip(table.values(),table.keys()))[-1][1]
    return findings

def break_caesar(message):
    global WORDS
    return check_shifts(message,WORDS)