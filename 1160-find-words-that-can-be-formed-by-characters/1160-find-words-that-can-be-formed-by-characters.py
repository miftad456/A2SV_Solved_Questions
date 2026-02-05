class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import Counter
        targets  = Counter(chars)
        def can_it(x):
            check  =  Counter(x)
            for i in check:
                if i not in targets:
                    return False
                elif i in targets and check[i] > targets[i]:
                    return False
            else:
                return True
        result  = 0
        for i in range(len(words)):
            if can_it(words[i]):
                result += len(words[i])
        return result


        