def list_average(li):

    result = 0

    for num in li:

        result = result + num / len(li)

    return result

result = list_average([2, 1, 4, 3, 5])

print("Average list result is:",result)


