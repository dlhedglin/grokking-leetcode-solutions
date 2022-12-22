class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        a = 0
        b = 0
        while a < len(firstList) and b < len(secondList):
            print(a,b)
            head1 = firstList[a]
            head2 = secondList[b]

            if head1[1] >= head2[0]:
                ## intersect
                newPair = [max(head1[0], head2[0]), min(head2[1], head1[1])]
                if newPair[0] <= newPair[1]:
                    res.append(newPair)
            
            if b < len(secondList) - 1 and secondList[b+1][0] <= head1[1]:
                b += 1
            elif a < len(firstList) - 1 and firstList[a+1][0] <= secondList[b][1]:
                a += 1
            else:
                b+=1
                a+=1
        return res