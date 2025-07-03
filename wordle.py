"""
Chef invented a modified wordle.

There is a hidden word S and a guess word T, both of length 5.

Chef defines a string M to determine the correctness of the guess word. For the ith index:

If the guess at the ith index is correct, the ith character of M is G.

If the guess at the ith index is wrong, the ith character of M is B.

Given the hidden word S and guess T, determine string M.
"""

# Take t as input.
def main():
    # Take t, the number of trials, as input.
    t = int(input())
    
    while t > 0:
        # Print the result of modified_world.
        print(modified_wordle())
        
    
    
def modified_wordle():
    # Initialise an empty string called output.
    output = ""
    # Take the hidden word, S, as input.
    hidden = input()
    # Take the guess word, T, as input.
    guess = input()
    # Zip the two lists of letters of each word and iterate through each pair.
    for a,b in zip(hidden, guess):
        # If the letters match, concatenate G to the output string.
        if a == b:
            output += "G"
        # If the letters do not match, concatenate B to the output string.
        else:
            output += "B"
    # Return the final output string.
    return output

# Only call main() if this is the main file being run.
if __name__ == "__main__":
    main()
        