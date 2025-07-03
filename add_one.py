# cook your dish here

# Basically this is a huge number.

# So, interesting - if the number is 999, then the number becomes 1000.
# If the number is 899, then the number becomes 900.
# If the number is 8999.
# If the number is 8989 - It becomes 8990.

# So if the number has a string of x 9s at the end, then the number is the first n-x-1 digits
# and then the remainder of the number is x+1 digits where the last digits are 0s and the x+1th digit
# from the end is increased by 1 (it is by definition not 9 as we have defined the digits like that.)

def main():
    t = int(input())
    
    while t > 0:
        print(add_one())
        t -= 1
        
    
def add_one():
    number = input("Enter your number ")
    string = ''
    # Calculate how many nines there are at the end of the number.
    for digit in number[::-1]:
        if digit == "9":
            string += digit
        else:
            break
    # Accordingly, calculate how to add one.
    
    # If there are no nines, simply add one to the last digit.
    # If there are nines, then change all the last digits to 0 and increase the previous digit by 1.
    # If they are all nines, then there is no previous digit. In this case, append a 1 
    # to the beginning of the string. This can be done by doing 1 + "0"*len(number) - this should do it.
    
    if len(string) == 0:
        last = int(number[-1])
        number = number[:-1]
        last += 1
        return number + str(last)
    
    elif len(string) < len(number):
        beg_slice = number[0:-len(string)-1]
        end_slice = number[-len(string)-1:]
        first_digit = int(end_slice[0])
        first_digit += 1
        first_digit = str(first_digit)
        return beg_slice + first_digit + "0"*len(string)
    
    else:
        return "1" + "0"*len(string)

if __name__ == "__main__":
    main()