

france = [1,2,3,4,5,7,8,9,11,12,13,14,15]
# paris = [2,6,10,12,15]
# lear = [12,15]
paris = [1, 4, 12, 13]
lear = [2, 3, 4, 13]

def lastValue(list, index):
    if index == (len(list) - 1):
        return True
    else: return False

def union(p1, p2): #or   
    answer = []
    i = 0
    j = 0
    while p1[-1] != float('inf') or p2[-1] != float('inf'):
        if p1[i] == p2[j]:
            answer.append(p1[i]) 

            if lastValue(p1, i) and lastValue (p2, j):
                p1[i] = float('inf')
                p2[j] = float('inf')
            elif lastValue(p1, i):
                p1[i] = float('inf')
                j += 1
            elif lastValue(p2, j):
                p2[j] = float('inf')
                i += 1
            else:
                i += 1
                j += 1
        elif p1[i] < p2[j]:
            answer.append(p1[i]) 
            if lastValue(p1, i): 
                p1[i] = float('inf')
            else: i += 1
        else:
            answer.append(p2[j]) 
            if lastValue(p2, j): 
                p2[j] = float('inf')
            else: j += 1
    return answer

def intersect(p1, p2): #and
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



def complement(): #not
    answer = []
    return answer

print(union(lear, paris))