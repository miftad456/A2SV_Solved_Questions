class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) % 2  !=  0:
            return -1
        else:
            skill.sort()
            left =  0
            right    =  len(skill)-1
            product  =  1
            check  =  skill[right] + skill[left]
            while right  > left :
                if skill[right] + skill[left] !=  check:
                    return -1
                else:
                    product  +=  skill[right] * skill[left] 
                    left +=1
                    right -=1
            return product - 1
                
        