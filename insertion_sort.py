def insertion_sort(array, n):
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
    return array
user_input = input("Enter numbers to be sorted (space-separated): ")
input_numbers = user_input.split()
numbers = []
for num in input_numbers:
    numbers.append(int(num))

