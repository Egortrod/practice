input_GNA = input() + ' '
counter = 0
index = input_GNA[0]
for i in input_GNA:       
    if index != i:
        print(index + str(counter), end = '')
        counter = 0
        index = i
    counter += 1