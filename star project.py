print("Hello world!")
x=2
y=7

print(x**y)
count = 0
print("t\t\Triangle")

for x in range(1 , 7):
    for y in range (7  - x):
        print ("", end = "")
    for y in range(1, x ):
        print("*", end = "")
    for y in range (x, 0, -1):
        print("*", end = "")

    print("\n")

userInput = int(input("*"))

row = 2
while(row < userInput):
    row += 1
    spaces = userInput - row

    spaces_counter = 0
    while(spaces_counter < spaces):
        print("*", end ='')
        spaces_counter += 1

    num_stars = 2*row-1
    while(num_stars > 0):
        print("*", end ='')
        num_stars -= 1

print()