# Sorting Algorithms
# sort a list of numbers in increasing order
# input 
[4, 2, 6, 3, 4, 6, 2, 1]
# output
[1, 2, 2, 3, 4, 4, 6, 6]

# scenario
# some lists of numbers in random order
# a list that already sorted
# a list that's sorted in descending order
# a list containing repeating elements
# an empty list
# a list containing just one element
# a list containing one element repeated many times
# a realy long list

test0 = {
    'input': {
        'nums': [4, 2, 6, 3, 4, 6, 2, 1]
        },
        'output': [1, 2, 2, 3, 4, 4, 6, 6]
}

test1 = {
    'input': {
        'nums': [5, 2, 6, 1, 23, 7, -12, 12, -243, 0]
    },
    'output': [-243, -12, 0, 1, 2, 5, 6, 7, 12, 23]
}

test2 = {
    'input': {
        'nums': [3, 5, 6, 8, 9, 10, 99]
    },
    'output': [3, 5, 6, 8, 9, 10, 99]
}

test3 = {
    'input': {
        'nums': [99, 10, 9, 8, 6, 5, 3]
    },
    'output': [3, 5, 6, 8, 9, 10, 99]
}

test4 = {
    'input': {
        'nums': [5, -12, 2, 6, 1, 23, 7, 7, -12, 6, 12, 1, -243, 1, 0]
    },
    'output': [-243, -12, -12, 0, 1, 1, 1, 2, 5, 6, 6, 7, 7, 12, 23]
}

test5 = {
    'input': {
        'nums': []
    },
    'output': []
}

test6 = {
    'input': {
        'nums': [23]
    },
    'output': [23]
}

test7 = {
    'input': {
        'nums': [42, 42, 42, 42, 42, 42, 42]
    },
    'output': [42, 42, 42, 42, 42, 42, 42]
}

import random
in_list = list(range(10000))
out_list = list(range(10000))
random.shuffle(in_list)

test8 = {
    'input': {
        'nums': in_list
    },
    'output': out_list
}

test = [test0,test1,test2,test3,test4,test5,test6,test7,test8]

# Solution
# bubble sort
# 1.Iterate over the list of numbers, starting from the left
# 2.compare each number with the number that follows it
# 3.if the number is greater than the one that follows it, swap the two elements
# 4.repeat steps 1 to 3 till the list is sorted


def bubble_sort(nums):
    nums = list(nums)

    # repeat the process n-1 times
    for _ in range(len(nums) - 1):

        # iterate over the array(expect last element)
        for i in range(len(nums) - 1):

            # compare the numbers
            if nums[i] > nums[i + 1]:

                # swap the two elements
                nums[i], nums[i+1] = nums[i+1], nums[i]
    
    return nums

nums0, output0 = test0['input']['nums'], test0['output']

result0 = bubble_sort(nums0)
result0 == output0

# complexity
# (n-1)*(n-1)
# (n-1)^2
# n^2 - 2n + 1


# Insertion sort
# we keep the initial portion of the array sorted
# insert the remaining elements one by one at the right position

# keep the initial portion at the initial place
# compare the next right element with initial portion
# if the next right element greater, stay
# if the next right element is smaller, insert to the front

def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i - 1
        while j>=0 and nums[j]>cur:
            j -= 1
        nums.insert(j+1, cur)
    return nums
num0, output0 = test0['input']['nums'], test0['output']
insertion_sort(nums0)
result0 == output0


# Divide and Conquer
# 1.divide the inputs into two roughly equal parts
# 2.recursively solve the problem individually for each of the two parts
# 3.combine the results to solve the problem for original inputs
# 4.include terminating conditions for small or indivisible inputs
# solution
# 1.if the input list is empty or contain just one element, it is already sorted, return it
# 2.if not, divide the list of numbers into two roughly equal parts
# 3.sort each part recursively using the merge sort algorithm
# get back two sorted list
# 4.merge the two sorted lists to get a single sorted list

def merge_sort(nums):
    # Terminating condition(list of 0 or 1 elements)
    if len(nums) <= 1:
        return nums

    # Get the midpoint
    mid = len(nums) // 2

    # Split the list into two halves
    left = nums[:mid]
    right = nums[mid:]

    # solve the problem for each half recursively 
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)

    # Combine the results of the two halves
    sorted_nums = merge(left_sorted, right_sorted)

    return sorted_nums
# to merge two sorted array, we can repeatedly compare the two least
# elements of each array, and copy over the smallest one into a new array
def merge(nums1, nums2):
    # list to store the results
    merged = []

    # Indices for iteration
    i, j = 0, 0

    # Loop over the two lists
    while i<len(nums1) and j<len(nums2):
        
        # Include the smaller element in the result and move to next element
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    
        
    # get the remaining parts
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]

    return merged + nums1_tail + nums2_tail

merge([1, 4, 7, 9, 11], [-1, 0, 2, 3, 8, 12])

nums0, output0 = test0['input']['nums'], test0['output']
result0 = merge_sort(nums0)
result0 == output0
# complexity


# Quick sort
# 1.if the list is empty or has just one element, return it
# 2.pick a random element from the list. it's called pivot
# 3.reorder the list so that all elements with values less than or
# equal to the pivot come before the pivot, while all elments with
# values greater than the pivot come after it
# this operation is partitioning
# 4.the pivot element divides the array into two parts which can be 
# sorted independently by making a recursive call to quicksort
def quicksort(nums, start=0, end=None):
    if end is None:
        nums = list(nums)
        end = len(nums) - 1

    if start < end:
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot-1)
        quicksort(nums, pivot+1, end)
    return nums
# when left > pivot and right < pivot, swap
# otherwise, keep traversing
def partition(nums, start=0, end=None):
    if end is None:
        end = len(nums) - 1

    # Initialise right and left pointers
    l, r = start, end - 1

    # Iterate while they're apart
    while r > l:
        # Increment left pointer if number is less or equal to pivot
        if nums[l] <= nums[end]:
            l += 1
        # Discrement right pointer if number is greater than pivot
        elif nums[r] > nums[end]:
            r -= 1
        # Two out-of-place elements found, swap them
        else:
            nums[l], nums[r] = nums[r], nums[l]
    
    # Place the pivot between the two parts
    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else:
        return end
l1 = [1, 5, 6, 2, 0, 11, 3]
pivot = partition(l1)

nums0, output0 = test0['input']['nums'], test0['output']
quicksort(nums0)