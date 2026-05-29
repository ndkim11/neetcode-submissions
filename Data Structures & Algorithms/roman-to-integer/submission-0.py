class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        "III" = (1+1+1)
        "XLIX" = (50-10) + (10-1)
        '''
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        l = len(s)
        i = 0
        t_sum = 0
        while i < l:
            if i<l-1 and d[s[i]]<d[s[i+1]]: # Not last and is smaller than succesive item
                t_sum += (d[s[i+1]]-d[s[i]])
                i += 2
            
            else: # 1.i==n-1 2.s[i]>s[i+1]
                t_sum += d[s[i]]
                i += 1

        return t_sum
