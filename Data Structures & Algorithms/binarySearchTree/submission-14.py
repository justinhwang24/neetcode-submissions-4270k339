class Node:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = Node(key, val)
        if not self.root:
            self.root = newNode
            return
        curr = self.root
        while curr:
            if key < curr.key:
                if not curr.left:
                    curr.left = newNode
                    return
                curr = curr.left
            elif key > curr.key:
                if not curr.right:
                    curr.right = newNode
                    return
                curr = curr.right
            else:
                curr.val = val
                return
        return

    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        return -1

    def getMin(self) -> int:
        curr = self.root
        while curr and curr.left:
            curr = curr.left
        return curr.val if curr else -1

    def getMax(self) -> int:
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val if curr else -1

    def findMin(self, node) -> Node:
        while node and node.left:
            node = node.left
        return node
    
    def remove(self, key: int) -> None:
        self.root = self.removeHelp(self.root, key)
    
    def removeHelp(self, curr: Node, key: int) -> Node:
        if not curr:
            return None
        if key > curr.key:
            curr.right = self.removeHelp(curr.right, key)
        elif key < curr.key:
            curr.left = self.removeHelp(curr.left, key)
        else:
            if not curr.left:
                return curr.right
            elif not curr.right:
                return curr.left
            else:
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeHelp(curr.right, minNode.key)
        return curr

    def getInorderKeys(self) -> List[int]:
        res = []
        self.getInorderKeysHelp(self.root, res)
        return res
    
    def getInorderKeysHelp(self, node, res):
        if not node:
            return []
        self.getInorderKeysHelp(node.left, res)
        res.append(node.key)
        self.getInorderKeysHelp(node.right, res)
