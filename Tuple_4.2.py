def del_element_from_tpl(tpl, element):
  if element in tpl:
    elem_index = tpl.index(element)
    return tpl[:elem_index] + tpl[elem_index + 1:]
  return tpl
y = 'y'
while y == 'y':
  input_tpl = input('enter tuple of elements, using comma: ').split(',')
  element = input('enter element to remove from tuple: ')
  print(del_element_from_tpl(input_tpl, element))
  y = input('restart?(y/n): ')
print('goodbye')