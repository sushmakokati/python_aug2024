def my_function(some_list):
    some_list.remove(10)
    some_list.insert(1,25)
    some_list.append(50)
print('Enter space seprated numbers')
list1 = list(map(int,input().split()))
print(list1)
my_function(list1)
print(list1)