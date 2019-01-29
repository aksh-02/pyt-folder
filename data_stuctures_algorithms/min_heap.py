# min_heap
# a heap is an implementation of a priority queue
# it is visualized as a nearly complete binary tree
# in a heap with index starting with 1, if i is the index of the parent then the index of the children if any would be 2*i and 2*i+1
# similarly if index of the children is i, index of the parent would be i//2

class heap:
    def __init__(self):
        self.heap_list=[0]
        self.cur_size=0

# the below function can make a heap of an array without having to insert its elements one by one 
    
    def build_heap(self,arr):
        self.cur_size=len(arr)
        self.heap_list=[0]+arr
        i=len(arr)//2
        while i>0:
            self.move_down(i)
            i-=1
    
    def insert(self,k):
        self.heap_list.append(k)
        self.cur_size+=1
        self.set_new(self.cur_size)

# the below function is used to remake the heap everytime we insert a new element
    def set_new(self,i):
        while i//2>0:
           if self.heap_list[i]<self.heap_list[i//2]:
               self.heap_list[i],self.heap_list[i//2]=self.heap_list[i//2],self.heap_list[i]
               i=i//2
           else:
               break

# the below function is used after everytime we extract minimum of heap
    def move_down(self,i):
        while i*2<=self.cur_size:
            mc=self.min_child(i)d
            if self.heap_list[i]>self.heap_list[mc]:
                self.heap_list[i],self.heap_list[mc]=self.heap_list[mc],self.heap_list[i]
                i=mc
            else:
                break

    def min_child(self,i):
        if i*2+1>self.cur_size:
           return i*2
        else:
            if self.heap_list[i*2]<self.heap_list[i*2+1]:
                return i*2
            else:
                return i*2+1

# below is a function which gives us minimum of heap everythime,hence is used for heap sort
    def ext_min(self):
        if self.cur_size==0:
            return 'heap empty'
        a=self.heap_list[1]
        self.heap_list[1]=self.heap_list[self.cur_size]
        self.heap_list.pop()
        self.cur_size-=1
        self.move_down(1) # to make a min heap again because heap_list[1] is not the minimum of heap
        return a

if __name__=='__main__':
    h1=heap()
    h1.insert(34)
    h1.insert(26)
    h1.insert(9)
    h1.insert(45)
    h1.insert(145)
    h1.insert(-1)
    h1.insert(0)
    h1.insert(78)
    h1.insert(45)
    h1.insert(23)
    h1.insert(13)
    print([h1.ext_min() for i in range(h1.cur_size)]) # this gives us a sorted list

# we can also make heap of a given list without inserting its element one by one

    h2=heap()
    h2.build_heap(list(map(int,input().split())))
    print([h2.ext_min() for i in range(h2.cur_size)])

