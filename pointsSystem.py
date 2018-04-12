### ================================================================================
### the functions below calculate fantasy points for players' performance...
### ...in batting, bowling and fieding
### The fantasy points sytem followed is shown below...
#-----------
## Batting
#-----------
#• 1 point for 2 runs scored
#• Additional 5 points for half century
#• Additional 10 points for century
#• 2 points for strike rate (runs/balls faced) of 80-100
#• Additional 4 points for strike rate>100
#• 1 point for hitting a boundary (four) and 2 points for over boundary (six)
#-----------
## Bowling
#-----------
# • 10 points for each wicket
# • Additional 5 points for three wickets per innings
# • Additional 10 points for 5 wickets or more in innings
# • 4 points for economy rate (runs given per over) between 3.5 and 4.5
# • 7 points for economy rate between 2 and 3.5
# • 10 points for economy rate less than 2
#-----------
## Fielding
#-----------
# • 10 points each for catch/stumping/
### ================================================================================

def batpoints(runs, balls, fours, sixes):
    batpoints = (runs/2) + (fours) + (sixes*2)

    if runs >= 100:
        batpoints += 10
    elif runs >= 50:
        batpoints += 5
    else:
        batpoints += 0

    if runs/balls*100 > 100:
        batpoints += 4
    elif runs/balls*100 >= 80 and runs/balls*100 <= 100:
        batpoints += 2
    else:
        batpoints += 0

    return batpoints


def bowlpoints(wkts, overs, runs):
    bowlpoints = wkts*10

    if wkts >= 5:
        bowlpoints += 10
    elif wkts >= 3:
        bowlpoints += 5
    else:
        bowlpoints = bowlpoints

    if runs/overs <2:
        bowlpoints += 10
    elif runs/overs >=2 and runs/overs < 3.5:
        bowlpoints += 7
    elif runs/overs >= 3.5 and runs/overs < 4.5:
        bowlpoints += 4
    else:
        bowlpoints = bowlpoints

    return bowlpoints

def fieldpoints(field):
    fieldpoints = field*10
    return fieldpoints

