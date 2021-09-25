## two sum ##

def twoSum(L, integer):
    EmpList = []
    for i in range(len(L)):
        number = L[i]
        for j in range (0, i):
            if number + L[j] == integer:
                EmpList.append (L.index(number))
                EmpList.append (j)
                return EmpList
        for j in range (i+1, len(L)):
            if number + L[j] == integer:
                EmpList.append (L.index(number))
                EmpList.append (j)
                return EmpList
    else:
        return None


