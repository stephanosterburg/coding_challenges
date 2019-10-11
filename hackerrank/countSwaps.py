def countSwaps(a):
    count = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                count += 1

    print("Array is sorted in {} swaps.".format(count))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))


a = [6,4,1]
countSwaps(a)

a = [1, 2, 3]
countSwaps(a)
