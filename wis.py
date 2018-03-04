#Создание двух таблиц Вижинера
tablu = [[0 for i in range(0, 26)] for j in range(0, 26)]
tabll = [[0 for i in range(0, 26)] for j in range(0, 26)]
alphu = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphl = "abcdefghijklmnopqrstuvwxyz"
s1 = ""
s2 = ""
for i in range(26):
    s1 = alphu[i:]
    s2 = alphu[:i]
    s = s1 + s2
    for j in range(26):
        tablu[i][j] = s[j]
for i in range(26):
    s1 = alphl[i:]
    s2 = alphl[:i]
    s = s1 + s2
    for j in range(26):
        tabll[i][j] = s[j]

#Функция шифрования
def enc(inp, k):
    i = 0
    j = 0
    rez = ""
    while i < len(inp):
        if k[j] in alphu:
            b = alphu.index(k[j])
        else:
            b = alphl.index(k[j])
        if inp[i] in alphu:
            a = alphu.index(inp[i])
            rez += tablu[a][b]
        else:
            a = alphl.index(inp[i])
            rez += tabll[a][b]        
        i += 1
        j += 1
        if j == len(k):
            j = 0
    return rez
#Функция дешифровки
def dec(inp, k):
    i = 0
    j = 0
    rez = ""
    while i < len(inp):
        g = 0
        f = True
        if k[j] in alphu:
            b = tablu[g].index(k[j])
        elif k[j] in alphl:
            b = tabll[g].index(k[j])
        while g < 26 and f:
            if inp[i] in alphu:
                au = tablu[g].index(inp[i])
                if au == b:
                    rez += tablu[g][0]
                    f = False
            elif inp[i] in alphl:
                al = tabll[g].index(inp[i])
                if al == b:
                    rez += tabll[g][0]
                    f = False
            g += 1
        i += 1
        j += 1
        if j == len(k):
            j = 0
    return rez