def diagonalDifference(arr):
    # Write your code here
    len_ar = len(arr)-1
    left = 0
    right = len_ar
    vleft = 0
    vright = 0
    while left <= len_ar and right >= 0:
        vleft+= (arr[left][left])
        vright += arr[left][right]
        left += 1
        right -= 1
    return abs(vleft - vright)
