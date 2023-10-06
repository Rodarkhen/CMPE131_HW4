def merge_list(list1, list2):
    if not all(isinstance(item, int) for item in list1) or not all(isinstance(item, int) for item in list2):
        raise TypeError("All elements in both input lists must be integers")

    new_list = []
    new_list.extend(list1)
    new_list.extend(list2)

    for i in range(len(new_list)):
        smallest_idx = i
        for j in range(i + 1, len(new_list)):
            if new_list[smallest_idx] > new_list[j]:
                smallest_idx = j
        new_list[i], new_list[smallest_idx] = new_list[smallest_idx], new_list[i]
    return new_list


'''
list1 = [1,5,9,11]
list2 = [2,4,3,1]
print("Input:  ", list1, ",", list2)
sorted_list = merge_list(list1, list2)
print(list1)
print("Output: ", sorted_list)
'''