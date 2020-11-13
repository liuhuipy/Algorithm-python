"""
    运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
    实现 LRUCache 类：
        LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
        int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
        void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，
        则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
 
    进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？
示例：
    输入
    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
    [null, null, null, 1, null, -1, null, -1, 3, 4]
解释
    LRUCache lRUCache = new LRUCache(2);
    lRUCache.put(1, 1); // 缓存是 {1=1}
    lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
    lRUCache.get(1);    // 返回 1
    lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
    lRUCache.get(2);    // 返回 -1 (未找到)
    lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
    lRUCache.get(1);    // 返回 -1 (未找到)
    lRUCache.get(3);    // 返回 3
    lRUCache.get(4);    // 返回 4

提示：
    1 <= capacity <= 3000
    0 <= key <= 3000
    0 <= value <= 104
    最多调用 3 * 104 次 get 和 put

方法：
    双向链表+HashMap
"""


class DoubleLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.len = 0
        self.cache = {}
        self.head = DoubleLinkedNode()
        self.tail = DoubleLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_head(self, node: DoubleLinkedNode) -> None:
        temp = node.next
        node.prev.next, temp.prev = temp, node.prev
        self.insert_node(node)

    def insert_node(self, node: DoubleLinkedNode):
        self.head.next.prev = node
        node.next, node.prev = self.head.next, self.head
        self.head.next = node

    def remove_tail_node(self):
        self.cache.pop(self.tail.prev.key)
        temp_tail = self.tail.prev.prev
        temp_tail.next, self.tail.prev = self.tail, temp_tail
        self.len -= 1

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_to_head(self.cache[key])
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.move_to_head(self.cache[key])
        else:
            node = DoubleLinkedNode(key, value)
            self.cache[key] = node
            self.insert_node(node)
            self.len += 1
            if self.len > self.cap:
                self.remove_tail_node()


if __name__ == '__main__':
    lru_cache = LRUCache(2)
    print(lru_cache.put(1, 1))
    print(lru_cache.put(2, 2))
    print(lru_cache.get(1))
    print(lru_cache.put(3, 3))
    print(lru_cache.get(2))
    print(lru_cache.put(4, 4))
    print(lru_cache.get(1))
    print(lru_cache.get(3))
    print(lru_cache.get(4))
