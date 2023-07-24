def chunk(arr, n):
  result = []
  index = 0

  while index < len(arr):
    result.append(arr[index : index + n])
    index += n
  
  return result
