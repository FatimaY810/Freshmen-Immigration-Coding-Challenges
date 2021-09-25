## reverse string (destructively) function ##

def reverseString(L):
    L.reverse()
    print (L) ##destructive function returns none##


## reverse string (non-destructively) function ##

def reverseStringNon(L):
    L = L[::-1]
    return L


