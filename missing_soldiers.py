# Write your code here
first_input = int(input())

adding = 0

for _ in range(first_input):
    listed = [n for n in input().split(' ')]
    adding += int(listed[2]) + 1

print(adding)

# sample input = 2, 1  1  4, 7  3  5 and sample output is 11

