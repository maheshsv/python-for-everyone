largest = None
smallest = None
while True:
    input_value = input("Enter a number: ")
    if input_value == "done" : break
    try:
        num = int(input_value)
    except Exception as e:
        print("Invalid Input")
        continue


    if largest is None and smallest is None:
        largest = num
        smallest = num
    if num > largest :
        largest = num
    if num  < smallest :
        smallest = num


print("Maximum is", largest)
print("Minimum is", smallest)
