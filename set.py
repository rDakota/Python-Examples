class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # LeetCode solution for single number problem
        # Set is like HashSet in java
        seen = set()
        for n in nums:
            if n in seen:
                seen.remove(n)
            else:
                seen.add(n)
        return list(seen)[0]
        