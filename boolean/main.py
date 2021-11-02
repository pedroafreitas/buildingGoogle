"""
Pedro Arthur Freitas Dias
Desenvolido em Python 3.9
"""

france = [1,2,3,4,5,7,8,9,11,12,13,14,15]
paris = [2,6,10,12,15]
lear = [12,15]


def lastValue(list, index):
    if index == (len(list) - 1):
        return True
    else: return False

def removeDuplicates(p1):
    p1 = list(dict.fromkeys(p1))
    return p1

def difference(target,subtract): 
    answer = []
    for i in range(len(target)):
        if target[i] not in subtract:
            answer.append(target[i])
    return answer

def union(p1, p2):    
    answer = p1 + p2
    answer.sort()
    answer = removeDuplicates(answer)
    return answer

def intersect(p1, p2): 
    answer = []
    i = 0
    j = 0
    while i < len(p1) and j < len(p2):
        if p1[i] == p2[j]:
            answer.append(p1[i]) 
            i += 1
            j += 1
        elif p1[i] < p2[j]:
            i += 1
        else:
            j += 1
    return answer



parisAndNotFrance = difference(paris,france)
print("PARIS and not FRANCE: " + str(parisAndNotFrance))

orLear = union(parisAndNotFrance, lear)
print("(PARIS and not FRANCE) or LEAR: " + str(orLear))
