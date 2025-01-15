# Introduction to Complexity Analysis (7 - 14 Jan, 2025)

complexity analysis measures how an algorithm performs as the size of its inputs grows. It allows to:
- Predict Performance: Understand how the algorithm will behave for large inputs.
- Compare Algorithms: Choose the most efficient algorithm for a problem.
- Optimize Code: Reduce execution time and memory usage.

# key concept of Complexity Analysis
1. Big-O notation:
Big 0-notation describe the *Upper bound* of an algorithm growth rate. It measure the worst-case scenario.
For instance:
- 0(1) - Constantine time (fastest)
- 0(log n) - logarithmic time
- 0(n) - Linear time
- 0(n log n) - Log-linear time
- 0(n<sup>2</sup>) - Quadratic time (slower)

Why Big-O? It abstracts away hardware differences and focuses on scalability.

2. Time Complexity:
Measures the number of operations an algorithm performs relative to input size.

3. Space Complexity:
Measures the additional memory the algorithm uses relative to input size.

# Why Is It Useful?
1. Helps design efficient algorithms.
2. Helps predicts system scalability.
3. Guides trade-offs between speed and memory.
4. Avoids bottlenecks in software solutions.

# When to use it?
1. When designing software design that handles large datasets.
2. To identify performance-critical section of the code
3. When comparing multiple algorithms for the same task.

# Code Samples

1. Constant Time Complexity: 0(1) <br />
No matter the size of the input, the operation count remain constant. See `constant-time.py` for code.

2. Linear Time Complexity: 0(n) <br />
The number of operation grows linearly with input size. See `linear-time.py` for code.

3. Quadratic Time Complexity: 0(n<sup>2</sup>) <br />
Nested loops over the same data cause quadratic growth.. See `quadratic-time.py` for code.

4. Logarithmic Time Complexity: O(log n)
This often occurs in divide-and-conquer algorithms, like binary search. See `logarithmic-time.py` for code