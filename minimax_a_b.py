import sys
import ast


class Node:
    def __init__(self, name, value=None, parent=None):
        self.Name = name
        self.value = value
        self.parent = parent
        self.children = []

    def addChildNode(self, childNode):
        self.children.append(childNode)

    def setName(self, name):
        self.Name = name

    def setValue(self, value):
        self.value = value

    def getName(self):
        return self.Name

    def getValue(self):
        return self.value

    def getChildren(self):
        return self.children


class Tree:
    def __init__(self, tree):
        self.root = None
        self.buildTree(tree)

    def buildTree(self, tree):
        self.root = Node(tree[0])
        self.subTree(tree, self.root)

    def subTree(self, subtree, parent):
        if isinstance(subtree, tuple):
            return
        else:
            for i in subtree[1:]:
                if isinstance(i, tuple):
                    parent.addChildNode(Node(i[0], i[1]))
                else:
                    temp = Node(i[0])
                    parent.addChildNode(temp)
                    self.subTree(i, temp)


class miniMax:
    def __init__(self, Tree):
        self.Tree = Tree
        self.root = Tree.root

    def getNextNodes(self, node):
        if type(node) is not tuple:
            return node.children

    def minimax(self, node):
        maximum_value = self.maxValue(node)
        nextNodes = self.getNextNodes(node)
        next_move = None
        for child in nextNodes:
            if child.value == maximum_value:
                next_move = child
                break
        print("utility:", maximum_value)
        print("move:", next_move.getName())
        return next_move

    def maxValue(self, node):
        print("node:", node.Name)
        if node.value != None:
            print(node, "leaf")
            return node.value
        maxValue = -9999999
        if node is not None:
            nextNodes = node.children
            for Nodes in nextNodes:
                maxValue = max(maxValue, self.minValue(Nodes))
            node.value = maxValue
            return maxValue

    def minValue(self, node):
        print("node:", node.Name)
        if node.value != None:
            return node.value
        minValue = 9999999
        if node is not None:
            nextNodes = node.children
            for Nodes in nextNodes:
                minValue = min(minValue, self.maxValue(Nodes))
            node.value = minValue
            return minValue


class alphaBeta:
    def __init__(self, Tree):
        self.Tree = Tree
        self.root = Tree.root

    def getNextNodes(self, node):
        if node is not None:
            return node.children

    def alphabeta(self, node):
        alpha = -9999999
        beta = 9999999
        print("node:", node.Name)
        nextNodes = self.getNextNodes(node)
        next_move = None
        for child in nextNodes:
            value = self.minValue(child, alpha, beta)
            if value > alpha:
                alpha = value
                next_move = child
        print("utility:", alpha)
        print("move:", next_move.getName())
        return next_move

    def maxValue(self, node, alpha, beta):
        print("node:", node.Name)
        if node.value != None:
            return node.value
        value = -9999999
        if node is not None:
            nextNodes = node.children
            for Nodes in nextNodes:
                value = max(value, self.minValue(Nodes, alpha, beta))
                if value >= beta:
                    print("now pruning")
                    return value
                alpha = max(alpha, value)
            return value

    def minValue(self, node, alpha, beta):
        print("node:", node.Name)
        if node.value != None:
            return node.value
        value = 9999999
        if node is not None:
            nextNodes = node.children
            for Nodes in nextNodes:
                value = min(value, self.maxValue(Nodes, alpha, beta))
                if value <= alpha:
                    print("now pruning")
                    return value
                beta = min(beta, value)
            return value


def inputData():
    inData = sys.argv
    data = open(inData[1], 'r')
    line = data.read()
    tree = ast.literal_eval(line)
    print("******************************************")
    print("****************Minimax sol***************")
    sol_tree = Tree(tree)
    sol = miniMax(sol_tree)
    sol.minimax(sol.root)
    print("******************************************")
    print("**************Alpha-beta sol**************")
    sol1_tree = Tree(tree)
    sol1 = alphaBeta(sol1_tree)
    sol1.alphabeta(sol1.root)
    print("******************************************")


inputData()
