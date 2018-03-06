class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if (n == 0):
            return 1 % d
        ans = 1
        base = x;
        while (n > 0):
            if (n % 2 == 1):
                ans = (ans * base) % d
                n=n-1
            else:
                base = (base * base) % d
                n =n/ 2
        
        if (ans < 0):
            ans = (ans + d) % d
        return ans
                
