# Insertion and deletion of a Array


n = int(input("Enter the array size : "))

arr = [0]*(n + 1)

for i in range(n):
    arr[i] = int(input("Enter the  element : "))

print("Original array:", arr[:n])

print("1. Insertion")
print("2. Deletion")
choice = int(input("Enter your choice : "))

if choice == 1:
    element = int(input("Enter element to insert : "))
    position = int(input("Enter position : "))

    if position < 0 or position > n:
        print("Invalid position")
    else:
        i = n
        while i > position:
            arr[i] = arr[i - 1]
            i = i - 1

        arr[position] = element
        n = n + 1

        print("Array after insertion:", arr[:n])

elif choice == 2:
    position = int(input("Enter position to delete : "))

    if position < 0 or position >= n:
        print("Invalid position")
    else:
        i = position
        while i < n - 1:
            arr[i] = arr[i + 1]
            i = i + 1

        n = n - 1
        print("Array after deletion :", arr[:n])

else:
    print("Invalid choice")


