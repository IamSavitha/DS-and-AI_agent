# 🎯 Interview Preparation - Data Structures & Algorithms

## Complete Guide for Technical Interviews

This folder contains comprehensive preparation materials for technical interviews focusing on **Data Structures** and **Algorithms** in Python. Perfect for aspiring Data Scientists, Machine Learning Engineers, Software Engineers, and Data Engineers.

---

## 📚 Structure

```
04_Interview_Prep/
├── 01_Data_Structures/          # Core data structures
│   ├── Arrays/
│   ├── LinkedLists/
│   ├── Stacks/
│   ├── Queues/
│   ├── Trees/
│   ├── Graphs/
│   ├── HashTables/
│   └── Heaps/
│
├── 02_Algorithms/                # Fundamental algorithms
│   ├── Sorting/
│   ├── Searching/
│   ├── Dynamic_Programming/
│   ├── Greedy/
│   ├── Graph_Algorithms/
│   ├── Two_Pointers/
│   ├── Sliding_Window/
│   └── Backtracking/
│
├── 03_LeetCode_Patterns/        # Common problem patterns
│   ├── Array_Problems/
│   ├── String_Problems/
│   ├── Tree_Problems/
│   └── Graph_Problems/
│
└── 04_System_Design_Basics/     # System design fundamentals
```

---

## 🎯 Learning Path

### **Week 1-2: Data Structures Fundamentals**

#### Arrays & Strings
- Array operations and common patterns
- Two-pointer technique
- Sliding window
- String manipulation

#### Linked Lists
- Singly, Doubly, Circular linked lists
- Common operations
- Fast & slow pointers

#### Stacks & Queues
- Implementation and applications
- Monotonic stack pattern
- BFS using queues

### **Week 3-4: Trees & Graphs**

#### Trees
- Binary trees, BST, AVL trees
- Tree traversal (DFS, BFS)
- Tree construction problems

#### Graphs
- Graph representation (adjacency list/matrix)
- DFS and BFS
- Shortest path algorithms
- Topological sort

### **Week 5-6: Hash Tables & Advanced Structures**

#### Hash Tables
- Implementation and collision handling
- Common use cases
- Hash functions

#### Heaps
- Min/Max heap implementation
- Priority queues
- Heap sort

### **Week 7-8: Core Algorithms**

#### Sorting & Searching
- Comparison-based sorts (Quick, Merge, Heap)
- Linear and binary search
- Search in rotated arrays

#### Dynamic Programming
- Memoization vs tabulation
- 1D, 2D DP problems
- Common DP patterns

### **Week 9-10: Advanced Patterns**

#### Two Pointers & Sliding Window
- Two sum problems
- Sliding window technique
- Meeting point problems

#### Greedy Algorithms
- Activity selection
- Interval scheduling
- Greedy optimization

#### Backtracking
- N-Queens
- Subset generation
- Permutation problems

### **Week 11-12: Practice & Patterns**

#### LeetCode Patterns
- Common problem patterns
- Template solutions
- Time/space complexity analysis

#### System Design Basics
- Scalability concepts
- Database design
- API design

---

## 📖 How to Use This Repository

### **For Interview Prep:**

1. **Start with Data Structures** (`01_Data_Structures/`)
   - Understand each structure thoroughly
   - Implement from scratch
   - Practice common operations

2. **Master Algorithms** (`02_Algorithms/`)
   - Learn fundamental algorithms
   - Understand time/space complexity
   - Practice variations

3. **Solve Pattern Problems** (`03_LeetCode_Patterns/`)
   - Recognize common patterns
   - Apply templates to new problems
   - Build problem-solving intuition

4. **System Design Basics** (`04_System_Design_Basics/`)
   - Understand scalability
   - Learn design principles
   - Practice design questions

---

## 🎓 Each Notebook Contains

### **Structure:**
1. **Introduction** - What is the data structure/algorithm?
2. **Implementation** - From-scratch Python implementation
3. **Operations** - Common operations with examples
4. **Time/Space Complexity** - Analysis for each operation
5. **Use Cases** - When to use this structure/algorithm
6. **Practice Problems** - LeetCode-style problems with solutions
7. **Common Patterns** - Interview patterns and templates
8. **Tips & Tricks** - Interview tips and common pitfalls

---

## 📝 Interview Strategy

### **Before the Interview:**
- ✅ Review all data structures (1-2 days)
- ✅ Practice 10-15 problems per category
- ✅ Understand time/space complexity
- ✅ Practice explaining your thought process

### **During the Interview:**
1. **Clarify the problem** - Ask questions
2. **Think out loud** - Explain your approach
3. **Start simple** - Brute force first, then optimize
4. **Write clean code** - Follow Python best practices
5. **Test your solution** - Walk through examples
6. **Optimize** - Discuss time/space improvements

### **Common Mistakes to Avoid:**
- ❌ Jumping to code without understanding
- ❌ Not considering edge cases
- ❌ Ignoring time/space complexity
- ❌ Not communicating your thought process
- ❌ Giving up too early

---

## 🔥 Essential Topics for Interviews

### **Must Know:**
- Arrays and Strings manipulation
- Hash Tables (dictionaries in Python)
- Two Pointers technique
- Sliding Window
- Binary Search
- Tree/Graph traversals
- Dynamic Programming basics

### **Should Know:**
- Linked Lists operations
- Stack/Queue applications
- Heap operations
- Backtracking
- Greedy algorithms
- Graph algorithms (BFS/DFS, shortest paths)

### **Nice to Know:**
- Advanced tree structures (Trie, Segment Tree)
- Union-Find (Disjoint Set)
- Advanced graph algorithms
- String algorithms (KMP, Rabin-Karp)

---

## 💡 Coding Tips for Interviews

### **Python Best Practices:**
```python
# Use built-in data structures effectively
from collections import defaultdict, deque, Counter

# List comprehensions for clean code
result = [x*2 for x in arr if x > 0]

# Use enumerate for index + value
for i, val in enumerate(arr):
    pass

# Use zip for parallel iteration
for a, b in zip(arr1, arr2):
    pass
```

### **Common Patterns:**

**Two Pointers:**
```python
left, right = 0, len(arr) - 1
while left < right:
    # Process
    left += 1
    right -= 1
```

**Sliding Window:**
```python
left = 0
for right in range(len(arr)):
    # Expand window
    while condition:
        # Contract window
        left += 1
```

**DFS Template:**
```python
def dfs(node, visited):
    if node in visited:
        return
    visited.add(node)
    # Process node
    for neighbor in node.neighbors:
        dfs(neighbor, visited)
```

---

## 📊 Complexity Cheat Sheet

| Data Structure | Access | Search | Insert | Delete |
|---------------|--------|--------|--------|--------|
| Array | O(1) | O(n) | O(n) | O(n) |
| Hash Table | O(1) | O(1) | O(1) | O(1) |
| Linked List | O(n) | O(n) | O(1) | O(1) |
| Stack/Queue | O(n) | O(n) | O(1) | O(1) |
| Binary Search Tree | O(log n) | O(log n) | O(log n) | O(log n) |
| Heap | O(1) | O(n) | O(log n) | O(log n) |

---

## 🎯 Practice Resources

### **Recommended Platforms:**
- **LeetCode** - Most popular interview platform
- **HackerRank** - Good for skill building
- **CodeSignal** - Company-specific practice
- **NeetCode** - Organized by patterns

### **Practice Schedule:**
- **Easy problems**: Build confidence and speed
- **Medium problems**: Most common in interviews
- **Hard problems**: For top companies

### **Daily Routine:**
1. Review 1 data structure concept (30 min)
2. Solve 2-3 problems (1-2 hours)
3. Review solutions and patterns (30 min)
4. Practice explaining solutions (15 min)

---

## 🚀 Quick Start

### **Day 1: Arrays & Two Pointers**
```bash
04_Interview_Prep/
├── 01_Data_Structures/Arrays/
│   └── arrays_complete.ipynb
└── 02_Algorithms/Two_Pointers/
    └── two_pointers_complete.ipynb
```

### **Day 2: Hash Tables**
```bash
01_Data_Structures/HashTables/
└── hash_tables_complete.ipynb
```

### **Day 3: Trees & DFS**
```bash
01_Data_Structures/Trees/
└── trees_complete.ipynb
```

---

## 📚 Additional Resources

### **Books:**
- "Cracking the Coding Interview" by Gayle Laakmann McDowell
- "Elements of Programming Interviews in Python" by Adnan Aziz
- "Algorithm Design Manual" by Steven Skiena

### **Online Courses:**
- LeetCode Explore Cards
- NeetCode YouTube channel
- AlgoExpert

### **Communities:**
- r/cscareerquestions
- LeetCode Discuss
- Blind (for company-specific info)

---

## ✅ Checklist for Interview Day

- [ ] Reviewed all data structures
- [ ] Practiced 50+ problems
- [ ] Can explain time/space complexity
- [ ] Comfortable with Python syntax
- [ ] Practiced coding on whiteboard/screen share
- [ ] Prepared questions to ask interviewer
- [ ] Reviewed company and role

---

## 🎓 Success Tips

1. **Consistency over intensity** - 1-2 hours daily > 10 hours once a week
2. **Understand, don't memorize** - Know WHY solutions work
3. **Practice explaining** - Verbalize your thought process
4. **Learn patterns** - Recognize problem types quickly
5. **Time yourself** - Practice under time pressure
6. **Review mistakes** - Learn from every problem

---

**Good luck with your interviews! 🚀**

*Remember: Interviews are conversations, not tests. Communicate your thinking, ask questions, and show your problem-solving process.*

