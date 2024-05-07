def selection_sort(arr):
    for i in range(len(arr) - 1):
        index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[index]:
                index = j
        arr[index], arr[i] = arr[i], arr[index]

if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = []
    print("Enter elements:")
    for _ in range(n):
        arr.append(int(input()))

    print("Before Selection Sort:")
    print(*arr)

    selection_sort(arr)

    print("After Selection Sort:")
    print(*arr)

