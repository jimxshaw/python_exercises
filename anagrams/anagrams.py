import re

def anagrams_one(first, second):
  first_dict = {}
  second_dict = {}

  first_cleaned = re.findall(r'[a-z]', ''.join(first.lower()))
  second_cleaned = re.findall(r'[a-z]', ''.join(second.lower()))

  for char in first_cleaned:
    if char in first_dict:
      first_dict[char] += 1
    else:
      first_dict[char] = 1

  for char in second_cleaned:
    if char in second_dict:
      second_dict[char] += 1
    else:
      second_dict[char] = 1

  if first_dict.keys() == second_dict.keys():
    for key in first_dict:
      if first_dict[key] != second_dict[key]:
        return False
    return True
  else:
    return False

def anagrams_two(first, second):
  def clean_and_count(input):
      cleaned = re.sub(r'[^a-zA-Z]', '', input).lower()
      counter = {}
      for char in cleaned:
          counter[char] = counter.get(char, 0) + 1
      return counter

  first_dict = clean_and_count(first)
  second_dict = clean_and_count(second)

  return first_dict == second_dict
