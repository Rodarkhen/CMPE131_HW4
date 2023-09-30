import time

def my_steps(n):
    
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return n;
    #elif n == 2:
    #    return 2
    else:
        return my_steps(n - 1) + my_steps(n - 2)

def my_steps_list(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    
    # Create a list to store the number of ways to climb for each step.
    ways_to_climb = [0] * (n + 1)
    
    # Initialize values for the first two steps.
    ways_to_climb[1] = 1
    ways_to_climb[2] = 2
    
    # Calculate the number of ways to climb for each step from 3 to n.
    for i in range(3, n + 1):
        ways_to_climb[i] = ways_to_climb[i - 1] + ways_to_climb[i - 2]
    
    return ways_to_climb[n]
'''
def my_steps(n):
  """
  Returns the total number of ways to climb a ladder of `n` steps, where you can
  either go up by 1 or 2 steps, without using base cases.

  Args:
    n: An integer representing the number of steps on the ladder.

  Returns:
    An integer representing the total number of ways to climb the ladder.
  """

  if n < 1:
    raise ValueError("`n` must be an integer greater than or equal to 1.")

  # Initialize the two previous values.
  prev_prev_value = 1
  prev_value = 2

  # Recursively calculate the number of ways to climb a ladder of `n` steps.
  for i in range(3, n + 1):
    current_value = prev_prev_value + prev_value
    prev_prev_value = prev_value
    prev_value = current_value

  # Return the number of ways to climb a ladder of `n` steps.
  return current_value
'''
if __name__ == "__main__":
    while True:
      n = int(input("Enter the number of steps on the ladder (1 ≤ n ≤ 25): "))
      while n < 1:
        print("Invalid value!")
        n = int(input("Enter the number of steps on the ladder (1 ≤ n ≤ 25): "))
      start1 = time.time()
      ways1 = my_steps(n)
      print("Total number of ways w/o the list: ", ways1)
      end1 = time.time()
      print("Time elpased = ",end1- start1, "s")
      
      start2 = time.time()
      ways2 = my_steps_list(n)
      print("Total number of ways w the list: ", ways2)
      end2 = time.time()
      print("Time elpased = ",end2 - start2, "s")
      
