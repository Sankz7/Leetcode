

arr = [-4,-1,0,3,10]

arr2 = [0] * len(arr)

if not arr:
    print("invalid")

i = 0
j = len(arr) - 1

k = len(arr2) - 1

while i < len(arr):
    if i > j:
        print("stop", arr2)
        break

    # if abs(arr[i]) == abs(arr[j]):
    #     arr2[k] = arr[i] * arr[i]
    #     k = k - 1
    #     arr2[k] = arr[i] * arr[i]
    #     k = k - 1


    if abs(arr[i]) > abs(arr[j]):
        arr2[k] = arr[i] * arr[i]
        k = k - 1
        i = i + 1

    else:
        arr2[k] = arr[j] * arr[j]
        k = k - 1
        j = j - 1


print(arr2)