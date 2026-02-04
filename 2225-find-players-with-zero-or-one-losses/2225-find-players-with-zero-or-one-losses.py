class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner =  {}
        loser  =  {}
        for win , los in matches:
            if win in winner:
                winner[win]+=1
            else:
                winner[win] = 1
            if los in  loser:
                loser[los]+=1
            else:
                loser[los] =1
        res =  []
        for i in winner :
            if i not in loser:
                res.append(i)
        rest = []
        for i in loser:
            if loser[i]==1:
                rest.append(i)
        res.sort()
        rest.sort()
        return [res,rest]

        