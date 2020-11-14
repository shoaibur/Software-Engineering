# Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a 
# researcher, write a function to compute the researcher's h-index.
# According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N 
# papers have at least h citations each, and the other N − h papers have no more than h citations each."

def hIndex(self, citations: List[int]) -> int:
    # O(log n)
    n = len(citations)
    lo, hi = 0, n-1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if citations[mid] < n - mid:
            lo = mid + 1
        else:
            hi = mid - 1
    return n - lo
