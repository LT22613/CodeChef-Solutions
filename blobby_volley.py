"""
Blobby Volley Scores

Alice and Bob are playing a game of Blobby Volley. 

In this game, in each turn, one player is the server and the other player is the receiver.

Initially, Alice is the server, and Bob is the receiver.

If the server wins the point in this turn, their score increases by 1, and they remain as the server for the next turn.

But if the receiver wins the point in this turn, their score does not increase. But they become the server in the next turn.

In other words, your score increases only when you win a point when you are the server.

Please see the Sample Inputs and Explanation for more detailed explanation.

They start with a score of 0 each, and play N turns. 

The winner of each of those hands is given to you as a string consisting of 'A's and 'B's.

'A' denoting that Alice won that point, and 'B' denoting that Bob won that point. 

Your job is the find the score of both of them after the N turns.
"""
import sys

def main():
    t = int(input())
    
    while t > 0:
        # Determine the score using determine_score()
        points = determine_score()
        # Print each player's score using the scores dictionary
        for point in points.values():
            print(point, end = " ")
        print()
        t -= 1



def determine_score():
    try:
        # Define a dictionary to store Alice and Bob's score.
        points = {"A": 0, "B": 0}
        # Define Alice as the server, as she serves first.
        server = "A"
        # Take the number of turns N as input
        N = input()
        # Take the string representing the results, S, as input.
        S = input()
        
        # Iterate through the result string.
        for winner in S:
            if winner in ["A","B"]:
                # If the winner is the server, then if they win the point, their score is increased by 1.
                if winner == server:
                    points[winner] +=1
                # If the winner is not the server, they do not get a point, but they do become the server for the next point.
                else:
                    server = winner
            else:
                raise ValueError("String must only contain A and B")
        # Return the final updated dictionary score.
        return points
    
    
    except ValueError as e:
        print(e)
        sys.exit()


    
if __name__ == "__main__":
    main()