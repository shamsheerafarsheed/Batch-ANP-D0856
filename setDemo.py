#Set --> A set is unordered,unindexed and mutable collection of unique elements
Set1={11,22,33}
#empty set using set constructor--()
print(Set1)
set2=()
Birds={"Crow","Owl","peacock"}
print(Birds)
print("----Adding Elements--")
Birds.add("Pigion")
print(Birds)
Birds.remove("peacock")
print(Birds)

#discard-->no error if elements not present
#remove-->raise an  error if elements not present
#pop,clear,issubset(),issuperset,isdisjoint(true if no common elements)
set2={23,45,67}
print("----------Union---------")
a={22,45,67,89}
b={34,56,78,67,56}
print(a.union(b))
print("---------Intersection----------")
print(a.intersection(b))
print("---------Difference----------")
print(a.difference(b))
print("---------Symmetric Difference----------")
print(a.symmetric_difference(b))

#to remove duplicates
#fast membership
#store unique,unordered items(ex:users,categories etc)

day1={"Anusha","Prachi Kumari","uzma","Chandrashekar C M"}
day2={"Anusha","Prachi Kumari","manoj","Govardhan"}
All=day1.union(day2)
print(All)
Present_Allday=day1.intersection(day2)
print(Present_Allday)



