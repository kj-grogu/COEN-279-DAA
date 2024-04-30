class IsSubsequence:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        s_ptr = t_ptr = 0
        count = 0
        while s_ptr < len(s) and t_ptr < len(t):
            if s[s_ptr] == t[t_ptr]:
                count += 1
                s_ptr += 1
            
            if count == len(s):
                return True
            
            t_ptr += 1

        return s_ptr >= len(s)
        

