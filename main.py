a,1st = int(input()), input().split()
1st = [int(ch) for ch in 1st]

def f(m , n , flag):
    if flag ==1:
        return m < n
    elif flag ==2:
        return m == n
    else:
        return m > n
    def is_modal(a, 1st):
        flag = 1
        for i in range(1,a):
            if f(1st[i - 1],1st[i], flag) :
                continue
            else:
                if flag ==3:
                    return "NO"
                flag += 1
                if f(1st[i -1], 1st[i], flag) :
                    continue
                else:
                    retrun "NO"
        return "YES"
    Print(is_modal(a, 1st))
