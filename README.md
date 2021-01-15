

# for run :- 
python samanvay.py

# sample input :- 
2
A
B
C
D
E
F
F
A
C
B
D
E


# The Archeville Super-Archy Tournament

# problem details 

The Archeville super-archy tournament is a team archery tournament that happens once every four years. Every nation sends two of their best archers to the tournament, and the first team to reach 60 points wins. 
The archery board has 5 concentric circles - A, B, C, D and E, A being the innermost. A carries 5 points and E carries 1 point. 
Points for every circle increase by 1 at every round. For example, In the 4th round, A will carry 8 points while E will carry 4 points. Hitting outside the board (F) will always be 0. 
If both archers in a team hit the same circle in a round, a bonus 2 points are given to the team for synchronicity. 
The game finishes when one team reaches 60 points. 
If more than one team cross 60 points in a round, the team with the highest score wins. 

You have been hired to build the scoreboard for the contest. The first set of inputs will be the participating nations and their participants. The next input is the order in which the scores are coming in. This is followed by lines of input for each round. The scoreboard must be refreshed after each round with scores of each team, individual scores, and bonus points. The program stops once a team wins. 
