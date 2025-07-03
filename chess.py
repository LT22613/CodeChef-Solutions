"""
14 classical games are played out between Carlsen and Chef.
The total prize money is 100*x.
The points scored are as follows: 
Win - 2
Draw - 1
Loss - 0

The outright winner recieves 60*x
The loser then receives 40*x.

If they draw, Carlsen receives 55*x and Chef receives 45*x.

The number of test cases is given.
Then x is given - 100*x is the total prize money.
Then a string is given denoting who won each game.

C - Carlsen wins.
N - Carlsen loses.
D - They draw.

Create a program that accurately returns how much Carlsen wins after a given set of games.
"""

def calculate_prize():
    """Calculates the prize Magnus will receive at the end of the 14 games.

    Returns:
        int : Magnus's prize money.
    """
    # Take x as input.
    x = int(input())
    # Take the results as input in the form a string of length 14 containing Cs, Ns and Ds.
    results = input()
    
    # Count the number of Cs in the string to record Magnus's number of wins.
    carlsen_wins = results.count('C')
    # Count the number of Ns in the string to record Chef's number of wins.
    chef_wins = results.count('N')
    
    # If Magnus has more wins than Chef, he will receive 60*x as prize money.
    if carlsen_wins > chef_wins:
        return 60 * x
    # If Magnus has the same number of wins, he will recive 55*x as prize money.
    elif carlsen_wins == chef_wins:
        return 55 * x
    # If Magnus has less wins than Chef, he will receive 40*x as prize money.
    else:
        return 40 * x
    
def main():
    # Ask for the number of trials as input and convert to int.
    t = int(input())
    # Execute while loop for the specified number of trials.
    while t > 0:
        # Print the returned result of Magnus's prize money.
        print(calculate_prize())
        # Decrement t by 1 for each trial.
        t-=1

# Only execute this file if it is the main file being executed, as supposed to being imported.
if __name__ == "__main__":
    main()
    