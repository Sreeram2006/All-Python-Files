#FOR LOOPS IN PYTHON: Iterate items over a collection of a string
for item in "Python":
    print(item)
#Range function in for Loop:
for z in range(10):
    print(z)
for a in range(5,10):
    print(a)


#IMAGINARY SHOPPING CART:
prices= [10,20,30]
total=0
for price in prices:
    total+=price
print(f"Total is { total }")


#nested loops:
#generate co-ordinates:
for i in range(4):
    for y in range(3):
        print(f"({i}, {y})")

#making F-shape:
numbers= [5,2,5,2,2]
for x_count in numbers:
    print('x'* x_count)

#second way:
nos=[5,2,5,2,2]
for y_coun in nos:
    output=''
    for coun in range(y_coun):
        output+='x'
    print(output)


