from array import *
import numpy as np
from collections import Counter

# tree node definition
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def get(self):
        return self.data
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    def setLeft(self, left):
        self.left = left
    def setRight(self, new_right):
        self.right = new_right
    def set(self,data):
        self.data = data
    node = property(get,set)
    left = property(getLeft,setLeft)
    right = property(getRight, setRight)


# Binary Tree 
class BinaryTree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def insert(self, data):
        pdata = TreeNode(data)
        if self.root is None:
            self.root = pdata
            return None

        runner = self.root
        while (runner):
            if (runner.node < data):
                if runner.right is None:
                    runner.right = pdata
                    return None
                else:
                    runner = runner.right
            elif (runner.node > data):
                if runner.left is None:
                    runner.left = pdata
                    return None
                else:
                    runner = runner.left
            else: # duplicate values -- how to handle?
                runner = pdata
                return None

    def search(self, data):
        runner = self.root
        while (runner):
            if (runner.node > data):
                if runner.left is None:
                    return 'Not Found'
                else:
                    runner = runner.left
            elif (runner.node < data):
                if runner.right is None:
                    return 'Not Found'
                else:
                    runner = runner.right
            else:
                return 'Value Found'
    
    def printIterative(self):
        root = self.root
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

        level_out = str(root.node)
        for level in levels:
            print(level_out + "|")
            next_out = ""
            for node in level:
                if(node == 0):
                    next_out += str("- - ")
                else:
                    if node.left:
                        next_out += str(node.left.node) +  " "
                    else:
                        next_out += "- "
                    if node.right:
                        next_out += str(node.right.node) + " "
                    else:
                        next_out += "- "
            level_out = next_out
        

def main():       
    # Automated Test 1 (testing with lab 3 example output)
    print('--------------- Test 1 ----------------')
    arr = [42, 68, 35, 1, 70, 25, 79, 59, 63, 65]
    bt = BinaryTree()
    for i in arr:
        bt.insert(i)
    
    # test the search operation
    print('1)Search for value in the tree:')
    search_val = 42
    print('Search for: ' + str(search_val))
    result = bt.search(search_val)
    print(result)

    print('')
    print('2)Search for value not in the tree:')
    search_val = 777
    print('Search for: ' + str(search_val))
    result = bt.search(search_val)
    print(result)

    # print the Binary tree horizontally 
    print('')
    print('3)Printing the tree: ')
    bt.printIterative()
    
    
    # Automated Test 2 (with numbers.txt file)
    print('')
    print('---------------- Test 2 -----------------')
    print('Printing the tree: ')
    print('')
    tree = BinaryTree()
    numbers = np.loadtxt(fname = "./Numbers.txt")
    for i in numbers:
        tree.insert(int(i))
    tree.printIterative()
    print('')
    

if __name__ == '__main__':
    main()