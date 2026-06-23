class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)
    

def isSameTree(self, p, q):
    if not p and not q:
        return True
    
    if not p or not q or p.val != q.val:
        return False
    
    return (
        self.isSameTree(p.left, q.left) 
        and 
        self.isSameTree(p.right, q.right)
    )
    
