class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        Sorting + Two pointers: O(nlogn)
        Greedy algorithm: Heaviest person is the hardest to place
        If they can be paired with the lightest, they must be alone
        """
        people.sort()
        count = 0
        l, r = 0, len(people) - 1

        # Use l <= r when single element is processed (Search, Single index matters)
        while l <= r:
            remain = limit - people[r]
            r -= 1
            count += 1
            if l <= r and people[l] <= remain:
                l += 1
        return count
