class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """ Hashmap + Sorting: O(n logn), O(n)
        1. Sort + count each number
        2. Iterate every num
        3. If count[num] > 0, start checking new group of size k (since it's not assigned)
        4. For i in (num, num + k), if count[i] = 0, can't form group -> return False
        5. count[i] -= 1 for every group assign
        """
        n = len(hand)
        k = groupSize
        if n % k != 0:
            return False
        
        hand.sort()
        # Counter(list) auto return 0 if key is missing
        count = Counter(hand)
        
        for num in hand:
            # only start new group if num is unused
            if count[num]:
                for i in range(num, num + k):
                    # mising number needed to form group
                    if not count[i]:
                        return False
                    count[i] -= 1
        return True