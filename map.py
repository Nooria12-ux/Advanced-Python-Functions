numbers = [1,2,3,4,5,6,7,8,9]

even = [i for i in numbers if i% 2 == 0]

print(even)

#==========================================================

nums = [1,2,3,4,5]

def sq(n):
    return n * n

square = map(sq, nums)

print(f"The square numbers list is s follows: {list(square)}")
