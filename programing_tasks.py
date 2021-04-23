'''
Greed is a dice game played with five six-sided dice.
Your mission, should you choose to accept it, is to score a throw according to these rules.
You will always be given an array with five six-sided dice values.
 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
A single die can only be counted once in each roll.
For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.
'''
def score(dice):
    ones = dice.count(1)
    twos = dice.count(2)
    threes = dice.count(3)
    fours = dice.count(4)
    fives = dice.count(5)
    sixes = dice.count(6)
    point = 0
    if ones == 3:
        point += 1000
    if ones >3:
        point += 1000 + (ones-3)*100
    if ones <3 and ones>0:
        point += 100*ones
    if twos >= 3:
        point += 200
    if threes>=3:
        point += 300
    if fours >=3:
        point += 400
    if sixes>=3:
        point += 600
    if fives == 3:
        point+=500
    if fives > 3:
        point += 500 + (fives-3)*50
    if fives <3 and fives >0:
        point += 50*fives
    return point
