# -*- coding: utf-8 -*-

#Ekaum Soni
#List Practice HW

#1. You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.
list1 = [15, 100, 154, 20, 253, 530, 203]
for elem in list1:
    if (elem == 20):
        elem = 200
print(list1)

#problem 2:
list1 = [5, 20, 15, 20, 25, 50, 20]
for elem in list1:
    if (elem == 20):
        list1.remove(elem)
print(list1)

#problem 3:
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
print(list(filter(None, list1)))

#problem 4:
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

#problem 5:
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sublist = ["h", "i", "j"]
list1[2][1][2].extend(sublist)
print(list1)

#problem 6:
list1 = [10, 20, 30, 40] 
list2 = [100, 200, 300, 400]
for i in range(len(list1)):
    print(list1[i], end= " ")
    print(list2[len(list1) - 1 -i])

#problem 7:
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = []
x = zip(list1, list2)
for a, b in x:
    list3.append(a + b)
print(list3)

#problem 8:
numbers = [1, 2, 3, 4, 5, 6, 7]
list2 = []
for elem in numbers:
    list2.append(pow(int(elem), 2))
print(list2)

#problem 9:
phrase = " The best class in Greenhill is Data Science"
print(phrase.split())