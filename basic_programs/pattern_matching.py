ms=input('enter the main string : ')
ps=input('enter the pattern : ')
count=0
for i in range(len(ms)):
    k=i
    j=0
    while j<len(ps):
        if k==len(ms):
            break
        elif ms[k]==ps[j]:
            k+=1
            j+=1
        else:
            break

        if j==len(ps):
            count+=1
            break
        

print(count)
