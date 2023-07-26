def capitalize_title(word):
  return word.title()

def capitalize_manual(word):
  return ' '.join(string[0].upper() + string[1:] for string in word.split())


print(capitalize_manual("hello world everyone"))
