# 632. Smallest Range Covering Elements from K Lists

__Type:__ Hard <br>
__Topics:__ Array, Hash Table, Greedy, Sliding Window, Sorting, Heap (Priority Queue) <br>
__Companies:__ Amazon, PhonePe, Google, Microsoft, Lyft, WinZO, Flipkart, Databricks, Bloomberg, Adobe, Schrodinger, Snap, Apple, DE Shaw, Pinterest, ClearTax <br>
__LeetCode Link:__ [Smallest Range Covering Elements from K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/description/)
<hr>

You have `k` lists of sorted integers in __non-decreasing order__. Find the __smallest__ range that includes at least one number from each of the `k` lists.

We define the range `[a, b]` is smaller than range `[c, d]` if `b - a < d - c` or `a < c` if `b - a == d - c`.
<hr>

### Examples:

- __Example 1:__ <br>
__Input:__ nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]] <br>
__Output:__ [20,24] <br>
__Explanation:__ <br>
List 1: [4, 10, 15, 24,26], 24 is in range [20,24]. <br>
List 2: [0, 9, 12, 20], 20 is in range [20,24]. <br>
List 3: [5, 18, 22, 30], 22 is in range [20,24].

- __Example 2:__ <br>
__Input:__ nums = [[1,2,3],[1,2,3],[1,2,3]] <br>
__Output:__ [1,1]
<hr> 

### Constraints:

- `nums.length == k`
- `1 <= k <= 3500`
- `1 <= nums[i].length <= 50`
- <code>-10<sup>5</sup> <= nums[i][j] <= 10<sup>5</sup></code>
- `nums[i]` is sorted in non-decreasing order.
