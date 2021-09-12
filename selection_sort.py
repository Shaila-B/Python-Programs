list=[56, 8, 4, 3, 6, 1]
print(list)
for i in range(len(list)):
    min_val=min(list)
    print('min value:', min_val)
    min_ind=list.index(min_val)
    print('min value index', min_ind)
    list[i], list[min_ind]=list[min_ind], list[i]
print(list)
    
