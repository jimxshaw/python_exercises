def steps(n):
  for i in range(1, n + 1):
    print('#' * i + ' ' * (n - i))

def steps_recursion(n, row=0, step=''):
  if n == row:
    return

  if n == len(step):
    print(step)
    return steps_recursion(n, row + 1)

  if len(step) <= row:
    step += '#'
  else:
    step += ' '

  steps_recursion(n, row, step)
