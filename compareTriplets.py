def compareTriplets(a, b):
    # Write your code here
    bob = 0
    alice = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            bob+=1
        elif a[i] < b[i]:
            alice +=1
    return [bob, alice]
