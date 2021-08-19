class Solution:
    def permuteUnique(self, nums) :
        n = len(nums)
        res = []
        path = []
        nums.sort()
        def backtrack(used):
            if used == (1 << n) -1:
                res.append(path[:])
                return
            for i in range(n):
                if used & (1 << i) or (i > 0 and nums[i] == nums[i-1] and not used & (1 << (i-1))):
                    continue
                path.append(nums[i])
                backtrack(used | (1 << i))
                path.pop()
        backtrack(0)
        return res

nums=[1,1,3]
test=Solution()
print(test.permuteUnique(nums))

