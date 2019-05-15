def li_average(li):

    result = 0

    for number in li:

        result = result + number / 2

    return result

result = li_average([2, 4, 1, 6, 8, 10])

print("Average result of list:", result)


