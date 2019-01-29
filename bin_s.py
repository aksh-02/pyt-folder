def bin_s(sarr,x):
    if not sarr:
        return False
    if sarr[len(sarr)//2]==x:
        return True
    elif sarr[len(sarr)//2]>x:
        return bin_s(sarr[:len(sarr)//2],x)
    elif sarr[len(sarr)//2]<x:
        return bin_s(sarr[len(sarr)//2+1:],x)
    

if __name__=='__main__':
    print(bin_s(list(map(int,input().split())),int(input())))
