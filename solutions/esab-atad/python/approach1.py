import sys

def getBit(index):
    print(index)
    sys.stdout.flush()
    return input() 

def getPair(data, left, b):
    right = b - 1 - left
    data[left]['val'] = getBit(left+1)
    data[right]['val'] = getBit(right+1)
    
    data[left]['sym'] = data[left]['val'] == data[right]['val']
    data[right]['sym'] = data[left]['sym']

def getFluctuationType(data):
    symIndex = next((i for i,v in enumerate(data) if v['sym'] == True), None)
    asymIndex = next((i for i,v in enumerate(data) if v['sym'] == False), None)
    symB = asymB = dSym = dAsym = None

    if symIndex is not None:
        symB = getBit(symIndex+1)
        dSym = data[symIndex]['val'] != symB
    else:
        getBit(1)
    if asymIndex is not None:
        asymB = getBit(asymIndex+1)
        dAsym = data[asymIndex]['val'] != asymB
    else:
        getBit(1)

    if (symB is not None) and (asymB is not None):
        if dSym and dAsym:
            return "C"
        elif (not dSym) and dAsym:
            return "R"
        elif dSym and (not dAsym):
            return "CR"
        elif (not dSym) and (not dAsym):
            return None
    elif (symB is not None) and (asymB is None):
        if dSym:
            return "C"
        else:
            return None
    elif (symB is None) and (asymB is not None):
        if dAsym:
            return "C"
        else:
            return None

def complement(data):
    for d in data:
        if d['val'] == '0':
            d['val'] = '1'
        elif d['val'] == '1':
            d['val'] = '0'

def update(data, fluctuationType):
    if fluctuationType == "C":
        complement(data)
    elif fluctuationType == "R":
        data.reverse()
    elif fluctuationType == "CR":
        complement(data)
        data.reverse()

t, b = (int(s) for s in input().split(' '))
q = 0

for testCase in range(1, t + 1):
    data = [ {'val': None, 'sym': None } for _ in range(b)]
    for i in range(0, int(b/2)):
        if q > 0 and q%10 == 0:
            update(data, getFluctuationType(data))
            q += 2
        getPair(data, i, b)
        q += 2
    r = ""
    for dict in data:
        r += dict['val']
    print(r)
    sys.stdout.flush()
    ans = input()
    q = 0
    if ans != 'Y':
        break