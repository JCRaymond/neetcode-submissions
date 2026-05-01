class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f'{len(s)}|{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        strs = []
        while len(s) > 0:
            s_len, _, s = s.partition('|')
            s_len = int(s_len)
            strs.append(s[:s_len])
            s = s[s_len:]
        return strs