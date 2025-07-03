# Difficulty 940


# Consider if the number is 999, then the number becomes 1000.
# If the number is 899, then the number becomes 900.
# If the number is 8999, it becomes 9000.
# If the number is 8989 - It becomes 8990.

# So if the number has a string of x 9s at the end, then we can consider first the slice of the number that is the first n-x-1 digits
# and then the end slice of the number which is the remaining x+1 digit. When converting the number, the last digits will become 0s and the x+1th digit
# from the end is increased by 1 (it is by definition not 9 as we have defined the digits like that.)
       
    
def add_one():
    # Ask for the number.
    number = input("Enter your number ")
    # Initialise an empty string.
    string = ''
    # Calculate how many nines there are at the end of the number.
    for digit in number[::-1]:
        if digit == "9":
            string += digit
        else:
            break
        
    # Accordingly, calculate how to add one.

    # If there are no nines, simply add one to the last digit.
    # If there are some nines, then change all the last digits to 0 and increase the last non-nine digit by 1.
    # If they are all nines, then there is no previous digit. In this case, append a 1 
    # to the beginning of the string. 
    # This can be done by doing 1 + "0"*len(number).
    
    # If the last digit is not a 9, then the string is empty.
    if len(string) == 0:
        # Convert the last digit of number, which is a string, to an integer.
        last = int(number[-1])
        # Slice the given number so that it contains all the digits apart from the last.
        number = number[:-1]
        # Add 1 to the last digit
        last += 1
        # Convert the last digit back to a string and concatenate the two strings to make the new number.
        return number + str(last)
    
    # If the string is not empty, but does not contain all the digits of number, execute this block.
    elif len(string) < len(number):
        # Slice off the part of "number" one digit before the part contained in string.
        beg_slice = number[0:-len(string)-1]
        # Slice off the part of the the number that is contained in string and one extra digit before.
        end_slice = number[-len(string)-1:]
        # Convert the first digit of the end slice to an integer.
        first_digit = int(end_slice[0])
        # Add one to the first digit
        first_digit += 1
        # Convert first_digit back to a str.
        first_digit = str(first_digit)
        # Concatenate the beg_slice, the first digit and set the remainder of the digits to 0.
        return beg_slice + first_digit + "0"*len(string)
    
    else:
        # If all the digits of number are 9, concatenate one to the beginning of a string of 0s the length of the number.
        return "1" + "0"*len(string)
    
def main():
    # Ask for the number of trials and convert to an integer.
    t = int(input())
    
    while t > 0:
        # Call add_one() and print the result.
        print(add_one())
        # Decrement t by one to ensure the while loop ends after all tests have been run.
        t -= 1

# Only call main() if this is the main file being run.
if __name__ == "__main__":
    main()