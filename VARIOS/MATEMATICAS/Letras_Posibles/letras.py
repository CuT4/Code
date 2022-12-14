#NO LO HE HECHO YO

string = "abcde"
contador=0
def combinations(head, tail=''):
    global contador
    if len(head) == 0:
        print(tail)
    else:
        for i in range(len(head)):
            combinations(head[:i] + head[i+1:], tail + head[i])
combinations(string)