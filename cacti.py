def cacti_number(func):
    def wrapper(arr):
        count = 0
        rows = len(arr)
        cols = len(arr[0])
        
        FIRST_ROW, FIRST_COL = 0
        LAST_ROW = rows - 1
        LAST_COL = cols - 1
        
        for i in range(rows):
            for j in range(cols):
                if i == FIRST_ROW:
                    if j == FIRST_COL:
                        if arr[i][j] == 1:
                            continue
                        else:
                            if arr[i+1][j] == 0 and arr[i][j+1] == 0:
                                count += 1
                            else:
                                continue
                    elif j == LAST_COL:
                        pass
                            
                print(arr[i][j], end=' ')
            print()
        return count
    return wrapper(func)

def print_arr(arr):
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            print(arr[x][y], end=' ')
        print()
    print('------------')
    
def cacti_number2(plot):
    def wrapper(arr): 
        prev_count = 0
        count = 0
        rows = len(arr)
        cols = len(arr[0])

        FIRST_ROW = 0
        FIRST_COL = 0
        LAST_ROW = rows - 1
        LAST_COL = cols - 1
        
        print_arr(arr)
        for i in range(rows):
            for j in range(cols):
                if arr[i][j] == 1:
                    continue
                else:
                    if i > 0 and j > 0 and i < LAST_ROW and j < LAST_COL:
                        if arr[i-1][j] == 1 or arr[i][j-1] == 1 or arr[i+1][j] == 1 or arr[i][j+1]:
                            continue
                        else:
                            count += 1
                            arr[i][j] = 1
                    # First row
                    elif i == FIRST_ROW and j == FIRST_COL: # First row and column
                        count += 1
                        arr[i][j] = 1
                    elif i == FIRST_ROW and j == LAST_COL:
                        if arr[i][j-1] == 0 and arr[i+1][j] == 0:
                            count += 1
                            arr[i][j] = 1
                    # Middle rows
                    elif i == LAST_ROW and j == FIRST_COL:
                        if arr[i-1][j] == 0 and arr[i][j+1] == 0:
                            count += 1
                            arr[i][j] = 1
                    # Last rows
                    elif i == LAST_ROW and j == LAST_COL:
                        if arr[i-1][j] == 0 and arr[i][j-1] == 0:
                            count += 1
                            arr[i][j] = 1
                            
                # Print the array when the count changes
                if prev_count != count:
                    print_arr(arr)  
                prev_count = count
        return count

    return wrapper(plot)

def main():
    # plot = [ [1, 0, 1, 0, 1],
            #  [0, 0, 0, 0, 0],
            #  [1, 0, 0, 0, 0] ]

    plot = [ [0, 1, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0],
             [1, 0, 1, 0, 0, 1] ]
    print(f"count = {cacti_number2(plot)}")

main()