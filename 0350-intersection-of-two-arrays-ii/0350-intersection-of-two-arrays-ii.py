class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        # Find the intersection by taking the minimum count for each element present in both arrays
        intersection = []
        for num in count1:
            if num in count2:
                # Append the number min(count1[num], count2[num]) times to the result
                intersection.extend([num] * min(count1[num], count2[num]))
        
        return intersection