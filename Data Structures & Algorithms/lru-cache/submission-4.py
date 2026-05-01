class DoubleNode:

    def __init__(self, key, *, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.values = {}
        self.usage_nodes = {}
        self.least_used = None
        self.recently_used = None

    def __refresh_key(self, key: int):
        if key in self.usage_nodes:
            node = self.usage_nodes[key]
            
            if node.right is None:
                return
            else:
                node.right.left = node.left

            if node.left is None:
                self.least_used = node.right
            else:
                node.left.right = node.right
        else:
            node = DoubleNode(key)
            self.usage_nodes[key] = node
            if self.least_used is None:
                self.least_used = node
            self.size += 1

        node.left = self.recently_used
        if self.recently_used is not None:
            self.recently_used.right = node

        node.right = None
        self.recently_used = node
        if self.least_used is None:
            self.least_used = node

        if self.size > self.capacity:
            node = self.least_used
            del self.values[node.key]
            del self.usage_nodes[node.key]
            self.least_used = node.right
            del node
            self.least_used.left = None
            self.size -= 1

        curr = self.least_used
        while curr is not None:
            curr = curr.right

    def get(self, key: int) -> int:
        if key not in self.values:
            return -1
        val = self.values[key]
        self.__refresh_key(key)
        return val        

    def put(self, key: int, value: int) -> None:
        self.values[key] = value
        self.__refresh_key(key)
        
