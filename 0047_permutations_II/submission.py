class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        for n in nums:
            ret = [
                    l[:i]+[n]+l[i:]
                        for l in ret
                        for i in range((l+[n]).index(n)+1)
                ]
        return ret
