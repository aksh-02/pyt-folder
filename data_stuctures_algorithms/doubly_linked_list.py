class node:
  def __init__(self,data=None):
    self.data=data
    self.prev=None
    self.next=None

class doubly_linked_list:
  def __init__(self):
    self.head=node()

  def append(self,data):
    new_node=node(data)
    cur=self.head
    while cur.next!=None:
      cur=cur.next
    cur.next=new_node
    new_node.prev=cur

  def appendleft(self,data):
    new_node=node(data)
    cur=self.head
    new_node.next=cur.next
    new_node.prev=cur
    cur=cur.next
    cur.prev=new_node
    self.head.next=new_node

  def display(self):
    li=[]
    cur=self.head
    while cur.next!=None:
      cur=cur.next
      li.append(cur.data)
    print(li)

  def length(self):
    total=0
    cur=self.head
    while cur.next!=None:
      cur=cur.next
      total+=1
    return total

  def get(self,index):
    if index>self.length():
      print('index out of range')
    else:
      ind=0
      cur=self.head
      while ind!=index:
        ind+=1
        cur=cur.next
      print(cur.data)
      return None

  def erase(self,index):
    if index>self.length():
      print('index out of range')
    else:
      ind=0
      cur=self.head
      while ind!=index-1:
        ind+=1
        cur=cur.next
      a=cur.next
      cur.next=a.next  


if __name__=="__main__":
  a=doubly_linked_list()
  a.append(45)
  a.append(90)
  a.append(135)
  a.append(180)
  a.display()
  print(a.length())
  a.get(2)
  a.erase(2)
  a.display()
  a.get(2)
  a.get(1)
  a.appendleft(200)
  a.get(1)
  a.display()
