class Solution:
    def isHappy(self, n: int) -> bool:
        digits = [int(x) for x in str(n)]
        curSum = 0
        seenSums = set()
        while 1:
            for digit in digits:
                curSum += digit*digit
            if curSum in seenSums:
                return False
            seenSums.add(curSum)
            if curSum == 1:
                return True
            digits = [int(x) for x in str(curSum)]
            curSum = 0


class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        slow = self.squaredSum(n)
        fast = self.squaredSum(self.squaredSum(n))

        while fast != slow and fast != 1 and slow != 1:
            slow = self.squaredSum(slow)
            fast = self.squaredSum(self.squaredSum(fast))
        return False if fast == slow and fast != 1 else True
    
    def squaredSum(self, n: int) -> int:
        return sum([int(x) ** 2 for x in str(n)])