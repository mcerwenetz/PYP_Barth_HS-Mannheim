lis=[1,2,3]
print("lis: " , lis)

lis[len(lis):]=[4]
print("lis: " , lis)

unter=[5,6]
print("lis: " , lis)
print("unter: " , unter)

lis[1]=unter
print("lis: " , lis)
print("unter: " , unter)

unter[0]=7
print("lis: " , lis)
print("unter: " , unter)