# Take t as input.
def main():
    modified_wordle()
    
def modified_wordle():
    t = int(input())
    
    while t > 0:
        output = ""
        hidden = input()
        guess = input()
        for a,b in zip(hidden, guess):
            if a == b:
                output += "G"
            else:
                output += "B"
        print(output)

main()
        