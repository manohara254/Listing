# List = []
# print("Intial blank List: ")
# print(List)
#
# # Addition of Elements
# # in the List
# List.append(1)
# List.append(2)
# List.append(4)
# print("\nList after Addition of Three elements: ")
# print(List)
#
# # Adding elements to the List
# # using Iterator
# for i in range(4, 5):
#     List.append(i)
# print("\nList after Addition of elements from 1-3: ")
# print(List)
#
# List2 = ['For', 'Geeks']
# List.append(List2)
# print("\nList after Addition of a List: ")
# print(List)
#
# # Addition of Element at
# # specific Position
# # (using Insert Method)
# List.insert(3, 12)
# List2.insert(0, 'Geeks')
# print("\nList after performing Insert Operation: ")
# print(List)
#
# def Sumlist(items):
#     sum = 0
#     for i in items:
#         sum+=i
#     return sum
# print Sumlist([5,6,7,8])
#
# def mullist(items):
#     mul = 1
#     for i in items:
#         mul*=i
#     return mul
# print mullist([5,6,7,8])
#
#
# def large(items):
#     max = items[0]
#     for i in items:
#         if i > max:
#             max = i
#     return max
# print large([5,6,7,8])
#
# def small(items):
#     min = items[0]
#     for i in items:
#         if i < min:
#             min = i
#     return min
# print small([5,6,7,8])
#
# def FLsame(items):
#     count = 0
#     for i in items:
#         if len(i) > 1 and i[0] == i[-1]:
#             count+=1
#     return countenumerate
# print FLsame(["1","676","7997","898", "765"])
#
# items = [1,2,3,4,5,1,2,5,9,4]
# dupli = []
# uni = set(items)
# print uni
# for i in items:
#     if i not in dupli:
#         uni.add(i)
#         dupli.append(i)
# print(dupli)
# print(uni)
#
# def lasterthenn(n, str):
#     list = []
#     txt = str.split(" ")
#     for i in txt:
#         if len(i) > n :
#             list.append(i)
#     return list
# print (lasterthenn(3, "The quick brown fox jumps over the lazy dog"))
#
# def truernot(items1 , items2):
#     result = False
#     for i in items1:
#         for j in items2:
#             if i == j:
#                 result = True
#                 return result
#
# print (truernot([1,2,3,4,5], [5,6,7,1]))
#
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# color = [x for (i,x) in enumerate(color) if i not in (0,4,5)] #x is list item in it i is index no.
# print(color)
#
# test_list = [{"Akash": 1}, {"Kil": 2}, {"Akshat": 3}, {"Kil": 2}, {"Akshat": 3}]
#
# # printing original list
# print ("Original list : " + str(test_list))
#
# # using naive method to
# # remove duplicates
# res_list = []
#
# for i in range(len(test_list)):
#     if test_list[i] not in test_list[i + 1:]:
#         res_list.append(test_list[i])
#
#     # printing resultant list
# print ("Resultant list is : " + str(res_list))
#
# items = [1,2,3,4,5,1,2,5,9,4]
# temp = []
# for i in range(0,len(items)-1,2):
#     temp = items[i]
#     items[i] = items[i+1]
#     items[i+1] = temp
#
# print items
#
# items = [1,2,3,4,5,1,2,5,9,4]
# temp = []
# n = len(items)-1
# for i,j in range(-1):
#     temp = items[i]
#     items[i] = items[j]
#     items[j] = temp
# print items
#
# thistuple = ["apple", "banana", "cherry"]
# print(thistuple)
# thistuple.insert(1, "blackcurrant")
# print(thistuple)
# print thistuple * 2
# print thistuple.index("banana")
# # the value is still the same:
#
#
# str1 = ["apple", "banana", "cherry"]
#
# str1.reverse()
# print str1.append("apple1")
# str1.sort()
# print str1
#
#
#
#
# str1 = ('Manohara', 'So')
# str2 = ('.R',)
# str = (str1 + str2)
#
# print (str)
#
#
# coral = ["blue coral", "staghorn coral", "pillar coral", "elkhorn coral"]
# kelp = ["wakame",]
#
# coral_kelp = (coral * 2 + kelp)
#
# print(coral_kelp)
#
# word = 'geeks, for, geeks'
#
# print(word.split()[1:3])
# a = [1,2,3,4,5,1]
# a = set(a)
# print a
# a = {"a", "b","c"}
# b = {"a","c"}
#
# customer_details = { 1001 : "John", 1004 : "Jill", 1005: "Joe", 1003 : "Jack" }
#
# print(customer_details)
# print(len(customer_details))
# print(sorted(customer_details.values()))
# del(customer_details[1005])
# print(customer_details)
# customer_details[1003] = "Mary"
# print(customer_details)
# print(1002 in customer_details)
#
# java_course = {"John", "Jack", "Jill", "Joe"}
# python_course = {"Jake", "John", "Eric", "Jill"}
# '''a. List the number of Students enrolled for Python course
# b. List the names of Students enrolled for Java course only
# c. List the names of Students enrolled for Python course only
# d. List the number and names of Students enrolled for both Java and Python courses
# e. List the number and names of Students enrolled for either Java or Python courses
# but not both
# f. List names and number of Students enrolled for either Java or Python courses'''
# print len(python_course)
# print len(java_course)
# print len(python_course - java_course)
# print len(java_course & python_course)
# print len(java_course - python_course)
# a = len(python_course - java_course)
# b = len(java_course - python_course)
# c= a+b
# print c

#
# def merge_sort(n_list):
#     print("splitting",n_list)
#     if len(n_list)>1:
#         mid = len(n_list)//2
#         lefthalf = n_list[:mid]
#         righthalf = n_list[mid:]
#
#         merge_sort(lefthalf)
#         merge_sort(righthalf)
#         i = j = k = 0
#         while i < len(lefthalf) and j < len(righthalf):
#             if lefthalf[i] < righthalf[j]:
#                 n_list[k] = lefthalf[i]
#                 i = i + 1
#             else:
#                 n_list[k] = righthalf[j]
#                 j = j + 1
#             k = k + 1
#
#         while i < len(lefthalf):
#             n_list[k] = lefthalf[i]
#             i = i + 1
#             k = k + 1
#
#
#         while j < len(righthalf):
#             n_list[k] = righthalf[j]
#             j = j + 1
#             k = k + 1
#     print("Merging ", n_list)
#
# print(merge_sort([6,7,1,2,3,9,8]))




# tuo = (1,2,3)
# tu4 = ('1',)
# print (tuo + tu4)
#
#
# b= {1, 2.0,'three'}
# c={4,5}
# a = sum(c)
# print(a)
# b.add(3)
# print(b)
#
# a = any({0,''})
#
# print(a)
#
# numbers={1, 2, 3, 4, 5, 6, 3.5}
# print(sorted(numbers))
# print(numbers)

set1 = {1,2,3}
set2 = {3,4,5}

# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set1.symmetric_difference(set2))
# print(set1.intersection_update(set2))
# print(set1.difference_update(set2))
# print(set1.symmetric_difference_update(set2))
#
# a = bool((3,2))
# print(a)

# a = [1,2,[3,4,[5,6,[8,9,[10,11]]]]]
#
# b = []
#
# for i in a:
#
#     if type(i) is not list:
#             b.append(i)
#             print(b)
#     else:
#         for j in i:
#             b.append(j)
#             print(b)

#
# def listing(nlist,b = []):
#     for i in nlist:
#         if type(i) is not list:
#             b.append(i)
#         else:
#             listing(i)
#
#     return b
# print(listing([1,2,[3,4,[5,6,[8,9,[10,11]]]]]))
#
# l = [[1,2],[3,4],[5,6]]
# d = []
# for i in l:
#     for j in i:
#         d.append(j)
# print(d)
#
#
# l=6
#
# for i in range(2,l):
#     if l % i == 0:
#         print(False)
#         break
#     else:
#         print(True)
#         break
#
# lower = 900
# upper = 1000
#
#
# print("Prime numbers between", lower, "and", upper, "are:")

# for num in range(lower,upper):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)
#     else:
#         print(num)

# def fac(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fac(n-1)
# print(fac(5))
#
# def fibb(n):
#     if n <= 1:
#         return n
#     else:
#         return (fibb(n-1) + fibb(n-2))
# n = 5
# for i in range (n):
#     print(fibb(i))
#
# x = lambda a : a * 2
# for i in range(1,11):
#     print(x(i))
# numbers=[0,1,2,3,4,5,6,7,8,9,10]
# # print(list(filter(lambda x:x%3==0,numbers)))
#
# from functools import reduce
# print(reduce(lambda x,y:y-x,numbers))
#
#
# def divide(a, b):
#     return a / b
#
#
# def decorator(func):
#     def wrapper(a, b):
#         if b == 0:
#             print("Can't divide by 0!")
#             return
#         return func(a, b)
#
#     return wrapper
#
# r = decorator(divide)
# print(r(4,2))
#
# def sum(a,b):
#     return(a+b)
# def doc(func):
#     def wrap(a,b):
#         return func(a,b)
#     return wrap
# r = doc(sum)
# print(r(4,2))
#
# nums = [1, 2, 3]
# numIter = iter(nums)
# print(numIter.next())
# print(numIter.next())
# print(numIter.next())



l1 = [1,2,[3,4,[5,6,[8,9,[10,11]]]]]
str1 = str(l1).replace(']','').replace('[','')
print(str1.split(','))
a = list(map(int ,str1.split(',')))
print(a)
#
# print(a[5:])
#
# a = "10"
# print(2*a)
#
#
# l1 = ['a','b',['c','d',['e','f',['g','h',['i','j']]]]]
# l2 = []
# for i in str(l1):
#     if i.isalpha():
#         l2.append((i))
# print(l2)
#
#
# print(l2[-4:-1])


a = [1,2,3,4,5,6]
b = [9,8,7,5,3,4]
c = []
for i in range(len(a)):
    if i % 2 == 0:
        c.append(a[i])
    else:
        c.append(b[i])
print(c)

a = [1,2,3,4,5,6]
b = [9,8,7,5,3,4]

for i in range(1,len(a),2):
    a[i] = b[i]
print(a)

d ={}
for i in a:
    keys = d.keys()
    if i in keys:
        d[i] = d[i] + 1
    else:
        d[i] = 1
print(d)

# l = [1,2,3,1,1,1,2,3,4,5]
# d = {}
# for i in l:
#     keys = d.keys()
#     if i in keys:
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1
# print(d)



# import xmltodict
# import pprint
# import json
#
# my_xml = """
#     <audience>
#       <id what="attribute">123</id>
#       <name>Shubham</name>
#     </audience>
# """
# my_dict = xmltodict.parse(my_xml)
# print(my_dict['audience']['id'])
# print(my_dict['audience']['id']['@what'])



a = 'helloworld'
print(a[-3:-6:-1])
a = "manu"
print("".join(reversed(a)))




with open('text.txt','r') as fp:
    for i in fp.readlines():
        str = []
        if i.islower():
            str.append(i)
        print str

num = 1
def a():
    global num
    num = num + 3
    return(num)
print(a())
print(num)


str = 'My name is Manohara'
str = str.split(' ')
str = str[::-1]
print(str)

a= ''
for i in str:
    a = a +' '+i
print(a.strip())

