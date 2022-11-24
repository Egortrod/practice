import random
import time
start_time = time.time()
items = [random.randint(0, 10) for i in range(10)]
print('Ranomize array:')
print(items)
print('Maximum value of array =', max(items))
print('Minimal value of array =', min(items))
runtime = (time.time() - start_time) * 100000 
print('Time passed:' + " %s * 10^-5 seconds " % runtime)
