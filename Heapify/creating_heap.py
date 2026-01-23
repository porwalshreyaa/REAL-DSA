class MinHeap:
    def __init__(self):
        self.arr = []
    def insert(self, value):
        self.arr.append(value) #suppose arr is empty rn
        n = len(self.arr)
        self._compare_parent_and_swap(n-1)
    def delete(self):
        n =len(self.arr)
        self.arr[0],self.arr[n-1]=self.arr[n-1],self.arr[0]
        self.arr.pop()
        self._compare_child_and_swap(0)
    def _compare_parent_and_swap(self, index):
        if index>0:
            p = (index-1)//2 # p = parent
            if self.arr[p] > self.arr[index]:
                self.arr[p], self.arr[index] = self.arr[index], self.arr[p]
            return self._compare_parent_and_swap(p)
        else:
            return
    def _compare_child_and_swap(self, index):
        n = len(self.arr)
        smallest = index # index of smallest element seen so far
        l = 2*index +1 # l = left child
        r = 2*index +2 # r = right child
        if l<n and self.arr[l]<self.arr[smallest]:
            smallest=l
        if r<n and self.arr[r]<self.arr[smallest]:
            smallest=r
        if smallest != index:
            self.arr[index], self.arr[smallest]=self.arr[smallest], self.arr[index] # swap the smallest with parent -> min heap
            self._compare_child_and_swap(smallest) # repeat with the swapped element
    def show(self):
        for i in self.arr:
            print(i)

# array = MinHeap()
# array.insert(4)
# array.insert(5)
# array.insert(1)
# array.insert(2)
# array.insert(3)
# array.insert(7)
# array.insert(12)
# array.show() # [1,2,4,5,3,7,12]
# print("after delete")
# array.delete()
# array.delete()
# array.show() 

# Heapify - parent to children but start from last
# for minimum

def BottomCompare(arr, index): # compare parent node with it's children
    n = len(arr) # array size
    smallest = index # index of smallest element seen so far
    l = index*2 + 1 # l = left child
    r = index*2 + 2 # r = right child
    if l < n and arr[l]<arr[smallest]: # child node index present in array  and node left child node smaller than smallest
        smallest=l # update index of smallest seen
    if r < n and arr[r]<arr[smallest]: 
        smallest=r
    if smallest!=index:
        arr[smallest], arr[index]=arr[index], arr[smallest] # swap the smallest with parent -> min heap
        BottomCompare(arr, smallest) # repeat this with the swapped index - 
        # why? - incase it is larger than other descendants as well? example - the largest misplaced at top most should go to bottom most

def heapify(arr): # arr = array
    if (not isinstance(arr, list)):
        raise TypeError("Invalid Input!")
    n = len(arr) # length of array
    if n<2: # if there is only 1 element or empty array
        return arr
    currentIndex = n-1 # start from last element
    while currentIndex>=0: 
        BottomCompare(arr,currentIndex) # heapify/fix the order of indexes - inorder of last filled child node to root node 
        currentIndex-=1 
    return arr

array2 = [5,2,0,1,9,100,4]

print(heapify(array2)) # [0,1,4,2,9,100,5]