class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """ Binary Search: O(log n)
        1. When found a target, instead of return mid, keep searching for leftmost/rightmost target
        2. Set r = mid - 1,to search start
        3. Set l = mid + 1 to search end
        4. The while loop only break when l > r, which we have process all targets
        """
        # is_left = boolean to decide search left or right half
        def search(nums, target, is_left):
            l, r = 0, len(nums) - 1
            i = -1
            while l <= r:
                mid = (l + r) // 2
                if target > nums[mid]:
                    l = mid + 1
                elif target < nums[mid]:
                    r = mid - 1
                # otherwise find another target, find its leftmost/rightmost until l > r
                else:
                    i = mid
                    if is_left:
                        r = mid - 1     # search start position
                    else:
                        l = mid + 1     # search end position
            return i        
        
        # now, call the functions to find start and end position
        start = search(nums, target, True)
        end = search(nums, target, False)
        return [start, end]