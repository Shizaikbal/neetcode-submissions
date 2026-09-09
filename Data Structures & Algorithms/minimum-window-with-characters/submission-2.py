class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = defaultdict(int)
        window = defaultdict(int)

        res = [-1, -1]
        resLen = float('inf')

        for ch in t:
            countT[ch] += 1

        have = 0
        need = len(countT)

        l = 0
        for r in range(len(s)):
            ch = s[r]
            window[ch] += 1

            if ch in countT and countT[ch] == window[ch]:
                have += 1

            while have == need:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r-l+1

                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1

        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""



            