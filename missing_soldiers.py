# Write your code here
# Take this algorithm
# For any input of x, y and d
# Calculate the range of possible x points within
# Append the range to a list
# Finally count the non-recurring points #


list_of_x_points = []

for _ in range(int(input())):
    listed = list(input().split(' '))
    for val in range(int(listed[0]), int(listed[2]) + int(listed[0]) + 1):
        if val not in list_of_x_points:
            list_of_x_points.append(val)


print(len(list_of_x_points))

