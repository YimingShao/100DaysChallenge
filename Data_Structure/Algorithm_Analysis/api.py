import  time
from functools import wraps


'''Three-Way Set Disjointness'''
def disjoint1(groupA, groupB, groupC):
    '''If each of the original sets has size n,
    then the worst-case running time of this method is O(n3).'''
    for a in groupA:
        for b in groupB:
            for c in groupC:
                if a == b and b == c:
                    return True
    return False

def disjoint2(groupA, groupB, groupC):
    '''the worst-case running time of this method is O(n2)'''
    for a in groupA:
        for b in groupB:
            if a == b:
                for c in groupC:
                    if a == c:
                        return True
    return False


