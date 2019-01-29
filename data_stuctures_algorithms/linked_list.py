class node:
  def __init__(self,data=None):
    self.data=data
    self.next=None

class linked_list:
  def __init__(self):
    self.head=node()

  def append(self,data):
    new_node=node(data)
    cur=self.head
    while cur.next!=None:
      cur=cur.next
    cur.next=new_node

  def display(self):
    cur=self.head
    li=[]
    while cur.next!=None:
      cur=cur.next
      li.append(cur.data)
    print(li)

  def length(self):
    total=0
    cur=self.head
    while cur.next!=None:
      total+=1
      cur=cur.next
    return total

  def get(self,index):
    if index>self.length():
      print('index out of range')
      return None
    else:
      ind=0
      cur=self.head
      while ind!=index:
        cur=cur.next
        ind+=1
      print(cur.data)
      return None

  def erase(self,index):
    if index>self.length():
      print('given index out of range')
    else:
      ind=0
      cur=self.head
      while ind!=index-1:
        cur=cur.next
        ind+=1
      a=cur.next
      cur.next=a.next    
    
if __name__=="__main__":
  a=linked_list()
  a.append(40)
  a.append(33)
  a.append(98)
  a.append(100)
  print(a.length())
  a.get(1)
  a.get(3)
  a.get(4)
  a.get(0)
  a.display()
  a.erase(2)
  a.display()
  a.get(2)
