class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(arr, low, high):
            # Choose pivot as middle
            mid = (low + high) // 2

            # Swap pivot to the front, it stay there throughout scanning process
            arr[low], arr[mid] = arr[mid], arr[low]
            pivot = arr[low]

            # "< pivot" boundary
            last_small = low

            # Iterate the subarray from second element (first is pivot)
            for i in range(low + 1, high + 1):
                if arr[i] < pivot:
                    # If current number < pivot, expand < pivot region, then swap
                    # Thus, low + 1 to last_small always < pivot
                    last_small += 1
                    arr[i], arr[last_small] = arr[last_small], arr[i]

            # Swap pivot (now at low) back to its correct index (last_small)
            arr[low], arr[last_small] = arr[last_small], arr[low]

            # Return pivot index
            return last_small

        def quicksort(arr, low, high):
            if low >= high:
                return

            pivot = partition(arr, low, high)

            # Recursively sort each subarray i.e left and right of pivot
            quicksort(arr, low, pivot -1)
            quicksort(arr, pivot + 1, high)

        
        quicksort(nums, 0, len(nums)-1)
        return nums