arr = [10,20,30,40,50]
#Tranversal- It means to visit each element one by one.
print("Array element:")
for element in arr:
    print(element)
    
#searching-it means to find the element in the array.
search = 30
if search in arr:
    print(search, "was found")
else:
    print(search, "was not found")
    
#updating- I means to change the value of an elememnt in the array.
arr[2] = 35
print("After updating:", arr)

#insertion- It means to add a new element in the array
arr.append(60)
print("After insertion:", arr)

#deletion- It means to remove an element from the array.
arr.remove(20)
print("After deletion:", arr)

#sorting- It means to arrange the elements of an array in a particular order.
arr.sort()
print("After sorting:", arr)            