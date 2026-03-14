# coded by Zenet

def bouncy_number():
    num = int(input("Enter a number "))
    while num < 0:
        num = int(input("Enter a number "))

    if num < 10:
        return "number is not bouncy"

    num_list = [int(n) for n in str(num)]

    increasing_count = 0
    decreasing_count = 0
    equal_count = 0

    for index in range(1, len(num_list)):
        if num_list[index] < num_list[index - 1]:
            decreasing_count += 1
        elif num_list[index] > num_list[index - 1]:
            increasing_count += 1
        elif num_list[index] == num_list[index - 1]:
            equal_count += 1

    if (increasing_count + equal_count == (len(num_list) - 1)
            and decreasing_count + equal_count == (len(num_list) - 1)):
        return "number is a increasing and decreasing number"

    if increasing_count + equal_count == (len(num_list) - 1):
        return "number is an increasing number"

    elif decreasing_count + equal_count == (len(num_list) - 1):
        return "number is a decreasing number"

    elif increasing_count == decreasing_count:
        return "number is perfectly bouncy"

    else:
        return "number is bouncy"

message = bouncy_number()
print(message)
