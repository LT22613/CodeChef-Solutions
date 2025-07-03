# Take t as input.
def main():
    t = int(input())

    while t > 0:
        encoded_seq = ""
        n = int(input())
        s = input()
        # Iterate through every two characters in s, which is the binary input line.
        # To do so we can use a list comprehension combined with slicing.
        pairs = [s[2*i:2*i+2] for i in range(n//2)]
        
        # If "00", then return A, if "01" return T, if "10" return C, if "11" return G.
        for pair in pairs:
            if pair == "00":
                encoded_seq += "A"
            elif pair == "01":
                encoded_seq += "T"
            elif pair == "10":
                encoded_seq += "C"
            else:
                encoded_seq += "G"
        t -= 1
        print(encoded_seq)

main()