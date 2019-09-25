strng = 'test1, test2, test3, test4, test5'

# first approach
n = input('Which test should we delete: ')
if strng.find(n) == len(strng) - 1:
    test = ', ' + 'test' + n
else:
    test = 'test' + n + ', '
print(strng.replace(test, ''))


# # second approach
# list = strng.split(', ')
# n = input('Which test should we delete: ')
# for test in list:
#     if n in test:
#         list.remove(test)
# print(', '.join(list))