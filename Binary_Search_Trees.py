class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root,new_val)
        "$$2 'BST' object has no attribute 'intert_helper'"

    def search(self, find_val):
        return self.search_helper(self.root,find_val)
        "$$3 global name 'search_helper' is not defined"
        
    def insert_helper(self,current,new_val):
        if current:
            if current.value<new_val:
                if current.right:
                    return self.insert_helper(current.right,new-val)
                else:
                    current.right = Node(new_val)
            else:
                if current.left:
                    return self.insert_helper(current.left,new_val)
                else:
                    current.left = Node(new_val)
            
        
    def search_helper(self,current,new_val):
        if current:
            if current.value== new_val:
                "$$1 current.value= new_val missing =="
                return True
            elif current.value>new_val:
                return self.search_helper(current.right,new_val)
            else:
                return self.search_helper(current.left,new_val)
                
        return False
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
