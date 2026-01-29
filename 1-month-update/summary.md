# 1-Month Update — Practice Summary

**Total problems solved:** 29

Overview of what you learned, grouped by pattern/topic, with counts.

---

## Topic counts

| Topic | Count | Problems |
|-------|-------|----------|
| **Greedy** | 3 | 3798, 3809, reverse_a_permutation |
| **DP / Memoization** | 3 | 3796, huge_pile, product_queries |
| **Case analysis / Ad-hoc / Direct formula** | 3 | binary_array_game, perfect_root, prefix_max |
| **Modular arithmetic / Parity** | 3 | dbmb_and_the_array, hourglass, social_experiment |
| **Brute force** | 2 | 3799, 3804 |
| **Single pass** | 2 | 3803, 3813 |
| **Array scan / manipulation** | 2 | 3818, 3819 |
| **Simulation** | 2 | out_of_memory_error, the_robotic_rush |
| **Sliding window / Two pointers** | 2 | 3795, 3810 |
| **Binary search** | 1 | monster_game |
| **Prefix sum** | 1 | replace_and_sum |
| **Hashing / normalization** | 1 | 3805 |
| **BFS / Graph** | 1 | 3820 |
| **Combinatorics** | 1 | 3821 |
| **String manipulation** | 1 | 3794 |
| **Longest consecutive subsequence** | 1 | shifted_mex |

*Some problems use multiple techniques; each is counted under one primary topic above.*

---

## Techniques used (multi-count)

When a problem uses more than one idea, it appears under each:

| Technique | # of problems |
|-----------|----------------|
| Greedy | 5 (3796, 3798, 3809, monster_game, reverse_a_permutation) |
| Hash map / Set | 4 (3795, 3803, 3804, 3805) |
| Two pointers / Sliding window | 2 (3795, 3810) |
| DP / Memoization | 3 (3796, huge_pile, product_queries) |
| Binary search | 2 (monster_game, the_robotic_rush) |
| Prefix sum | 3 (monster_game, replace_and_sum, the_robotic_rush) |
| Simulation | 2 (out_of_memory_error, the_robotic_rush) |
| Single pass | 2 (3803, 3813) |
| Brute force | 2 (3799, 3804) |
| BFS | 1 (3820) |
| Combinatorics | 1 (3821) |
| String manipulation | 1 (3794) |
| Array scan / manipulation | 2 (3818, 3819) |
| Case analysis / Ad-hoc / Formula | 3 (binary_array_game, perfect_root, prefix_max) |
| Modular arithmetic / Parity | 3 (dbmb_and_the_array, hourglass, social_experiment) |
| Longest consecutive run | 1 (shifted_mex) |

---

## What you learned (by category)

### Greedy
- **When:** Make a sequence of choices that look best locally and still yield a correct global answer.
- **Examples:** Remove trailing 1s so a string ends with 2 (3798); pick best tower by quality then lex order (3809); fix a permutation by reversing one segment that brings the next max into place (reverse_a_permutation).
- **Takeaway:** Often used with “remove/choose until condition” or “one reversible move.”

### DP / Memoization
- **When:** Optimal substructure + overlapping subproblems; counting or minimizing steps/cost.
- **Examples:** Propagate constraints backward then build sequence (3796); min steps to reach `k` by repeatedly splitting `n` (huge_pile); min elements to get value `i` using factors (product_queries).
- **Takeaway:** Define state (e.g. index or value), recurrence, and base cases; cache by state.

### Sliding window / Two pointers
- **When:** Contiguous subarray/substring with a condition (e.g. sum ≥ k, same value).
- **Examples:** Min length subarray with “distinct sum” ≥ k (3795); maximal segments of same value (3810).
- **Takeaway:** Expand right, shrink left when the condition holds; use a frequency map or similar to maintain the invariant.

### Hashing / Set
- **When:** Need to count, group, or check “same as something seen” in O(1).
- **Examples:** Caesar-equivalent pairs via normalized form (3805); centered subarrays where sum is in the set of elements (3804); residue prefixes with unique-char count (3803).
- **Takeaway:** Design a canonical form or key so equivalent objects hash the same.

### Binary search & prefix sum
- **When:** “How many elements satisfy X?” or “first position where condition holds” + cumulative sums.
- **Examples:** Maximize (sword strength × levels passable) using bisect on prefix sum (monster_game); closest spike + move simulation + cumulative deaths (the_robotic_rush).
- **Takeaway:** Sort if needed, build prefix sum, then use binary search to count or find boundaries.

### Simulation
- **When:** Process events or steps in order; state changes over time.
- **Examples:** Lazy reset when a value exceeds threshold (out_of_memory_error); compress moves to positions, then compute when each robot hits a spike (the_robotic_rush).
- **Takeaway:** Keep state compact (e.g. last_reset per index, or “position → first time reached”).

### BFS / Graph
- **When:** Shortest path or distances in an unweighted graph (or tree).
- **Example:** BFS from three nodes (x, y, z), then count nodes whose distances form a Pythagorean triple (3820).
- **Takeaway:** Multi-source BFS gives distances from multiple roots; then apply a condition on those distances.

### Combinatorics
- **When:** “nth smallest with property” or counting with structure.
- **Example:** nth smallest integer with exactly k one-bits using binomial coefficients (3821).
- **Takeaway:** Place digits/bits one by one; use C(n, k) or similar to skip ranges.

### Modular arithmetic / Parity
- **When:** Answer depends on remainder or odd/even.
- **Examples:** diff % x == 0 (dbmb_and_the_array); position after m steps using m // k and m % k (hourglass); n % 2 for “splitting by 3” (social_experiment).
- **Takeaway:** Write down a few small cases and express the answer in terms of mod or parity.

### Single pass & array tricks
- **When:** One or two passes over the array; no full brute force.
- **Examples:** Count vowels/consonants (3813); track unique chars and residue (3803); longest strictly decreasing suffix by scanning from the right (3818); gather non-negatives, rotate, scatter (3819).
- **Takeaway:** Often “scan and maintain one or two variables” or “scan from the end” for suffix structure.

### Case analysis / Ad-hoc
- **When:** Problem-specific rule or small number of cases.
- **Examples:** Winner from first and last character (binary_array_game); output 1..n (perfect_root); answer = n × max(array) (prefix_max).
- **Takeaway:** Try small examples and edge cases; codify the pattern in a few branches.

### Longest consecutive run
- **When:** “Longest contiguous block” in a sequence (after sorting or in order).
- **Example:** Sort, then longest run where a[i] = a[i-1] + 1 (shifted_mex).
- **Takeaway:** Sort (if allowed), then one pass tracking current run length.

---

## Next steps

- **Most practice:** Greedy, DP, hashing, modular/parity, case analysis.
- **Good to reinforce:** Two pointers, prefix sum, binary search, simulation.
- **Rarer but important:** BFS, combinatorics, longest run, constraint propagation.

Use this as a quick reference when you see a new problem: guess the topic from the problem type, then match to one of these patterns.
