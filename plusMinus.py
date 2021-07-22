def plusMinus(arr):
    # Write your code here
    zero_idx = binary_search(arr.sort())
    if zero_idx[0] == 0:
        negative = (zero_idx - 1)/len(arr)
        positive = (len(arr) - zero_idx+1)/len(arr)
        print("%.6f", positive)
        print("%.6f", 1/len(arr))
        print("%.6f", negative)
    else:
        negative = (zero_idx)/len(arr)
        positive = (len(arr) - zero_idx+1)/len(arr)
        print("%.6f", positive)
        print(0)
        print("%.6f", negative)
def binary_search(arr):
    mid = len(arr)//2
    left = 0
    right = len(arr)
    last_change_idx = -1
    if arr[mid] == 0:
            return mid
    while not last_change_idx == mid:
        if arr[mid] < 0:
            lef = mid
            last_change_idx = mid
            mid =  (right + mid)//2
            
        elif arr[mid] > 0:
            right = mid
            last_change_idx = mid
            mid = (mid-left)//2
    if arr[mid] == 0:
        return [0, mid]
    return [1, mid]  
