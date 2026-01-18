tests = int(input())

for _ in range(tests):
    array_len = int(input())
    
    arrays = []
    min_element = float("inf")
    for _ in range(array_len):
        _ = input()
        arr_str = input()
        arr = [int(elem) for elem in arr_str.split()]
        
        arr.sort()
        min_element = min(min_element, arr[0])
        arrays.append(arr[1])

    # print(arrays)
    arrays.sort()
    arrays[0] = min_element
    print(sum(arrays))

"""
num cases

2 <- number of arrays in the list
2 <- num elements in array 
1 2
2 <- num elements in array 
4 3

[[1, 2], [4, 3]]

maximize the array
we can only move at most one

Greedy - try to increase each array

case 2

3
[100 1 6]

Each array will give up  their min and we want to maximize that value..

increase the min in each array..

sort each array

[2], [4]

[1, 3]
 ^

3

[[1, 100], [3, 4], [5, 6]]
When we give a element away it increase my array to the next greatest element
but it might also shrink who you send the element to





[10000000],    [2, 5, 6, 7, 1001, 1007], [6, 8, 11]
 ^                                    

 1000000 + 2 + 6


choose the one that will increase 

move all the mins out.. 

that def give us the max result.. we need to redistrubute it..

move it 

to the one with the smallest second

2, 7, 1001, 1007

8 11

9

2, 5, 6

"""