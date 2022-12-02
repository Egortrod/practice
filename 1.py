import random
import time
start_time = time.time()
items = [random.randint(0, 1000) for i in range(1000)]
print('Ranomize array:')
print(items)
print('Maximum value of array =', max(items))
print('Minimal value of array =', min(items))
runtime = (time.time() - start_time) 
# print('Time passed:' + " %s * 10^-5 seconds " % runtime)
print(f'Time passed: {round(runtime*1000, 2)} ms') 
