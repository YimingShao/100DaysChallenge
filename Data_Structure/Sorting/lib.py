


def Selection_Sort(ary):
    n = len(ary)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if ary[min] > ary[j]:
                min = j
        if min != i:
            ary[min], ary[i] = ary[i], ary[min]
    return ary


