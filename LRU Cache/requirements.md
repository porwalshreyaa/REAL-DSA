## Build a Cache that has:

Product Manager Question

1. Input type: string (key)
2. Output type: string (value)
3. key-value each limit: 100 characters
4. cache limit: 20 items
5. cache reset: No
6. item time limit: 20s
7. what to do on overflow? remove least recently used
8. time complexity space complexity
9. If we have multiple least recently used then which one to delete?
10. Time complexity?
11. if we have 2 entries and hits overflow one expires and one is least recently used, which one to delete first?


Engineering Questions
1. 

What our Cache stores?


What our Node stores?
1. creation time - to calculate time to live
2. last used time - to track least recently used
3. value
4. 