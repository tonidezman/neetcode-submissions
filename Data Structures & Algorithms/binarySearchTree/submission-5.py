class Node:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class TreeMap:

    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        newNode = Node(key, val)
        if self.root is None:
            self.root = newNode
            return

        curr = self.root
        while True:
            if key < curr.key:
                if curr.left is None:
                    curr.left = newNode
                    return
                curr = curr.left
            elif key > curr.key:
                if curr.right is None:
                    curr.right = newNode
                    return
                curr = curr.right
            else:
                curr.val = val
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


    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)


    def removeHelper(self, node: Node, key: int) -> None:
        if node is None:
            return

        if key < node.key:
            node.left = self.removeHelper(node.left, key)
        elif key > node.key:
            node.right = self.removeHelper(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            
            # node has both left and right children
            curr = node.right
            while curr and curr.left:
                curr = curr.left
            node.key = curr.key
            node.val = curr.val
            node.right = self.removeHelper(node.right, curr.key)
        return node


    def getInorderKeys(self) -> List[int]:
        def dfs(node: Node, res: List[int]):
            if node is None:
                return
            dfs(node.left, res)
            res.append(node.key)
            dfs(node.right, res)
        res = []
        dfs(self.root, res)
        return res


