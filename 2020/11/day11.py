"""
"""

import timeit
import numpy as np


def read():
    with open('input.txt') as f:
        return f.read().splitlines()

def part1(arr):
    height, width = arr.shape

    arr2 = arr.copy()
    for x in range(1, height - 1):
        for y in range(1, width -1):
            # positions to slice relative to our current position
            top_x, top_y = x - 1, y - 1
            bot_x, bot_y = x + 2, y + 2
            
            # test_arr is all the adjacent points with our
            # current point in the center of a 3 x 3 array
            test_arr = np.copy(arr[top_x:bot_x, top_y:bot_y])
            test_arr[1,1] = 'X'
            
            if arr[x,y] == 'L':
                if np.sum(test_arr == '#') == 0:
                    arr2[x,y] = '#'
            
            if arr[x,y] == '#':
                if np.sum(test_arr == '#') >= 4:
                    arr2[x,y] = 'L'

    print('Count: ', np.sum(arr2 == '#'))            
    # print_arr(arr2)       
 
    return arr2 

def print_arr(arr):
    # printing the array so we can validate against example
    height, width = arr.shape
    for x in range(1, height - 1):
        for y in range(1, width -1):
            print(arr[x,y], end='')
        print()
    print()

def main():
    lst = []
    for line in read():
        # line = line
        lst.append([x for x in line])
    arr = np.array(lst)

    # padding all sides of the array so slicing in my loop works
    arr = np.pad(arr,(1,1),'constant', constant_values=('Z','Z'))

    counter = 0
    while True:
        arr_last = arr.copy()
        arr = part1(arr)

        # Eventually array stablizes and the Count of # remains constant,
        # so no need to loop forever        
        counter += 1
        if counter >=100:
            break

if __name__ == '__main__':
    print(timeit.timeit(main, number=1), 'seconds')