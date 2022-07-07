def sieve(lst):
  unique_lst = []
  for elem in reversed(lst):
    if elem not in unique_lst:
      unique_lst.append(elem)
  return tuple(unique_lst)
y = 'y'
while y == 'y':
  input_list = input('enter list of elements, using comma: ').split(',')
  print(sieve(input_list))
  y = input('restart?(y/n): ')
print(goodbye)