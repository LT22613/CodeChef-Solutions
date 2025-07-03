# Interesting, if we consider 11110100 - this is a string of length 8. In such a string there are 7 gaps between the numbers.
# It is where the consecutive numbers are 10 or 01 that we do not need to place a number to defy consecutiveness.
# The count function doesn't count overlapping numbers of the same type - but by definition, you can't have two 10s in a row as otherwise 
# you'd have two 1s in a row...

# Hence, we can reverse engineer the count a little bit.
# If the string has length n, then there are n-1 spaces, and we can take away the number of occurences of 01 and 10 to leave the number of times we have 00
# or 11.

t = int(input())

# Setup a while loop that runs for all test cases.
while t > 0:
    # Take in n as the length of the binary string.
    n = int(input())
    # Take in s as the binary string.
    s = input()
    # Count the number of times 00 appears in s.
    counter_1 = int(s.count("01"))
    # Count the number of times 11 appears in s.
    counter_2 = int(s.count("10"))
    # Print out the number of times both things
    print(n - 1 -(counter_1 + counter_2))
    # Reduce the counter so that the code stops running once all tests have been run.
    t -= 1