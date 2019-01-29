#!/bin/python3

class Node:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def printlist(node):
    while node:
        print(node.data)

        node = node.next

      

def insert(head, data):
    if head:
        cur=head
        while cur.next!=None:
            cur=cur.next
        cur.next=Node(data)
    else:
        head=Node(data)
       
    
    return head

def reverse(head):
    if head.next==None:
        return head

    a=reverse(head.next)
    cur=a
    while cur.next!=None:
        cur=cur.next
    cur.next=head

    return a

    
if __name__ == '__main__':

    llist = SinglyLinkedList()

    for i in range(int(input())):

        llist_head = insert(llist.head,int(input()))
        llist.head = llist_head

    printlist(llist.head)
    
    k=reverse(llist.head)
    printlist(llist.head)
