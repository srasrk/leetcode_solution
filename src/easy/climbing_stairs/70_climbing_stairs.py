class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 2
        if n == 1:
            return a
        for i in range(3, n+1):
            a, b = b, a + b  
        return b


if __name__ == "__main__":
    solution = Solution()
    n = 1
    result = solution.climbStairs(n)
    print(f"Number of distinct ways to climb {n} stairs: {result}")