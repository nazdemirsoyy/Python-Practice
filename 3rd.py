c0 = int(input("Enter a non-negative, non-zero integer number: "))

while c0 <= 0:
    print("Invalid input. Please enter a non-negative, non-zero integer number.")
    c0 = int(input("Enter a non-negative, non-zero integer number: "))

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    print(c0)


## LIST
list = ["1", "2", "3"]
# print(list)
list.append("5")
# print(list) # ['1', '2', '3', '5']

list.extend([4, 5, 6])
for i in range(7, 9):
    list.append(i)
#print(list)

any_list = [1,2,4,5,6,9]
any_list.pop()
#print(any_list)

beatles= []
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

#use for loop to append
for i in range(2):
    user_name= input("Enter a user name: ")
    beatles.append(user_name)

print(beatles) # See the changes before delition


# use the del to remove Stu Sutcliffe and Pete Best from the list
del beatles[3]
del beatles[3]

print(beatles)

# Use the insert() method to add Ringo Starr to the beggining of the list
beatles.insert(0,"Ringo Starr")

print(beatles)

 
# Find the uniqiue elems in a list and remove
list3 = [1, 2, 2, 3, 4, 4, 5, 6, 6]

# Initialize an empty list to store the unique elements
unique_elems = []

# Loop through each element in the list
for elem in list3:
    # Check if the element is not already in the unique_elems list
    if elem not in unique_elems:
        # If it's not, add it to the unique_elems list
        unique_elems.append(elem)

# Loop through each unique element in the list
for elem in unique_elems:
    # Remove the element from the original list
    list3.remove(elem)

# Print the updated list without the unique elements
print(list3)



