power = [3,8,9,7]
mini,maxi = 0,0

for i in power:
    if mini == 0 and maxi == 0:
        mini = i
        maxi = i
    if i < mini:
        mini = min(i, mini)
    if i > maxi:
        maxi = max(i, maxi)
    print(f"Min: {mini}, Max: {maxi}")


def power(base, exponent):
    if(exponent==0):
        return 1
    else:
        return base * power(base, exponent-1)
    
print(power(2, 3))  # Output: 8

def mergeSort(arr):
    if(len(arr)>1):
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        l = r = k = 0

        while l < len(L) and r < len(R):
            if L[l] < R[r]:
                arr[k] = L[l]
                l += 1
            else:
                arr[k] = R[r]
                r += 1
            k += 1

        while l < len(L):
            arr[k] = L[l]
            l += 1
            k += 1

        while r < len(R):
            arr[k] = R[r]
            r += 1
            k += 1

arr = [8,2,9,5,3,4,7,6,1]
mergeSort(arr)
print("Sorted array is:", arr)

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)