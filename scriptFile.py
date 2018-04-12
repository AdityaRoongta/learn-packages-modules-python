### ================================================================================
### This file contains the cricket performance of five players
### The performance for each player is stored as a dictionary object for each player
### The code below the dictionaries calcullates the fantasy points for each player...
### ...based on the pointsSystem deviced in the other file (pointsSystem.py), ...
### ... and then finally displays the name of the best player based on the points caculated
### ================================================================================

p1 = {'name':'Virat Kohli', 'role':'bat', 'runs':112, '4':10, '6':0, 'balls':119, 'field':0}
p2 = {'name':'du Plessis', 'role':'bat', 'runs':119, '4':11, '6':2, 'balls':112, 'field':0}
p3 = {'name':'Bhuvneshwar Kumar', 'role':'bowl', 'wkts':1, 'overs':10, 'runs':71, 'field':1}
p4 = {'name':'Yuzvendra Chahal', 'role':'bowl', 'wkts':2, 'overs':10, 'runs':45, 'field':0}
p5 = {'name':'Kuldeep Yadav', 'role':'bowl', 'wkts':3, 'overs':10, 'runs':34, 'field':0}

playersList = [p1,p2,p3,p4,p5]

def bestPlayer():
    import pointsSystem
    playersPoints = ({},{},{},{},{})
    for p in playersList:
        if p['role'] == 'bat':
            playersPoints[playersList.index(p)]['name'] = p['name']
            playersPoints[playersList.index(p)]['batpoints'] = pointsSystem.batpoints(p['runs'], p['balls'], p['4'], p['6'])
            playersPoints[playersList.index(p)]['fieldpoints'] = pointsSystem.fieldpoints(p['field'])
            playersPoints[playersList.index(p)]['totalpoints'] = pointsSystem.batpoints(p['runs'], p['balls'], p['4'], p['6']) + pointsSystem.fieldpoints(p['field'])
        else:
            playersPoints[playersList.index(p)]['name'] = p['name']
            playersPoints[playersList.index(p)]['bowlpoints'] = pointsSystem.bowlpoints(p['wkts'], p['overs'], p['runs'])
            playersPoints[playersList.index(p)]['fieldpoints'] = pointsSystem.fieldpoints(p['field'])
            playersPoints[playersList.index(p)]['totalpoints'] = pointsSystem.bowlpoints(p['wkts'], p['overs'], p['runs']) + pointsSystem.fieldpoints(p['field'])
    totalpoints = []
    for d in playersPoints:
        totalpoints.append(d['totalpoints'])
    return "The best player is {}".format(playersPoints[totalpoints.index(max(totalpoints))]['name'])

bestPlayer()
