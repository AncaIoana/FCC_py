#find the largest number
lst = [5,8,13,86,2,454,63,2]

largest_number = 0

##for i in lst:
##    if i > largest_number:
##        largest_number = i
##
##print (largest_number)


for i in range(len(lst)):
    if lst[i] > largest_number:
        largest_number = lst[i]

print (largest_number)
