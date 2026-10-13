# Sorting Algorithms in Python 🚀

A curated collection of efficient and foundational sorting algorithms implemented in clean, idiomatic Python.

---

## 📌 Repository Overview

This repository contains implementations of classic sorting algorithms and partitioning techniques commonly utilized in technical interviews, competitive programming, and real-world system design.

### 📊 Complexity & Characteristics Comparison

| Algorithm | Best Time | Average Time | Worst Time | Space Complexity | In-Place? | Stable? | Primary Use Case |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Dutch National Flag (DNF)** | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | Yes | No | 3-way partitioning (e.g., sorting 0s, 1s, and 2s) |
| **Merge Sort** | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n)$ | No | Yes | General-purpose sorting with guaranteed $\mathcal{O}(n \log n)$ performance |

---

## 📂 Included Implementations

### 1. Dutch National Flag Algorithm (`DutchNationalFlagAlgorithm.py`)

#### 📖 Description
The **Dutch National Flag (DNF)** algorithm is a 3-way partitioning algorithm originally designed by computer scientist **Edsger W. Dijkstra**. It is specifically tailored to sort an array containing three distinct values (commonly represented as `0`, `1`, and `2`, or three categories/colors) in a single linear pass without using extra memory.

#### ⚙️ How It Works
The algorithm maintains three pointers:
- `left`: Boundary for elements equal to `0`. Everything before index `left` is `0`.
- `mid`: Current element being inspected. Everything between `left` and `mid - 1` is `1`.
- `high`: Boundary for elements equal to `2`. Everything after index `high` is `2`.

**Array Partition Zones:**
```text
[ 0 ... left-1 ]  --> All 0s
[ left ... mid-1 ] --> All 1s
[ mid ... high ]   --> Unprocessed / Unknown elements
[ high+1 ... n-1 ] --> All 2s
```

#### 🔄 Pointer Transitions:
- If `nums[mid] == 0`: Swap `nums[left]` and `nums[mid]`, then increment both `left += 1` and `mid += 1`.
- If `nums[mid] == 1`: The element is already in the correct middle segment; simply increment `mid += 1`.
- If `nums[mid] == 2`: Swap `nums[mid]` and `nums[high]`, then decrement `high -= 1` (do **not** increment `mid` yet, as the newly swapped element at `mid` needs evaluation).

#### 💻 Code Preview:
```python
nums = [0, 1, 2, 1, 2, 0]

def Sorting(nums):
    left = mid = 0
    high = len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[left], nums[mid] = nums[mid], nums[left]
            left += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

Sorting(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]
```

- **Time Complexity:** $\mathcal{O}(n)$ (single traversal)
- **Space Complexity:** $\mathcal{O}(1)$ (in-place)

---

### 2. Merge Sort (`MergeSort.py`)

#### 📖 Description
**Merge Sort** is a canonical **Divide-and-Conquer** sorting algorithm. It recursively breaks down a list into smaller sub-lists until each sub-list contains a single element (which is inherently sorted), and then merges those sub-lists in sorted order.

#### ⚙️ How It Works
1. **Divide:** Compute midpoint `mid = left + (right - left) // 2` to split the range $[left, right]$ into two halves: $[left, mid]$ and $[mid + 1, right]$.
2. **Conquer:** Recursively sort both sub-arrays.
3. **Combine (Merge):** Maintain two pointers across both sorted halves and insert the smaller element into an auxiliary buffer `temp`. Once one half is exhausted, append the remaining elements and copy `temp` back into the original array.

#### 💻 Code Preview:
```python
class Solution:
    def sort(self, nums: list[int]) -> list[int]:
        def mergeSort(left, right):
            if left >= right:
                return 
            
            mid = left + (right - left) // 2
            mergeSort(left, mid)
            mergeSort(mid + 1, right)
            merge(left, mid, right)
        
        def merge(left, mid, right):
            temp = []
            i = left 
            j = mid + 1

            while i <= mid and j <= right:
                if nums[i] < nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            
            while i <= mid:
                temp.append(nums[i])
                i += 1
            
            while j <= right:
                temp.append(nums[j])
                j += 1

            for k in range(len(temp)):
                nums[left + k] = temp[k]

        mergeSort(0, len(nums) - 1)
        return nums

sol = Solution()
print(sol.sort([3, 23, 41, 45, 27, 3, 7, 83]))
# Output: [3, 3, 7, 23, 27, 41, 45, 83]
```

- **Time Complexity:** $\mathcal{O}(n \log n)$ across all cases (Best, Average, Worst).
- **Space Complexity:** $\mathcal{O}(n)$ auxiliary space used during the merge phase.
- **Stability:** Stable sort (preserves relative order of equal keys).

---

## 🚀 Getting Started & Execution

Ensure you have Python 3.7+ installed.

### Clone the Repository
```bash
git clone https://github.com/Dileep2006/Sorting_Algorithms.git
cd Sorting_Algorithms
```

### Run Dutch National Flag Algorithm
```bash
python DutchNationalFlagAlgorithm.py
```
**Output:**
```
[0, 0, 1, 1, 2, 2]
```

### Run Merge Sort
```bash
python MergeSort.py
```
**Output:**
```
[3, 3, 7, 23, 27, 41, 45, 83]
```

---

## 📁 Repository Structure

```text
Sorting_Algorithms/
├── DutchNationalFlagAlgorithm.py   # O(n) time, O(1) space 3-way partitioning
├── MergeSort.py                    # O(n log n) Divide and Conquer sorting
└── README.md                       # Documentation and complexity analysis
```

---

## 👤 Author
Developed and maintained by [Dileep2006](https://github.com/Dileep2006).