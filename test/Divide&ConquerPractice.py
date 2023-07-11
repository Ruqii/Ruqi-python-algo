## Problem Statement - Polynomial Multiplication

# Given two polynomials represented by two lists, 
# write a function that efficiently multiplies given two polynomials. 
# For example, the lists `[2, 0, 5, 7]` and `[3, 4, 2]` 
# represent the polynomials 2 + 5x^2 + 7x^3 and 3 + 4x + 2x^2. 
#  
# Their product is 
# (2 \times 3) + (2 \times 4 + 0 \times 3)x + 
# (2 \times 2 + 3 \times 5 + 4 \times 0)x^2 + 
# (7 \times 3 + 5 \times 4 + 0 \times 2)x^3 + 
# (7 \times 4 + 5 \times 2)x^4 + (7 \times 2)x^5 i.e. 
# 
# 6 + 8x + 19x^2 + 41x^3 + 38x^4 + 14x^5
# 
# It can be represented by the list `[6, 8, 19, 41, 38, 14]`.

# input
nums1 = [2, 0, 5, 7]
nums2 = [3, 4, 2]

# output list length = len(nums1) + len(nums2)
# traverse nums1 and nums2
# nums1.index + nums2.index = output.index

# 1.set an output list with [0] * list length
# 2.traverse nums1 and nums2
# 3.multiply values in two list
# 4.add value to certain position in output list

def multiplies(nums1, nums2):
    output = [0] * (len(nums1) + len(nums2))
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            # print(i, j)
            output[i+j] += nums1[i] + nums2[j]
    return output
multiplies(nums1,nums2)


# improvement
def add(poly1, poly2):
    """add two polynomials"""
    result = [0]*max(len(poly1),len(poly2))
    for i in range(len(result)):
        if i < len(poly1):
            result[i] += poly1[i]
        if i < len(poly2):
            result[i] += poly2[i]
    return result
def split(poly1, poly2):
    """split each polynomials"""
    mid = max(len(poly1), len(poly2)) // 2
    return (poly1[:mid], poly1[mid:]), (poly2[:mid], poly2[mid:])
def increase_exponent(poly, n):
    """multiply poly1 by x^n"""
    return [0]*n + poly
def multiply_optimised(poly1, poly2):
    split1, split2 = split(poly1, poly2)

split(nums1, nums2)