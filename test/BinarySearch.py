

# Linear Search
# find the location of query

input = [13, 1, 10, 7, 4, 3, 1, 0]
query = 7
output = 3



# solution:
def locate_card(cards, query):
    pass
# way to test the solution
test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}
test['input']

locate_card(**test['input'])==test['output']



# creat different senarios
test = []
# query occurs in the middle
test.append(
    {'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
     'output': 6
    }
)
# query is the first element
test.append(
    {'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
     'output': 0
    }
)
# query is the last element
test.append(
    {'input':{
        'cards': [3, -1, -9, -127],
        'query': -127
    },
     'output': 3
    }
)
# cards contains just one element 
test.append(
    {'input':{
        'cards': [6],
        'query': 6
    },
     'output': 0
    }
)
# cards does not contain query
test.append(
    {'input':{
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
     'output': -1
    }
)
# cards is empty
test.append(
    {'input':{
        'cards': [],
        'query': 7
    },
     'output': -1}
)
# numbers can repeat in cards
test.append(
    {'input':{
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
     'output': 7}
)
# query occurs multiple times
test.append(
    {'input':{
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
     'output': 2}
)
test

# linear search algorithm
# 1.create a variable position with the value 0
# 2.check whether the number at index position in card equals quary
# 3.if it does, position is the answer and can be returned from the function
# 4.if not, increment the value of position by 1, and repeat steps 2 to 5 till we reach the last position
# 5.if the number was not found, return -1

def locate_card(cards, query):
    # create a variable postion with the value 0
    position = 0

    # set up a loop for repetition
    while True:
        # check if element at the current position match the query
        if cards[position] == query:
            return position
        # increment the postion
        position += 1

        # check if we have reached the end of array
        if position == len(cards):
            return -1


result = locate_card(test[0]['input']['cards'],test[0]['input']['query'])
result == test[0]['output']


from jovian.pythondsa import evaluate_test_cases


evaluate_test_cases(locate_card, test)

cards5 = test[5]['input']['cards']
query5 = test[5]['input']['query']
cards5
query5

len(cards5)

def locate_card(cards, query):
    position = 0
    # if index is in the range
    while position < len(cards):
        if cards[position] ==query:
            return position
        position += 1
    # if index out of range
    return -1

test[5]

locate_card(cards5,query5)

evaluate_test_cases(locate_card, test)


# complexity and big O notation

# The time complexity of algorithm is cN 
# for fixed constant c
# that depends on the number of operations we perform in each iteration
# and the time taken to execute a statement

# The space complexity is some constant c(independent of N)
# it occupies a constant space in the computer's memory(RAM)

# Big O notation
# worst case complexity
# drop fixed constants and lower powers of variables
# to capture the trend of relationship
# between the size of input and the complexity of the algorithm
# the time complexity of linear search is O(N)
# space complexity is O(1)


# Binary Search

# Find the middle element of the list
# if it matches queried number, return the middle position as the answer
# if it is less than the queried number, then search the first half of the list
# if it is greater than the queried number, then search the second half of the list
# if no more elements remain, return -1

def locate_card(cards,query):
    # find the first position and the last position
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        # find the middle position
        mid = (lo + hi)//2
        # find the number of middle position
        mid_number = cards[mid]

        print('lo:',lo, ',hi:',hi, ',mid:',mid, ',mid_number:',mid_number)

        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid - 1
        elif mid_number > query:
            low = mid + 1
    return -1



cards7 = test[7]['input']['cards']
query7 = test[7]['input']['query']
cards7
query7
locate_card(cards7,query7)==test[7]['output']

# we want to find the first one
# check the left position

def test_location(cards,query,mid):
    # locate current middle number of middle position
    mid_number = cards[mid]
    print('mid:',mid, ',mid_number:',mid_number)

    if mid_number == query:
        # check the left position
        if mid-1 >=0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'

    elif mid_number < query:
        return 'left'
    else:
        return 'right'


def locate_card(cards, query):
    # find the first position and last position
    lo, hi = 0, len(cards)-1

    while lo<=hi:
        mid = (lo + hi)//2
        result = test_location(cards,query,mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1


locate_card(cards7,query7)==test[7]['output']


evaluate_test_cases(locate_card, test)


# initial length - N
# iteration 1 - N/2
# iteration 2 - N/4 (N/2^2)
# iteration 3 - N/8 (N/2^3)
# ...
# iteration k - N/2^k

# final length of array is 1
# so N/2^k = 1
# N = 2^k
# taking the logarithm
# k = log N
# time complexity O(logN)


# Generic Binary Search
# general strategy behind binary search

# 1.come up with a condition to determine whether the answer lies before, after or at a given position
# 2.retrieve the midpoint and the middle element of the list
# 3.if it is the answer, return the middle positioin as the answer
# 4.if answer lies before it, repeat the search with the first half of the list
# 5.if answer lies after it, repeat the search with the second half of the list

# search first half or second half
def binary_search(lo, hi, condition):
    
    # low <= high, when low == high: there's only one number, mid=low=high
    while lo <= hi:
        print('lo:',lo, ',hi:',hi)
        mid = (lo + hi)//2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

# python allows passing functions as arguments to other functions

# find if it should go left or right
def locate_card(cards,query):

    def condition(mid):
        print('mid:',mid, ',mid_number:',cards[mid], ',query:',query)
        if cards[mid] == query:
            if mid-1 >= 0 and cards[mid-1]==query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'
    return binary_search(0, len(cards)-1, condition)

locate_card(cards7, query7)
test[7]


# given an array of intergers nums sorted in ascending order, 
# find the starting and ending position of a given number

# 1.the numbers are sorted in ascending order
# 2.we are looking for both the increasing order and the decreasing order

def first_position(num,target):
    def condition(mid):
        if num[mid] == target:
            if mid-1 >= 0 and num[mid-1] == target:
                return 'left'
            else:
                return 'found'
        elif num[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(target)-1, condition)

def last_position(num, target):
    def condition(mid):
        if num[mid] == target:
            if mid+1 <= len(num)-1 and num[mid+1] == target:
                return 'right'
            else:
                return 'found'
        elif num[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(target)-1, condition)

def first_and_last_position(num,target):
    return first_position(num,target), last_position(num,target)