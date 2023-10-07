def merge_list(list1, list2):
    new_list = []
    new_list.extend(list1)
    new_list.extend(list2)

    for i in range(len(new_list)):
        if not isinstance(new_list[i], int):
            raise TypeError("All elements must be integers")
        smallest_idx = i
        for j in range(i + 1, len(new_list)):
            if new_list[smallest_idx] > new_list[j]:
                smallest_idx = j
        new_list[i], new_list[smallest_idx] = new_list[smallest_idx], new_list[i]
    return new_list

'''
list1 = [1,'a',9,11]
list2 = [2,4,3,1]
print("Input:  ", list1, ",", list2)
sorted_list = merge_list(list1, list2)
print(list1)
print("Output: ", sorted_list)
'''