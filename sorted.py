def sort_dictionary(input_dict):
    items = list(input_dict.items())
    n = len(items)

    # Insertion sort by age (the second element of the tuple)
    for i in range(1, n):
        key_item = items[i]
        j = i - 1
        while j >= 0 and key_item[1][1] < items[j][1][1]:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key_item

    # Create a list of tuples with names and phone numbers
    sorted_list = [(name, values[0]) for name, values in items]

    return sorted_list

myDict = {'Tom': (5464512,24), 'Sara' : (5446987, 32), 'Mary': (1557896,20)}
sorted_dict = sort_dictionary(myDict)
print(sorted_dict)