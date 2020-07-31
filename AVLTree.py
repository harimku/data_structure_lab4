from array import *
import numpy as np
from collections import Counter

# Create a tree node
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


# AVL Tree
class AVLTree:
    def __init__(self):
        self.root = None
        self.cur_balance_factor = None

    def getRoot(self):
        return self.root

    def getHeight(self, root):
        if root is None:
            return 0
        return root.height

    def getBalance(self, root):
        if root is None:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def checkBalance(self, root):
        balance_factor = self.getBalance(root)
        if(balance_factor > 1):
            return True
        elif(balance_factor < -1):
            return False
        else: # balance_factor = 0 meaning it is balanced 
            return None

    def checkHeight(self, root):
        largest_height = sorted([self.getHeight(root.left), self.getHeight(root.right)])[1]
        return (1 + largest_height)

    def insert_node(self, root, key):
        if root is None:
            return TreeNode(key)
        elif key >= root.key:
            root.right = self.insert_node(root.right, key)
        else:
            root.left = self.insert_node(root.left, key)
        root.height = self.checkHeight(root)
        # check for balance and deal with it accordingly
        balance = self.checkBalance(root)
        if balance is not None:
            if balance:
                if key >= root.left.key:
                    root.left = self.leftRotate(root.left)
                    return self.rightRotate(root)
                else:
                    return self.rightRotate(root)
            else:
                if key <= root.right.key:
                    root.right = self.rightRotate(root.right)
                    return self.leftRotate(root)
                else:
                    return self.leftRotate(root)
        return root

    def leftRotate(self, root):
        other = root.right
        temp = other.left
        other.left = root
        root.right = temp
        root.height = self.checkHeight(root)
        other.height = self.checkHeight(other)
        return other

    def rightRotate(self, root):
        other = root.left
        temp = other.right
        other.right = root
        root.left = temp
        root.height = self.checkHeight(root)
        other.height = self.checkHeight(other)
        return other

    # Horizontal tree output function (lab 3)
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
    # Level ordered numbers set (Given in lab 4 specification)
    print('------------- Comparison --------------')
    arr= [42, 25, 68, 1, 35, 63, 70, 59, 65, 79]
    avl = AVLTree()
    avl_root = None
    for i in arr:
        avl_root = avl.insert_node(avl_root, i)
    avl.printIterative(avl_root)
    print('')

    # Original number set
    print('--------------- Test 1 ----------------')
    arr = [42, 68, 35, 1, 70, 25, 79, 59, 63, 65]
    avl1 = AVLTree()
    avl1_root = None
    for i in arr:
        avl1_root = avl1.insert_node(avl1_root, i)
    avl1.printIterative(avl1_root)
    print('')

    # Re-ordered number set
    print('--------------- Test 2 ----------------')
    arr = [42, 68, 1, 25, 35, 70, 59, 63, 65, 79]
    avl2 = AVLTree()
    avl2_root = None
    for i in arr:
        avl2_root = avl2.insert_node(avl2_root, i)
    avl2.printIterative(avl2_root)
    print('')
    print('-------------- Finished ---------------')

if __name__ == '__main__':
    main()