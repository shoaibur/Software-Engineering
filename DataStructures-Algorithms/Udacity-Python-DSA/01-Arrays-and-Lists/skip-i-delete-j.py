def skip_i_delete_j(nums, i, j):
    ii, jj = 0, 0
    for num in nums:
        if ii < i:
            out.append(num)
            ii += 1
            jj = 0
        if ii == i:
            jj += 1
        if jj == j+1:
            ii = 0
    return out
