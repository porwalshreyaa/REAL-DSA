from datetime import datetime
from mock_rollno_score_db import db_read
import time


"""
How would my oldest created Node look like?
value = something
last used = xxx time
created = xxx time
node created before it = None
node created after it = None/Not None
"""

def now():
    return datetime.now().timestamp()


class Node:
    def __init__(self, key:str, value:str, ttl:int):
        self.key = key
        self.value = value
        self.expiry = now() + ttl
        self.node_created_before_it = None
        self.node_created_after_it = None
        self.node_used_before_it = None
        self.node_used_after_it = None
    

class QuadroCache:
    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.storage = {}
        self.used_head = None #first used (oldest)
        self.used_tail = None #last used (newest)
        self.created_head = None #first created (oldest)
        self.created_tail = None #last created (newest)


    def _add_recently_used(self, new_node):
        if not self.used_head:
            self.used_head = new_node
        else:
            new_node.node_used_before_it = self.used_tail
            self.used_tail.node_used_after_it = new_node
        self.used_tail = new_node

    def _add_recently_created(self, new_node):
        if not self.created_head:
            self.created_head = new_node
        else:
            new_node.node_created_before_it = self.created_tail
            self.created_tail.node_created_after_it = new_node
        self.created_tail = new_node
    
    def _remove_from_used(self, node):
        if node.node_used_before_it:
            node.node_used_before_it.node_used_after_it = node.node_used_after_it
        else:
            self.used_head = node.node_used_after_it
        if node.node_used_after_it:
            node.node_used_after_it.node_used_before_it = node.node_used_before_it
        else:
            self.used_tail = node.node_used_before_it
        node.node_used_before_it = None
        node.node_used_after_it = None

    def _remove_from_created(self, node):
        if node.node_created_before_it:
            node.node_created_before_it.node_created_after_it = node.node_created_after_it
        else:
            self.created_head = node.node_created_after_it
        if node.node_created_after_it:
            node.node_created_after_it.node_created_before_it = node.node_created_before_it
        else:
            self.created_tail = node.node_created_before_it
        node.node_created_before_it = None
        node.node_created_after_it = None

    def _delete_expired_cache(self):
        while  self.created_head and self.created_head.expiry <= now():
            temp = self.created_head
            self._remove_from_used(temp)
            if temp == self.created_tail:
                self.created_head = None
                self.created_tail = None
            else:
                self.created_head = temp.node_created_after_it
                self.created_head.node_created_before_it = None
                temp.node_created_after_it = None
            del self.storage[temp.key]
    
    def _delete_least_recently_used(self):
        if len(self.storage) < self.capacity:
            return
        temp = self.used_head
        self.used_head = temp.node_used_after_it
        if self.used_head:
            self.used_head.node_used_before_it = None
        else:
            self.used_tail = None
        
        temp.node_used_after_it = None
        self._remove_from_created(temp)
        del self.storage[temp.key]
    
    def _update(self):
        self._delete_expired_cache()
        self._delete_least_recently_used()

    def write(self, key, value):
        """
        Input Format: (TableName,Key) 
        """
        if key in self.storage:
            return
        self._update()
        new_node = Node(key, value, 20)
        self.storage[key] = new_node
        self._add_recently_created(new_node)
        self._add_recently_used(new_node)

    def read(self, key):
        self._delete_expired_cache()
        if key not in self.storage:
            return None
        node = self.storage[key]
        self._remove_from_used(node)
        self._add_recently_used(node)
        return node.value



cache = QuadroCache()

# print(db_read("courses","CS301"))

testcases1 = [
    ("write", ["submissions","SUB060"], None),
    ("read", ["submissions","SUB060"], "Submission(submission_id='SUB060', assignment_id='AS005', roll='22f2421422', submitted_at='2024-02-26 10:30', marks=89)"),
    ("read", ["submissions","ENR001"], None),
    ("write", ["enrollments","ENR001"],  None),
    ("read", ["enrollments","ENR001"], "Enrollment(roll='21f2004662', course_id='CS101', semester=1, status='completed')"),
    ("read", ["courses","CS301"],  None),
    ("write", ["courses","CS301"],  None),
    ("read", ["courses","CS301"], "Course(course_id='CS301', name='Algorithms', credits=4, department='CS', instructor='Dr. Sundar')"),
]

def solution(test_op, test_in):
    match test_op:
        case "write":
            value = db_read(test_in[0], test_in[1])
            cache_written = cache.write(str(test_in), value)
            # print(cache_written)
            return cache_written
        case "read":
            cache_read = cache.read(str(test_in))
            # print(cache_read)
            return cache_read
        case _:
            print("Unknown operation") #not gonna happen though

result = []
for test_op, test_in, test_out in testcases1:
    result.append(solution(test_op, test_in) == test_out)
time.sleep(20)
testcases2 = [
    ("read", ["submissions","SUB060"], None),
    ("read", ["submissions","ENR001"], None),
    ("read", ["enrollments","ENR001"], None),
    ("read", ["courses","CS301"],  None),
    ("read", ["courses","CS301"], None),
]

for test_op, test_in, test_out in testcases2:
    result.append(solution(test_op, test_in) == test_out)

for test_op, test_in, test_out in testcases1:
    result.append(solution(test_op, test_in) == test_out)

for i in result:
    print(i)