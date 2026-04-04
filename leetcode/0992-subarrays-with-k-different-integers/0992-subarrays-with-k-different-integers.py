class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def check(k):
            hashMap = Counter()
            left  = 0
            right  = 0
            answer  = 0
            for right in range(len(nums)):
                hashMap[nums[right]] += 1
                while len(hashMap) > k:
                    hashMap[nums[left]] -= 1
                    if hashMap[nums[left]] == 0:
                        del hashMap[nums[left]]
                    left += 1
                answer +=  (right - left +  1)
            return answer 
        return check(k)  - check(k - 1)
            