# #list
# a = [1,2,3,4,5,6,7,8,9,10]
# b = [1,3,5,7]
# a.insert(1,50)
# print(a[1])

# a.remove(50)
# print(a[1])
# # a.extend(b)
# print(a)
# c = set(a)
# d = set(b)

# print(c.union(d))

# # #tuple
# # tp = (1,2,3,4,5)
# # # tp.append(10) not possible
# # print(tp[0])

# #Dictonary
# dic = {"Mradul" : "19/20","Moksh" : "18/20"}
# print(dic.keys())
# print(dic.values())
# print(dic["Mradul"])
# print(dic)

#Tuples
# tp = (10,20,30,40,50)
# print(tp[2])
# print(tp)
# print(tp.index(20))

# tup = (10,20,10,30,10)
# count = 0;
# for x in tup:
#     if(x == 10):
#         count+=1
# print(count)

#Create set
s = {5,10,15}
s.add(20)
print(s)
s.remove(10)
print(s)

set1 = {5,10,15}
set2 = {10,20,30}

print(set1.union(set2))