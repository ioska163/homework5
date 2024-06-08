immutable_var = (1, 2, 3, 'string', True)
print(immutable_var)
#immutable_var [0] = 100
#print(immutable_var) кортеж нельзя изменить!
mutable_list = [1, 2, 3, 'string', True]
mutable_list[3] = 'summer'
print(mutable_list)
