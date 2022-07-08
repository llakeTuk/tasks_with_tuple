def tpl_sort(tpl):
  for element in tpl:
    if isinstance(element, int):
      return print(tpl)
    else:
      return print(tuple(sorted(tpl)))
y = 'y'
while y == 'y':
  input_list = input('enter tuple of elements, using comma: ').split(',')
  tpl = tuple(input_list)
  tpl_sort(tpl)
  y = input('restart?(y/n): ')
print('goodbye')
