class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        res = 0
        for j in range(1, n - 1):
            less_left = sum(rating[i] < rating[j] for i in range(j))
            greater_left = j - less_left
            less_right = sum(rating[j] < rating[k] for k in range(j + 1, n))
            greater_right = n - j - 1 - less_right
            res += less_left * less_right + greater_left * greater_right
        return res
