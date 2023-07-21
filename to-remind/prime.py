#using clear and not-clear func

def prime_or_not(number):   #user
    ans = True
    for idx in range(2, (number // 2) + 1):
        if number % idx == 0:  
            ans = False
    return ans
    
def say_prime_or_not(number):
    if prime_or_not(number):
        print('yes')
    else:
        print('no')


###################################
import math

def is_prime(num):   #hexlet
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def say_prime_or_not(num):
    answer = 'yes' if is_prime(num) else 'no'
    print(answer)