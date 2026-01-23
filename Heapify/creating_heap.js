class minHeap {
    constructor() {
        this.arr = []
    }

    insert(value) {
        this.arr.push(value);
        let n = this.arr.length;
        this.#compareParentSwap(n - 1);
    }

    delete() {
        let n = this.arr.length;
        [this.arr[0], this.arr[n - 1]] = [this.arr[n - 1], this.arr[0]]
        this.arr.pop()
        this.#compareChildSwap(0);
    }

    #compareParentSwap(index) {
        index = parseInt(index)
        if (index > 0) {
            let p = parseInt((index - 1) / 2)
            if (this.arr[p] > this.arr[index]) {
                [this.arr[p], this.arr[index]] = [this.arr[index], this.arr[p]]
                this.#compareParentSwap(p)
            }
        }
    }
    #compareChildSwap(index) {
        index = parseInt(index)
        let n = this.arr.length;
        let smallest = index;
        let l = 2 * index + 1;
        let r = 2 * index + 2
        if (l < n && this.arr[l] < this.arr[smallest]) {
            smallest = l
        };
        if (r < n && this.arr[r] < this.arr[smallest]) {
            smallest = r
        };
        if (smallest != index) {
            [this.arr[index], this.arr[smallest]] = [this.arr[smallest], this.arr[index]]
            this.#compareChildSwap(smallest);
        }
    }
    printAsArray() {
        for (const i of this.arr) {
            console.log(i)
        }
    }
}

let array = new minHeap()
// array.insert(4)
// array.insert(5)
// array.insert(1)
// array.insert(2)
// array.insert(3)
// array.insert(7)
// array.insert(12)
// array.printAsArray() // [1,2,4,5,3,7,12]
// console.log()
// console.log("after delete")
// console.log()
// array.delete()
// array.delete()
// array.printAsArray() // [3,5,4,7,12]



// Independent Heapify Implementation


function topToBottomSwap(index, arrLength){
    index = parseInt(index)
    let smallest = index;
    let l = 2 * index + 1;
    let r = 2 * index + 2
    if (l < arrLength && array[l] < array[smallest]) {
        smallest = l
    };
    if (r < arrLength && array[r] < array[smallest]) {
        smallest = r
    };
    if (smallest != index) {
        [array[index], array[smallest]] = [array[smallest], array[index]]
        topToBottomSwap(smallest);
    }
}

function heapify(array) { //input type should be array
    if (!Array.isArray(array)) {
        throw new Error("Invalid Input");
    }
    let n = array.length
    if (n < 2) {
        return array
    }
    let currentIndex = n - 1
    while (currentIndex >= 0) {
        topToBottomSwap(currentIndex, n)
        currentIndex -= 1
    }
    return array
}

array = [1, 12, 2, 4, 5]

console.log(heapify(array));