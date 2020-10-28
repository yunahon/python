#Binary Tree, Construct, Insert and Traversal

class Node:
    def __init__(self, value):

        self.left = None
        self.right = None
        self.value = value

# Insert Node
    def insert(self, value):

        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

# Insert All Node
    def insertAll(self, value):
        for i in value:
            if self.value:
                if i < self.value:
                    if self.left is None:
                        self.left = Node(i)
                    else:
                        self.left.insert(i)
                elif i > self.value:
                    if self.right is None:
                        self.right = Node(i)
                    else:
                        self.right.insert(i)
            else:
                self.value = i
# Delete Node
    def delete(self, root, key):
        if not root:
            return root
        
        if root.value > key:
            root.left = self.delete(root.left, key)
        elif root.value < key:
            root.right = self.delete(root.right, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            temp = root.right
            while temp.left:
                temp = temp.left
            root.right = self.delete(root.right, root.value)
        return root

# Inorder traversal
# Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.value)
            res = res + self.inorderTraversal(root.right)
        return res

# Preorder traversal
# Left -> Root -> Right
    def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.value)
            res = res + self.inorderTraversal(root.left)
            res = res + self.inorderTraversal(root.right)
        return res


# Postorder traversal
# Left -> Root -> Right
    def postorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res = res + self.inorderTraversal(root.right)
            res.append(root.value)
        return res

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.insertAll([])

#print(root.inorderTraversal(root))
#delval = int(input("enter delete: "))



#print(root.postorderTraversal(root))
#print(root.preorderTraversal(root))


def inorderTraversal(root):
    res = []
    if root:
        res = inorderTraversal(root.left)
        res.append(root.value)
        res = res + inorderTraversal(root.right)
    return res

print(inorderTraversal(root))
                                                                                  
def solve(root, depth = 0):
    if root == None:
        return depth
    return max(solve(root.left, depth + 1), solve(root.right, depth +1))

print(solve(root))