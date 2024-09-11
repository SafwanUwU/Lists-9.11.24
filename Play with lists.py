l = [4, 5, 1, 2, 9, 7, 10, 8, 88, 99, 107, 10, -99]
print("Original List :" , l)
count = 0
for i in l:
    count = count + i
print("sum = ", count)
avg = count/len(l)
print("Average = ", avg)
l.sort()
print("Sorted List: ",l)
print("Smallest element is" , l[0])
print("Largest element is" , l[-1])