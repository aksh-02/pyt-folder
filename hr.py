# first method

def minuteToWinIt(a, k):

    m=1
    for i in range(len(a)):
        c=1
        for j in range(i+1,len(a)):
            if a[j]-a[i]==(j-i)*k:
                c+=1
        if c>m:
            m=c
        if m>=len(a)-(i+1):
            return len(a)-m

    return len(a)-m




# second method
# i guess this is much faster

def minuteToWinIt(a, k):

    p=[]
    m=1
    for i in range(0,len(a)):
        if a[i] not in p:
            p.append(a[i])
            c=1
            for j in range(i+1,len(a)):
                if a[j]-a[i]==(j-i)*k:
                    p.append(a[j])
                    c+=1
            if c>m:
                m=c
            if m>=len(a)-(i+1):
                return len(a)-m
    
    return len(a)-m

