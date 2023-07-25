import re

def anagrams_one(first, second):
  def build_char_dict(input):
    char_dict = {}
    cleaned = re.findall(r'[a-z]', input.lower())
    
    for char in cleaned:
      if char in char_dict:
        char_dict[char] += 1
      else:
        char_dict[char] = 1
    
    return char_dict

  first_dict = build_char_dict(first)
  second_dict = build_char_dict(second)

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
