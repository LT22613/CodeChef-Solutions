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
    x = int(input())
    results = input()
    
    carlsen_wins = results.count('C')
    chef_wins = results.count('N')
    
    if carlsen_wins > chef_wins:
        return 60 * x
    elif carlsen_wins == chef_wins:
        return 55 * x
    else:
        return 40 * x
    
def main():
    t = int(input())
    while t > 0:
        print(calculate_prize())
        t-=1
    
if __name__ == "__main__":
    main()
    