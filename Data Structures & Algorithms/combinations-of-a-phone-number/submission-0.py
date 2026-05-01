class Solution:
    dig_map = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz'
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        opts = [Solution.dig_map[int(digit)] for digit in digits]
        counter = [0]*len(opts)

        result = []
        while True:
            result.append(''.join(opts[i][val] for i, val in enumerate(counter)))

            i = 0
            counter[i] += 1
            while counter[i] >= len(opts[i]):
                counter[i] = 0
                i += 1
                if i < len(counter):
                    counter[i] += 1
                else:
                    break
            else:
                continue
            break
        
        return result
            
