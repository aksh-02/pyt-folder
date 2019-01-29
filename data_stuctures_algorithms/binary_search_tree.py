class node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None



class binary_search_tree:    
    def __init__(self):
        self.root=None

    def append(self,value):
        if self.root==None:
            self.root=node(value)
        else:
            cur=self.root
            while True:
                if value<cur.data:
                    if cur.left:
                        cur=cur.left
                    else:
                        cur.left=node(value)
                        break
                elif value>cur.data:
                    if cur.right:
                        cur=cur.right
                    else:
                        cur.right=node(value)
                        break
                else:
                    break

    def append2(self,value):  # a different method to append elements in the tree
        self._append2(self.root,value)

    def _append2(self,r,value):    # this append function works recursively when called by the above append2 function
        if r==None:
            r=node(value)
        elif value<r.data:
            r.left=self._append2(r.left,value)
        elif value>r.data:
            r.right=self._append2(r.right,value)
        return r     

    def print_tree(self):  # inorder traversal
        if self.root is not None:
            self._print_tree(self.root) 
        
    def _print_tree(self,cur):   # this is a private function used because we needed to set cur=self.root as a default argument
        if cur is None:
            return
        self._print_tree(cur.left)
        print(cur.data)
        self._print_tree(cur.right)


if __name__=='__main__':
    tree=binary_search_tree()
    tree.print_tree()
    tree.append(10)
    tree.append2(4)
    tree.append(34)
    tree.append(56)
    tree.append(2)
    tree.append(33)
    tree.append(0)
    tree.append(23)
    tree.print_tree()
