# Difficulty 801

"""
For encoding an even-length binary string into a sequence of A, T, C, and G, we iterate from left to right and replace the characters as follows:

00 is replaced with A
01 is replaced with T
10 is replaced with C
11 is replaced with G
Given a binary string S of length N (N is even), find the encoded sequence.
"""

# Take t as input.
def main():
    # Take t, the number of trials, as input.
    t = int(input())

    while t > 0:
        # Initialise an empty string called encoded_seq.
        encoded_seq = ""
        # Take in n, the length of the sequence, as an input and convert to an int.
        n = int(input())
        # Take in s, the binary string, as input.
        s = input()
        # Iterate through every two characters in s, which is the binary input line.
        pairs = [s[2*i:2*i+2] for i in range(n//2)]
        
        # If the element is "00", then concatenate A, if "01" concatenate T, if "10" concatenate C, if "11" concatenate G.
        for pair in pairs:
            if pair == "00":
                encoded_seq += "A"
            elif pair == "01":
                encoded_seq += "T"
            elif pair == "10":
                encoded_seq += "C"
            else:
                encoded_seq += "G"
        print(encoded_seq)
        t -= 1

# Only run if this is the main file being executed.
if __name__ == "__main__":
    main()