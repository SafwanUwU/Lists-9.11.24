def squareItOut(l):
    ll = []
    for i in l:
        ll.append(i**2)
    return ll
li = [1,2,3,4,5,6,7,8,9,10]
print("Original List" , li)

resultList = squareItOut(li)
print("Square of the List: ", resultList)