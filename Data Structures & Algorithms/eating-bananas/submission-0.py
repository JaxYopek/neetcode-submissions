import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        mink = r
        while l <= r:
            hours = 0
            mid = (l + r) // 2
            for p in piles:
                hours += math.ceil(p / mid)
            if  hours <= h:
                mink = min(mink,mid)
                r = mid - 1
            else:
                l = mid + 1
        return mink
            