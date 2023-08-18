from random import randint, choice

def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = choice(nums)
   l_nums = [n for n in nums if n < q]
   e_nums = [q] * nums.count(q)
   b_nums = [n for n in nums if n > q]
   return quicksort(l_nums) + e_nums + quicksort(b_nums)

def qsort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
                print(equal)
            elif x > pivot:
                greater.append(x)
        return qsort(less) + equal + qsort(greater)
    else:
        return array
    

user_data = [randint(1, 50) for _ in range(20)]
print(f'user arr: {user_data}')
print(f'sorted arr: {qsort(user_data)}')