class BTNode:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
class BT:
    def __init__(self, root = None):
        self.root = root
    
    def inorder(self, root):
	    if root is None:
	        return
	    self.inorder(root.left)
	    print root.data
	    self.inorder(root.right)
        
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print root.data
    inorder(root.right)
        
node1 = BTNode(6);node2 = BTNode(9);node3 = BTNode(2);
node4 = BTNode(30)
node5 = BTNode(35)

node1.left = node2; node1.right = node3
node3.left = node4
node4.right = node5

bt = BT(node1)
bt.inorder(node1)
