def max_char(input):
  char_dict = {}

  for char in input:
    if char in char_dict:
      char_dict[char] += 1
    else:
      char_dict[char] = 1

  return max(char_dict, key=char_dict.get)
