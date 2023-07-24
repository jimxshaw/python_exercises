def chunk(arr, n):
  result = []
  index = 0

  while index < len(arr):
    result.append(arr[index : index + n])
    index += n
  
  return result

def chunk_manual(arr, n):
  result = []

  for num in arr:
    if not result or len(result[-1]) == n:
        result.append([num])
    else:
        result[-1].append(num)
  
  return result
