from datetime import datetime
import heapq

def now():
    return datetime.now().timestamp()

class Node:
    def __init__(self, value):
        self.value = value
        self.last_used = now()
        self.created = now()
    
    def check_valid(self):
        if now() - self.created >= 20:
            return False
        return True

class Cache:
    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.storage = {}
        self.heap = []
    
    def write(self, key, value):
        if len(self.storage) >= self.capacity and key not in self.storage:
            self.delete_least_recently_used()
        node = Node(value)
        self.storage[key] = node
        heapq.heappush(self.heap, (node.last_used, key))

    def read(self, key):
        if key in self.storage:
            node = self.storage[key]
            if node.check_valid():
                node.last_used = now()
                return node.value
        value = get_value_from_db(key) # assuming some function returns value from db
        self.write(key, value)
        return value
    def delete_least_recently_used(self):
        while self.heap:
            timestamp, key = heapq.heappop(self.heap)
            if key in self.storage:
                node = self.storage[key]
                if node.last_used == timestamp:
                    del self.storage[key]
                    return


testcases = [
    (test_op, test_in, test_out)
]

def solution(test_op, test_in):
    pass

result = []
for test_op, test_in, test_out in testcases:
    result.append(solution(test_op, test_in) == test_out)


print(i for i in result)