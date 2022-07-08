def slicing(tpl, element):
  if element in tpl:
    if tpl.count(element) > 1:
      first_index = tpl.index(element)
      second_index = tpl.index(element, first_index + 1) + 1
      return tpl[first_index : second_index]
    else:
      return tpl[tpl.index(element) :]
  else:
    return ()
y = 'y'
while y == 'y':
  input_list = input('enter tuple of elements, using comma: ').split(',')
  element = input('enter element for slicing: ')
  tpl = tuple(input_list)
  print(slicing(tpl, element))
  y = input('restart?(y/n): ')
print('goodbye')
