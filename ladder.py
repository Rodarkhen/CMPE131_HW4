def my_steps(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    
    # Create a list to store the number of ways to climb for each step.
    steps = [0] * (n + 1)
    
    # Initialize values for the first two steps.
    steps[1] = 1
    steps[2] = 2
    
    # Calculate the number of ways to climb for each step from 3 to n.
    for i in range(3, n + 1):
        steps[i] = steps[i - 1] + steps[i - 2]
    
    return steps[n]