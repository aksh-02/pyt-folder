# Avl Trees

class node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
        self.height=1

class avl_tree:
    def __init__(self):
        self.root=None

    def insert(self,root,val):
        if root==None:
            return node(val)
        elif val<root.data:
            root.left=self.insert(root.left,val)
        elif val>root.data:
            root.right=self.insert(root.right,val)

        root.height=1+max(self.get_height(root.left),self.get_height(root.right))
        # getting the balance factor
        balance=self.get_balance(root)

        # case 1- left left
        if balance>1 and val<root.left.data:
            return self.right_rotate(root)

        # case 2- right right
        if balance<-1 and val>root.right.data:
            return self.left_rotate(root)

        # case 3- left right
        if balance>1 and val>root.left.data:
            root.left=self.left_rotate(root.left)
            return self.right_rotate(root)

        # case 4- right left
        if balance<-1 and val<root.right.data:
            root.right=self.right_rotate(root.right)
            return self.left_rotate(root)

        return root    

    def left_rotate(self,z):
        # z is the node at which the rotation is to be done
        y=z.right
        t=y.left

        # perform rotation
        y.left=z
        z.right=t

        # update the heights
        z.height=1+max(self.get_height(z.left),self.get_height(z.right))
        y.height=1+max(self.get_height(y.left),self.get_height(y.right))

        return y
        
    def right_rotate(self,z):
        # z is the node at which the rotation is to be done
        y=z.left
        t=y.right

        # perform rotation
        y.right=z
        z.left=t

        # update the heights
        z.height=1+max(self.get_height(z.left),self.get_height(z.right))
        y.height=1+max(self.get_height(y.left),self.get_height(y.right))

        return y

    def get_height(self,root):
        if not root:
            return 0
        return root.height

    def get_balance(self,root):
        if not root:
            return 0
        return self.get_height(root.left)-self.get_height(root.right)

    def inorder(self,root):  # for printing purposes
        if root==None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)         


if __name__=="__main__":
    my_tree=avl_tree()
    my_tree.root=my_tree.insert(my_tree.root,10)
    print('data',my_tree.root.data)
    my_tree.root=my_tree.insert(my_tree.root,20)
    print('data',my_tree.root.data)
    my_tree.root=my_tree.insert(my_tree.root,30)
    print('data',my_tree.root.data)
    my_tree.root=my_tree.insert(my_tree.root,40)
    print('data',my_tree.root.data)
    my_tree.root=my_tree.insert(my_tree.root,50)
    print('data',my_tree.root.data)
    my_tree.root=my_tree.insert(my_tree.root,60)
    print('data',my_tree.root.data)
    my_tree.root=my_tree.insert(my_tree.root,70)
    print('data',my_tree.root.data)
    my_tree.root=my_tree.insert(my_tree.root,80)
    print('data',my_tree.root.data)
    my_tree.root=my_tree.insert(my_tree.root,90)
    print('data',my_tree.root.data)
    my_tree.inorder(my_tree.root)
    print(my_tree.get_height(my_tree.root))
