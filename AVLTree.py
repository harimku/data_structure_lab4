from array import *
import numpy as np
from collections import Counter
import sys

# Create a tree node
class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


# AVL Tree
class AVLTree(object):
    def insert_node(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def printIterative(self, root):
        levels = []
        curr_level = []
        next_level = []
        curr_level.append(root)
        end_flag = True
        while(end_flag):
            levels.append(curr_level)
            for node in curr_level:
                if(node != 0):
                    if(node.left):
                        next_level.append(node.left)
                    else:
                        next_level.append(0)
                    if(node.right):
                        next_level.append(node.right)
                    else:
                        next_level.append(0)
                else:
                    next_level.append(0)
                    next_level.append(0)
            curr_level = []
            for node in next_level:
                curr_level.append(node)
            next_level = []
            zero_counts = dict(Counter(curr_level)).get(0)
            if(zero_counts is not None and len(curr_level) == zero_counts):
                end_flag = False

        level_out = str(root.key)
        for level in levels:
            print(level_out + "|")
            next_out = ""
            for node in level:
                if(node == 0):
                    next_out += str("- - ")
                else:
                    if node.left:
                        next_out += str(node.left.key) +  " "
                    else:
                        next_out += "- "
                    if node.right:
                        next_out += str(node.right.key) + " "
                    else:
                        next_out += "- "
            level_out = next_out

        

def main():       
    ## Automated Test 
    # Level ordered numbers set
    print('------------- Comparison --------------')
    arr= [42, 25, 68, 1, 35, 63, 70, 59, 65, 79]
    avl3 = AVLTree()
    avl3_root = None
    for i in arr:
        avl3_root = avl3.insert_node(avl3_root, i)
    avl3.printIterative(avl3_root)
    
    # Original number set
    print('--------------- Test 1 ----------------')
    arr = [42, 68, 35, 1, 70, 25, 79, 59, 63, 65]
    avl1 = AVLTree()
    avl1_root = None
    for i in arr:
        avl1_root = avl1.insert_node(avl1_root, i)
    avl1.printIterative(avl1_root)
    
    # Re-ordered number set
    print('--------------- Test 2 ----------------')
    arr = [42, 68, 35, 1, 25, 63, 70, 59, 65, 79]
    avl2 = AVLTree()
    avl2_root = None
    for i in arr:
        avl2_root = avl2.insert_node(avl2_root, i)
    avl2.printIterative(avl2_root)
    print('')
    

if __name__ == '__main__':
    main()