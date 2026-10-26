#one dimensional array
arr1 = [10,20,30,40,50]
print("1D Array:")
for i in range(len(arr1)):
    print("index", i, "=", arr1[i])
    print("base address of 1D array:", id(arr1))