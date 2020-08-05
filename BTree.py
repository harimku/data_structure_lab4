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


# Creating and Balancing a Binary Tree
class BTree:
    def __init__(self):
        self.root = None
        self.cur_balance_factor = None

    def getRoot(self):
        return self.root

    def getHeight(self, root):
        if root is None:
            return 0
        return root.height

    def checkHeight(self, root): 
        if root is None: 
            return 0
        else:
            return (1 + max(self.checkHeight(root.left), self.checkHeight(root.right)))

    def checkBalance(self, root): 
        if root is None: 
            return True

        lh = self.checkHeight(root.left) 
        rh = self.checkHeight(root.right) 

        if (abs(lh - rh) <= 1) and self.checkBalance( 
        root.left) is True and self.checkBalance(root.right) is True: 
            return True
        return False

    def insert_node(self, root, key):
        if root is None:
            return TreeNode(key)
        elif key >= root.key:
            root.right = self.insert_node(root.right, key)
        else:
            root.left = self.insert_node(root.left, key)
        root.height = self.checkHeight(root)
        return root

    def storeNodes(self, nodes, root): 
        if root is None: 
            return None
        else:
            self.storeNodes(nodes, root.left) 
            nodes.append(root) 
            self.storeNodes(nodes, root.right) 
            return None

    def reTree(self, nodes, start, end): 
        if (end < start): 
            return None
        else:
            node = nodes[(start + end)//2] 
            node.left=self.reTree(nodes, start, ((start+end)//2)-1) 
            node.right=self.reTree(nodes, ((start+end)//2)+1, end) 
            return node 

    # Balance an unbalanced Binary Tree
    def balanceTree(self, root): 
        nodes=[] 
        self.storeNodes(nodes, root) 
        return self.reTree(nodes, 0, len(nodes)-1) 

    # Horizontal tree output function (Lab 3)
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
    avl = BTree()
    avl_root = None
    for i in arr:
        avl_root = avl.insert_node(avl_root, i)
    avl.printIterative(avl_root)
    if avl.checkBalance(avl_root):
        print('This tree is balanced')
        print('Does not require rebalancing')
    else:
        print('This tree is unbalanced')
        print('Performing Rebalancing...')
        avl_root = avl.balanceTree(avl_root)
        avl.printIterative(avl_root)
        if avl.checkBalance(avl_root):
            print('This tree is now balanced')
        else:
            print('This tree is still unbalanced')
    print('')

    # Original number set
    print('--------------- Test 1 ----------------')
    arr = [42, 68, 35, 1, 70, 25, 79, 59, 63, 65]
    avl1 = BTree()
    avl1_root = None
    for i in arr:
        avl1_root = avl1.insert_node(avl1_root, i)
    avl1.printIterative(avl1_root)
    if avl1.checkBalance(avl1_root):
        print('This tree is balanced')
        print('Does not require rebalancing')
    else:
        print('This tree is unbalanced')
        print('Performing Rebalancing...')
        avl1_root = avl1.balanceTree(avl1_root)
        avl1.printIterative(avl1_root)
        if avl1.checkBalance(avl1_root):
            print('This tree is now balanced')
        else:
            print('This tree is still unbalanced')
    print('')

    # Re-ordered number set
    print('--------------- Test 2 ----------------')
    arr = [42, 68, 1, 25, 35, 70, 59, 63, 65, 79]
    #arr = [1, 25, 35, 42, 59, 63, 65, 68, 70, 79 ]
    avl2 = BTree()
    avl2_root = None
    for i in arr:
        avl2_root = avl2.insert_node(avl2_root, i)
    avl2.printIterative(avl2_root)
    if avl2.checkBalance(avl2_root):
        print('This tree is balanced')
        print('Does not require rebalancing')
    else:
        print('This tree is unbalanced')
        print('Performing Rebalancing...')
        avl2_root = avl2.balanceTree(avl2_root)
        avl2.printIterative(avl2_root)
        if avl2.checkBalance(avl2_root):
            print('This tree is now balanced')
        else:
            print('This tree is still unbalanced')
    print('')
    print('-------------- Finished ---------------')

if __name__ == '__main__':
    main() 