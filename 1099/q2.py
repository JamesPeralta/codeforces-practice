"""
Given an array a, let f(a) be the number of ways to partition a.

- each elem appears in exactly one subarray (use up all elems, no orphans)
- All subarrays have the same sum.

f([1, 1])
  1. [1, 1]
  2. [1] [1]

Given x and y.

use x 1s
use y -1s

We can have some permutation of those numbers.

How does the permutation affect the output?

x = 2
y = 1

1 1 -1
"""