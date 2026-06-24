class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = list(s)
        list_t = list(t)
        result = collections.Counter(list_s) == collections.Counter(list_t)
        if result:
            return True
        else :
            return False    