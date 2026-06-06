class Solution:

    def numDecodings(self, s: str) -> int:
        n = len(s)
        num_decodings = [0]*(n+1)

        num_decodings[-2] = 1 if s[-1] != '0' else 0
        num_decodings[-1] = 1

        print(s[-1], num_decodings)

        for i in range(n-2, -1, -1):
            if s[i] != '0':
                num_decodings[i] = num_decodings[i+1]

            if s[i] == '1' or s[i] == '2' and int(s[i+1]) < 7:
                num_decodings[i] += num_decodings[i+2]

            print(s[i], num_decodings)
        
        return num_decodings[0]

