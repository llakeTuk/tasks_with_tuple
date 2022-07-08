def del_element_from_tpl(tpl, element):
  input_lst = list(tpl)
  if element in input_lst:
    input_lst.remove(element)
  return tuple(input_lst)
y = 'y'
while y == 'y':
  input_tpl = input('enter tuple of elements, using comma: ').split(',')
  element = input('enter element to remove from tuple: ')
  print(del_element_from_tpl(input_tpl, element))
  y = input('restart?(y/n): ')
print('goodbye')