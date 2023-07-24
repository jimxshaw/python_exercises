def is_number_happy(n):
  def get_digit_square_sum(num):
    return sum(int(digit) ** 2 for digit in str(num))

  slow = n
  fast = n

  while True:
    slow = get_digit_square_sum(slow)
    fast = get_digit_square_sum(get_digit_square_sum(fast))

    if slow == fast:
      break

  return slow == 1
