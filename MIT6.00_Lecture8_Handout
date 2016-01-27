#O(b)
def exp(a,b):
    answer = 1
    for i in range(b):
        answer *=a
    return answer

#O(b)
def exp2(a,b):
    if b == 1:
        return a
    else:
        return a*exp2(a,b-1)

#O(log b)
def exp3(a,b):
    if b == 1:
        return a
    elif (2%b)*2 == b:
        return exp3(a*a, b/2)
    else:
        return a*exp3(a, b-1)

#O(m*n)
def g(n,m):
    x = 0
    for i in range(n):
        for j in range(m):
            x += 1
    return x

#O(2^n)
def Towers(size, fromStack, toStack, spareStack):
    if size == 1:
        print ('Move disk from',fromStack,'to',toStack)
    else:
        Towers(size-1, fromStack, spareStack, toStack)
        Towers(1, fromStack, toStack, spareStack)
        Towers(size-1, spareStack, toStack, fromStack)

def search(s, e):
    answer = None
    i = 0
    numCompares = 0
    while i < len(s) and answer == None:
        numCompares += 1
        if e == s[i]:
            answer = True
        elif e < s[i]:
            answer = False
        i += 1
    print(answer, numCompares)

def besearch(s, e, first, last):
    print(first, last)
    if (last - first) < 2: return s[first] == e or s[last] == e
    mid = int(first + (last - first)/2)
    if s[mid] == e: return True
    if s[mid] > e: return besearch(s,e,first, mid-1)
    return besearch(s,e,mid+1, last)

def search1(s,e):
    print (besearch(s,e,0, len(s)-1))
    print ('Search Complete')

def testSearch():
    s = range(0,1000000)
    input('basic, -1')
    print (search(s,-1))
    input('binary, -1')
    print (search1(s,-1))
    input('basic, end')
    print (search(s,1000000))
    input('binary, end')
    print (search1(s,1000000))
    s = range(0, 10000000)
    input('basic, partway')
    print (search(s,1000000))
    input('basic, larger end')
    print (search(s,1000000))
    input('binary, partway')
    print (search1(s,1000000))
    input('binary, larger end')
    print (search1(s,1000000))
    
