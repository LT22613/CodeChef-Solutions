# Convert all words into title case except for those that are already in upper case.

def main():
    # Take in t as the number of tests.
    t = int(input())
    
    # Run the while loop for the nubmert of tests being conducted.
    while t > 0:
        # Print out the result of performing the convert function which modifies the input string.
        print(convert())
        # Decrement t by 1 to ensure the while loop stops executing once t tests have been carried out.
        t -= 1

def convert():
    # Take in an input string s.
    s = input().split(" ")
    # Initialise a for loop to iterate through the different words in the input string.
    for i, val in enumerate(s):
        # If the word is in upper case, leave it.
        if val.isupper():
            pass
        # If the word is not completely in upper case, format it to title case.
        else:
            s[i] = val.title()
    # Return the elements of s as one long concatenated string. 
    # The syntax is that you place what you want between each element and then call the join method.
    # We want a space between each element, so we write ' ' and then call .join(s)
    return ' '.join(s)
        
# Only call main() if this is the main file being run.
if __name__ == "__main__":
    main()