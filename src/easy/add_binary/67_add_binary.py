class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = len(a)
        m = len(b)
        nums = []
        if n > m:
            b = b.rjust(n, "0")
        elif n < m:
            a = a.rjust(m, "0")

if __name__ == "__main__":
    s = Solution()

    print(s.addBinary("11", "1"))
    #print(s.addBinary("1010", "1011"))
