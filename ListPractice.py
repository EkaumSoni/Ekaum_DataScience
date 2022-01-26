# -*- coding: utf-8 -*-

#Ekaum Soni
#List Practice HW

#1. You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.
list1 = [15, 100, 154, 20, 253, 530, 203]
for elem in list1:
    if (elem == 20):
        elem = 200
print(list1)

#2. You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.
list1 = [5, 20, 15, 20, 25, 50, 20]
for elem in list1:
    if (elem == 20):
        list1.remove(elem)
print(list1)


#3.Given a Python list, write a program to remove all occurrences of item 20.

#4.Remove empty strings from the list of strings. HINT: use filter() function
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
print(list(filter(None, list1)))

#Write a program to add item 7000 after 6000 in the following Python List HINT(use append indexing the lists in the lists)
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

#6.  You have given a nested list. Write a program to extend it by adding the sublist ["h", "i", "j"] in such a way that it will look like the following list.
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sublist = ["h", "i", "j"]
list1[2][1][2].extend(sublist)
print(list1)

#7.-Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.
list1 = [10, 20, 30, 40] 
list2 = [100, 200, 300, 400]
for i in range(len(list1)):
    print(list1[i], end= " ")
    print(list2[len(list1) - 1 -i])

#8.Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = []
x = zip(list1, list2)
for i, f in x:
    list3.append(i + f)
print(list3)

#9.Given a list of numbers. write a program to turn every item of a list into its square.
numbers = [1, 2, 3, 4, 5, 6, 7]
list2 = []
for i in numbers:
    list2.append(pow(int(i), 2))
print(list2)

#10. Create a lsit for every word in a string:
phrase = " The best class in Greenhill is Data Science"
print(phrase.split())