#Linear search of the array.  n-1 checks at most.
def linearSearch(array1, target):
    global count
    count =1
    position = 0
    while position < len(array1):
        if (array1[position]== target):
                return position
        position  = position +1
        count = count +1
    return -1
        

#Binary search of the array.  Much more efficient than linear search
def binarySearch(array1,low, high,target):
        global count
        found = False
        count = 1
        while not found and low <= high:
                middle = (high + low)// 2
                if array1[middle] == target:
                        return middle
                else: 
                        if array1[middle] > target:
                                high = middle-1
                        else:
                                low = middle+1
                count = count+1
        
        return -1

#initialize sorted non-decreasing ordered array and get length
array1 = [1,2,3,4,5,6,7,8,9]
count = 0
length = len(array1)

#Prompt user for target value and casts as an int
print('please enter the number to search for:')
target = int(input())
#error check for out of bounds checks
if target > length:
        print('target value is outside the range of the array, please enter another value:')
        target = int(input())

#calls linear search function on array and prints location of the result and the number of comparisons
lresult = linearSearch(array1, target)
print('The target is in position:', lresult)
print('Number of comparisons made:', count)

#calls binaryseach function and prints location of the result and the number of comparisons
bresult = binarySearch(array1,0, length, target)
print ('The target is in position:', bresult)
print('Number of comparisons made:', count)


    