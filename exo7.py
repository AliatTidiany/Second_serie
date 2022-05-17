##Premiere methode


def som(i,j):
    n=(j-i)+1
    s=(n*(j+i))/2
##Deuxiéme méthode while
    s1=0
    y=i
    while (y<j+1):
        s1=s1+y
        y=y+1
##Troisiéme méthode
    s2=0
    for x in range (i,j+1):
        s2=s2+x
    return s, s1, s2
Result=som(2,4)
print(Result)


