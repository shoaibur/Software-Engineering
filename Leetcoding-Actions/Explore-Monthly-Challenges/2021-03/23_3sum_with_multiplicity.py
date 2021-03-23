class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        ans = 0
        arr.sort()

        for i, x in enumerate(arr):
            # We'll try to find the number of i < j < k
            # with A[j] + A[k] == T, where T = target - A[i].

            # The below is a "two sum with multiplicity".
            T = target - arr[i]
            j, k = i+1, len(arr) - 1

            while j < k:
                # These steps proceed as in a typical two-sum.
                if arr[j] + arr[k] < T:
                    j += 1
                elif arr[j] + arr[k] > T:
                    k -= 1
                # These steps differ:
                elif arr[j] != arr[k]: # We have A[j] + A[k] == T.
                    # Let's count "left": the number of A[j] == A[j+1] == A[j+2] == ...
                    # And similarly for "right".
                    left = right = 1
                    while j + 1 < k and arr[j] == arr[j+1]:
                        left += 1
                        j += 1
                    while k - 1 > j and arr[k] == arr[k-1]:
                        right += 1
                        k -= 1

                    # We contributed left * right many pairs.
                    ans += left * right
                    ans %= MOD
                    j += 1
                    k -= 1

                else:
                    # M = k - j + 1
                    # We contributed M * (M-1) / 2 pairs.
                    ans += (k-j+1) * (k-j) // 2
                    ans %= MOD
                    break

        return ans
