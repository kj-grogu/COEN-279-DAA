class Solution:
    def minSwaps(self, data: List[int]) -> int:
        sum_k = sum(data)
        n = len(data)

        cur_sum = sum(data[:sum_k])
        ans = cur_sum

        for i in range(sum_k, n):
            cur_sum += data[i] - data[i - sum_k]
            ans = max(cur_sum, ans)

        return sum_k - ans
