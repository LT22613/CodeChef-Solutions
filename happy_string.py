# Difficulty 956

"""
Chef has a string S with him. 

Chef is happy if the string contains a contiguous substring of length strictly greater than 2 in which all its characters are vowels.

Determine whether Chef is happy or not.

Note that, in english alphabet, vowels are a, e, i, o, and u.
"""

def main():
    # Take in t as the number of tests.
    t = int(input())

    while t > 0:
        # Call happy_string() and print the result.
        print(happy_string())
        # Decrement by t for each run.
        t -= 1
    
def happy_string():
    # Take in s as input and convert all characters to lowercase if necessary.
    s = input().lower()
    # Initialise a variable to count the number of consecutive vowels in a substring of s.
    vowel_counter = 0
    # Initialise a variable to keep track of where the for loop is up to in s.
    letter_counter = 0
    # Iterate over each character in s.
    for _ in s:
        # Add 1 to the letter_counter for each new iteration.
        letter_counter += 1
        
        # If the current letter is a vowel, proceed with this loop.
        if _ in ["a","e","i","o","u"]:
            # Add 1 to the counter.
            vowel_counter += 1
            # If the counter exceeds a count of 2, then print Happy and end the loop.
            if vowel_counter > 2:
                return "Happy"
            else:
                pass
        # If the current letter is not a vowel, reset the counter to 0.
        else:
            vowel_counter = 0
        
        if letter_counter == len(s):
            return "Sad"
        else:
            pass
    
if __name__ == "__main__":
    main()
        
            
        
   
