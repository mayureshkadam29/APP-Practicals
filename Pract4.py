# Experiment 4
# Calculate the nth Fibonacci number efficiently

# Take input from the user
n = int(input("Enter the value of n: "))

# If n is 0
if n == 0:
    print("Fibonacci number is:", 0)

# If n is 1
elif n == 1:
    print("Fibonacci number is:", 1)

# For n greater than 1
else:
    # First two Fibonacci numbers
    a = 0
    b = 1

    # Calculate Fibonacci number from 2 to n
    for i in range(2, n + 1):

        # Add previous two numbers
        c = a + b

        # Move b to a
        a = b

        # Move c to b
        b = c

    # Display the nth Fibonacci number
    print("Fibonacci number is:", b)
   