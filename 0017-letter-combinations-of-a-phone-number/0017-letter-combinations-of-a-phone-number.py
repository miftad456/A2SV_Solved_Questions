class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        from itertools import product
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def letter_combinations(digits):
            if not digits:
                return []
            
            letters_list = [digit_map[d] for d in digits]
            
            combinations = [''.join(comb) for comb in product(*letters_list)]
            
            return combinations


        return letter_combinations( digits)
                