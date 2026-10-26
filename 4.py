#two_dimensional array
array = [
    [15, 8, 25],
    [40, 3, 18],
    [12, 30, 7]
]

#function to find minimum
def find_minimum(arr):
    minimum = arr[0][0]
    location = (0, 0)
    
    for i in range(len(arr)):
         for j in range(len(arr[i])):
            if arr[i][j] < minimum:
                minimum = arr[i][j]#finding the minimum in row i and column j
                location = (i, j)
    return minimum, location

#function to find maximum
def find_maximum(arr):
    maximum = arr[0][0]
    location = (0, 0)
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] > maximum:
                maximum = arr[i][j]
                location = (i, j)
    return maximum, location

#call the functions
minimum, min_location = find_minimum(array)
maximum, max_location = find_maximum(array)

#display results
print("2D array:")

for row in array:
    print(row)
    
print("\nMinimum element:", minimum)
print("Minimum location: Row", min_location[0],
      "Column", min_location[1])

print("\nMaximum element:", maximum)
print("Maximum location: Row", max_location[0],
      "Column", max_location[1])
