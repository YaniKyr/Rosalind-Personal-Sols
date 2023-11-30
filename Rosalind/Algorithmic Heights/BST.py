class Node:
    def __init__(self,point,data=None,):
        self.data = data
        self.point =point
        self.right = None
        self.left = None

class Tree:
    def __init__(self):
        self.root =None
    def insert(self,point,item):

        if self.root is None:
            self.root = Node(point,item)
        else:
            self.insertIntoT(self.root,point,item)
    def insertIntoT(self,cur_node,point,item):
        if item<cur_node.data:
            if cur_node.left is None:
                cur_node.left= Node(point,item)
                
            else:
                self.insertIntoT(cur_node.left,point,item)

        elif item>cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(point,item)

            else:
                self.insertIntoT(cur_node.right,point,item)

    def Search_tree(self,item):
            if self.root is not None:
                print("Inorder")
                return self._Search_tree(self.root,item)
                

    def _Search_tree(self,cur_node,item):
        if cur_node is not None:
            self._Search_tree(cur_node.left,item)

            if cur_node.data ==item:
                return False
            self._Search_tree(cur_node.right,item)

    def Print_tree(self):
            if self.root is not None:
                print("Inorder")
                self._Print_tree(self.root)
                

    def _Print_tree(self,cur_node):
        if cur_node is not None:
            self._Print_tree(cur_node.left)
            print(cur_node.data)
            self._Print_tree(cur_node.right)