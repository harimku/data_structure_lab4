from array import *
import numpy as np
from collections import Counter

# Create tree node
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.parent = None

# Create Binary Tree
class AVLTree:
    def __init__(self):
        self.root = None
        self.val = None

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
        return self.getBalance(root)

    def checkHeight(self, root):
        largest_height = sorted([self.getHeight(root.left), self.getHeight(root.right)])[1]
        return (1 + largest_height)

    # This insert function simply inserts new nodes
    def insert_node(self, root, key):
        if root is None:
            return TreeNode(key)
        elif key >= root.key:
            root.right = self.insert_node(root.right, key)
            root.right.parent = root
        else:
            root.left = self.insert_node(root.left, key)
            root.left.parent = root
        root.height = self.checkHeight(root)
        return root

# Tree Balancing Algorithm
    def rebalance(self, root):
        if root is None:
            print('Root is none')
            return
        else:
            stack = [root]
            while stack:
                initial_root = stack.pop()
                initial_root_parent = initial_root.parent
                direction = ""
                if initial_root_parent:
                    if initial_root_parent.left is not None and initial_root_parent.left == initial_root:
                        direction = "left"
                    elif initial_root_parent.right is not None:
                        direction = "right"
                new_root = self.balance(initial_root)
                if new_root is not None:
                    if direction == "left":
                        initial_root_parent.left = new_root
                    elif direction == "right":
                        initial_root_parent.right = new_root
                if initial_root.left:
                    stack.append(initial_root.left)
                if initial_root.right:
                    stack.append(initial_root.right)

    def balance(self, root):
        balance = self.checkBalance(root)
        new_root = None
        if balance > 1:  # when left-heavy
            if self.getBalance(root.left) >= 0:
                new_root = self.rotate_right(root)
            else:
                new_root = self.rotate_left_right(root)
        elif balance < -1:
            # when right-heavy
            if self.getBalance(root.right) <= 0:
                new_root = self.rotate_left(root)
            else:
                new_root = self.rotate_right_left(root)
        if new_root is not None:
            self.val = 1
            temp_parent = root.parent
            new_root.parent = temp_parent
            root.parent = new_root
        return new_root

    def rotate_left(self, root):
        right_temp = root.right
        root.right = right_temp.left
        right_temp.left = root
        root.height = self.checkHeight(root)
        right_temp.height = self.checkHeight(right_temp)
        return right_temp

    def rotate_right(self, root):
        left_temp = root.left
        root.left = left_temp.right
        left_temp.right = root
        root.height = self.checkHeight(root)
        left_temp.height = self.checkHeight(left_temp)
        return left_temp

    def rotate_left_right(self, root):
        root.left = self.rotate_left(root.left)
        return self.rotate_right(root)

    def rotate_right_left(self, root):
        root.right = self.rotate_right(root.right)
        return self.rotate_left(root)

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
            print(level_out + '|')
            next_out = ''
            for node in level:
                if(node == 0):
                    next_out += str('- - ')
                else:
                    if node.left:
                        next_out += str(node.left.key) +  ' '
                    else:
                        next_out += '- '
                    if node.right:
                        next_out += str(node.right.key) + ' '
                    else:
                        next_out += '- '
            level_out = next_out


def main():
    ## Automated Test
    # Level ordered numbers set (Given in lab 4 specification)
    print('------------- Comparison --------------')
    arr = [42, 25, 68, 1, 35, 63, 70, 59, 65, 79]
    avl = AVLTree()
    avl_root = None
    for i in arr:
        avl_root = avl.insert_node(avl_root, i)
    avl.printIterative(avl_root)
    print('')
    print('This tree is level ordered and balanced.')
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
    avl1.rebalance(avl1_root)
    if avl1.val is None:
        print('Tree is already balanced')
    else:
        print('This tree is unbalanced')
        print('Balancing this tree...')
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
    avl2.rebalance(avl2_root)
    if avl2.val is None:
        print('Tree is already balanced')
    else:
        print('This tree is unbalanced')
        print('Balancing this tree...')
        avl2.printIterative(avl2_root)
    print('')
    print('-------------- Finished ---------------')


if __name__ == '__main__':
    main()