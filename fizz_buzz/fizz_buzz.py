def fizz_buzz_while(n):
  result = []
  counter = 1

  while counter <= n:
    if counter % 3 == 0 and counter % 5 == 0:
      result.append('fizzbuzz')
      counter += 1
    elif counter % 3 == 0:
      result.append('fizz')
      counter += 1
    elif counter % 5 == 0:
      result.append('buzz')
      counter += 1
    else:
      result.append(str(counter))
      counter += 1

  return result
