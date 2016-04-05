from flask import Flask, render_template, request, redirect, url_for, session
from flask.ext.socketio import SocketIO, emit
import os, uuid
import psycopg2
import psycopg2.extras
import sys
reload(sys)
sys.setdefaultencoding("UTF8")

app = Flask(__name__, static_url_path='')
app.secret_key = os.urandom(24).encode('hex')

socketio = SocketIO(app)

teamNames = []
regionNames = []
allgames = {}
allteams = {}
weeklist = ["week1", "week2", "week3", "week4", "week5", "week6", "week7", "week8", "week9", "week10", "week11", "week12"]

def getAllTeams():
    db = connectToDB()
    cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    for team in teamNames:
        cur.execute("SELECT id, class, gamesremaining, points, wins, losses, week1, week2, week3, week4, week5, week6, week7, week8, week9, week10, week11, week12 from teams where school=%s",(team,))
        line = cur.fetchone()
        allteams[line[0]] = {"name":team,"class":line[1],"remain":line[2], "points":line[3],"wins":line[4],"losses":line[5],
                            "week1":line[6],"week2":line[7],"week3":line[8],"week4":line[9],"week5":line[10],"week6":line[11],
                            "week7":line[12],"week8":line[13],"week9":line[14],"week10":line[15],"week11":line[16],"week12":line[17]}
    
def getAllGames():
    db = connectToDB()
    cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    for team in allteams:
        for week in weeklist:
            if (allteams[team][week] not in allgames.keys()) and (allteams[team][week]):
                allgames[allteams[team][week]] = {}
    for game in allgames.keys():
         cur.execute("SELECT homeid, awayid, homescore, awayscore, dist from games where id=%s",(game,))
         line = cur.fetchone()
         played = "N"
         if line[2]:
             played = "Y"
         allgames[game] = {"homeid":line[0],"awayid":line[1],"homescore":line[2],"awayscore":line[3],"played":played,"dist":line[4]}

def calcTeamMax(teamList, gameList, teamId):
    curPoints = float(teamList[teamId]["points"]) * (int(teamList[teamId]["wins"]) * int(teamList[teamId]["losses"]))
    for week in weeklist:
        if teamList[teamId][week]:
            thisGame = gameList[teamList[teamId][week]]
            if thisGame["played"] == "Y":
                pass
            else:
                pass
             
         
       
        
def connectToDB():
  connectionString = 'dbname=powerpoints user=pp password=pp host=localhost'
  try:
    return psycopg2.connect(connectionString)
  except:
    print("Can't connect to database")
    
def adminConnect():
    connectionString = 'dbname=powerpoints user=aduser password=aduser host=localhost'
    try:
        return psycopg2.connect(connectionString)
    except:
        print("Can't connect to database")
    
def getTeamNames():
    db = connectToDB()
    cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT school from teams where tracked = 'Y'")
    results = cur.fetchall()
    for tn in results:
        teamNames.append(tn[0])
    teamNames.sort()
    
def getRegionNames():
    db = connectToDB()
    cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT distinct region from conferences")
    results = cur.fetchall()
    for rn in results:
        regionNames.append(rn[0])
    regionNames.sort(reverse=True)
    
def updateRecords():
    db = adminConnect()
    cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    for team in teamNames:
        cur.execute("SELECT week1, week2, week3, week4, week5, week6, week7, week8, week9, week10, week11, week12 from teams where school=%s",(team,))
        results = cur.fetchone()
        wins = 0
        losses = 0
        i = 0
        remaining = 0
        while i < 12:
            if results[i] is not None:
                thisgame = getGameInfo(team, results[i])
                if thisgame["winloss"] == 'W':
                    wins += 1
                elif thisgame["winloss"] == "L":
                    losses += 1
                else:
                    remaining += 1
            i += 1
        query = ("update teams set wins="+ str(wins) +", losses=" + str(losses) + ", gamesremaining=" + str(remaining) + " where school='" + team + "';")
        cur.execute(query)
        db.commit()
        
def getGamesList(team, cur):
    gamesList = []
    i = 1
    while i <= 12:
        query=("select week"+str(i) + " from teams where school='" + team + "';")
        cur.execute(query)
        results = cur.fetchone()
        if str(results[0]) != "None":
            gamesList.append(results[0])
        i += 1
    return gamesList
    
def getOpponentsList(team, gamesList, cur):
    oppList = []
    for game in gamesList:
        query=("select school from teams where id=(select homeid from games where id=" + str(game) + ") union select school from teams where id=(select awayid from games where id=" + str(game) + ");")
        cur.execute(query)
        results=cur.fetchall()
        for name in results:
            if name != team:
                oppList.append(name)
    return oppList
        
def calculatePoints():
    db = adminConnect()
    cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    for team in teamNames:
        query="select class from teams where school='" + team + "';"
        cur.execute(query)
        teamClass = cur.fetchone()[0]
        gamesList = getGamesList(team, cur)
        totalPoints = 0
        gamesPlayed = 0
        for game in gamesList:
            info = getGameInfo(team, game)
            if (info["winloss"] == 'W') or (info["winloss"] == "L"):
                gamesPlayed += 1
                mult = 1
                if info["winloss"] == 'W':
                    mult = 2
                query="select class from teams where school='" + info["opp"] + "';"
                cur.execute(query)
                clss = cur.fetchone()[0]
                if teamClass > clss:
                    if info["dist"] == 'Y':
                        totalPoints += 2*(teamClass - clss)
                    else:
                        totalPoints += (teamClass - clss)
                query="select wins from teams where school='" + info["opp"] + "';"
                cur.execute(query)
                wins = cur.fetchone()[0]
                if info["winloss"] == 'W':
                    totalPoints += (2*clss) + 14 + (wins * 2)
                else:
                    totalPoints += (2*clss) + 2 + wins
        if gamesPlayed > 0:
            pp = (totalPoints * 1.0) / gamesPlayed
            query = "update teams set points=" + str(pp) + " where school='" + team + "';"
            cur.execute(query)
            db.commit()
        
    
def getTeamData(team):
    data = {}
    db = connectToDB()
    cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT school, mascot, class, district, confid, points, pmax, pmin, week1, week2, week3, week4, week5, week6, week7, week8, week9, week10, week11, week12 from teams where school=%s",(team,))
    results = cur.fetchone()
    data['school'] = results[0]
    data['mascot'] = results[1]
    data['class'] = results[2]
    data['district'] = results[3]
    data['conf'] = results[4]
    data['points'] = str(results[5])
    data['max'] = str(results[6])
    data['min'] = str(results[7])
    wins = 0
    losses = 0
    games = []
    i = 8
    while i < 20:
        thisgame = {}
        if results[i] is not None:
            thisgame = getGameInfo(team, results[i])
            if thisgame["winloss"] == 'W':
                wins += 1
            elif thisgame["winloss"] == "L":
                losses += 1
        else:
            thisgame = makeBye()
        thisgame['week'] = i-7
        games.append(thisgame)
        i += 1
    data['games'] = games
    data['record'] = str(wins) + "-" + str(losses)
    return data
    
def getTeamAdmin(teamName):
    data = getTeamData(teamName)
    gameList = []
    for game in data['games']:
        if game["opp"] != "Bye":
            oppName = game["opp"]
            winScore = ""
            losScore = ""
            if game["score"] != "":
                winScore = game["score"].split("-")[0]
                losScore = game["score"].split("-")[1]
            homeTeam = ""
            awayTeam = ""
            homeScore = ""
            awayScore = ""
            if game["loc"] == "at":
                homeTeam = oppName
                awayTeam = teamName
                if game["score"] != "":
                    if game["winloss"] == 'W':
                        awayScore = winScore
                        homeScore = losScore
                    else:
                        awayScore = losScore
                        homeScore = winScore
            else:
                homeTeam = teamName
                awayTeam = oppName
                if game["score"] != "":
                    if game["winloss"] == 'W':
                        awayScore = losScore
                        homeScore = winScore
                    else:
                        awayScore = winScore
                        homeScore = losScore
            finalGame = []
            finalGame.append(homeTeam)
            finalGame.append(awayTeam)
            finalGame.append(homeScore)
            finalGame.append(awayScore)
            finalGame.append(game["gameid"])
            gameList.append(finalGame)
    return gameList

def getGameInfo(team, gameNumber):
    data = {}
    db = connectToDB()
    cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT homeid, awayid, homescore, awayscore, day, dist from games where id=%s",(gameNumber,))
    results = cur.fetchone()
    dist=results[5]
    cur.execute("SELECT id from teams where school=%s",(team,))
    thisTeamNum = cur.fetchone()[0]
    isHome = False
    loc = "at"
    teamToIdentify = int(results[0])
    if int(results[0]) == thisTeamNum:
        isHome = True
        loc = "vs."
        teamToIdentify = int(results[1])
    cur.execute("SELECT school from teams where id=%s",(teamToIdentify,))
    otherTeam = cur.fetchone()[0]
    finalscore = ""
    winloss = ""
    score = ""
    if results[2] is not None:
        if int(results[2]) > int(results[3]):
            score = str(results[2]) + "-" + str(results[3])
            if isHome:
                winloss = "W"
            else:
                winloss = "L"
        else:
            score = str(results[3]) + "-" + str(results[2])
            if isHome:
                winloss = "L"
            else:
                winloss = "W"
    data["loc"]=loc
    data["opp"]=otherTeam
    data["score"]=score
    data["winloss"]=winloss
    data["dist"]=dist
    data["gameid"]=gameNumber
    return data
    
def getStandings(confName):
    # select * from teams join conferences on teams.confid=conferences.id where conferences.region='5A North';
    db = connectToDB()
    cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT teams.school, teams.wins, teams.losses, teams.points, teams.pmax, teams.pmin from teams join conferences on teams.confid=conferences.id where conferences.region=%s order by teams.points desc",(confName,))
    results = cur.fetchall()
    stand = []
    stand.append(confName)
    stand.append([])
    for row in results:
        rowDict = {}
        rowDict['name'] = row[0]
        rowDict['wins'] = row[1]
        rowDict['losses'] = row[2]
        rowDict['points'] = row[3]
        rowDict['max'] = row[4]
        rowDict['min'] = row[5]
        stand[1].append(rowDict)
    return stand
    
def makeBye():
    data = {}
    data["loc"] = ""
    data["opp"] = "Bye"
    data["score"] = ""
    data["winloss"] = ""
    return data

def getWeekGames(week):
    games = []
    db = connectToDB()
    cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    query = "select distinct week" + str(week) + " from teams where week" + str(week) + " > 0;"
    cur.execute(query)
    results = cur.fetchall()
    for game in results:
        query = "select homeid, awayid, homescore, awayscore from games where id="+str(game[0])
        cur.execute(query)
        gameData = cur.fetchone()
        query = "select school from teams where id=" + str(gameData[0])
        cur.execute(query)
        names = cur.fetchall()
        thisGame = []
        thisGame.append(names[0][0])
        query = "select school from teams where id=" + str(gameData[1])
        cur.execute(query)
        names = cur.fetchall()
        thisGame.append(names[0][0])
        
        if gameData[2] == None:
            thisGame.append("")
            thisGame.append("")
        else:
            thisGame.append(gameData[2])
            thisGame.append(gameData[3])
        thisGame.append(game)
        games.append(thisGame)
    return games
    
def updateAScore(gameId, hscore, ascore):
    db = adminConnect()
    cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    query = "select homescore, awayscore from games where id=" + gameId
    cur.execute(query)
    game = cur.fetchone()
    if (game[0] == None) or (game[0] == None) or (int(game[0]) != int(hscore)) or (int(game[1]) != int(ascore)):
        query = "update games set homescore=" + hscore + ", awayscore=" + ascore + " where id=" + gameId
        cur.execute(query)
        db.commit()

@app.route('/')
def mainIndex():
    session['teamToLoad'] = ''
    if len(teamNames) == 0:
        getTeamNames()
    if len(regionNames) == 0:
        getRegionNames()
    return render_template('index.html', teamnames=teamNames, regionnames=regionNames)

@app.route('/scenario')
def scenSession():
    print("I'm here!")
    session['uuid']=uuid.uuid1()
    getAllTeams()
    getAllGames()
    return render_template('scenario.html', uid=session['uuid'])
    
    
@app.route('/team', methods=['GET'])
def new_view():
    if len(teamNames) == 0:
        getTeamNames()
    if len(regionNames) == 0:
        getRegionNames()
    teamName = request.args.get('tn')
    teamData = getTeamData(teamName)
    return render_template('team.html', teamnames=teamNames, regionnames=regionNames, teamData=teamData)
    
@app.route('/stand', methods=['GET'])
def new_standview():
    if len(teamNames) == 0:
        getTeamNames()
    if len(regionNames) == 0:
        getRegionNames()
    regionName = request.args.get('rn')
    stanData = getStandings(regionName)
    return render_template('standings.html', teamnames=teamNames, regionnames=regionNames, stanData=stanData)
    
@app.route('/admin')
def adminPage():
    if len(teamNames) == 0:
        getTeamNames()
    if len(regionNames) == 0:
        getRegionNames()
    return render_template('admin.html', teamnames=teamNames, regionnames=regionNames)
       
@socketio.on('connect', namespace='/points')
def makeConnection(): 
    if len(teamNames) == 0:
        getTeamNames()
    if len(regionNames) == 0:
        getRegionNames() 
        
@socketio.on('fetchweek', namespace='/points')
def fetchweek(weekNum):
    data = getWeekGames(weekNum)
    params = []
    params.append(data)
    params.append(int(weekNum))
    emit('displayweek', params)
    
@socketio.on('fetchTeam', namespace='/points')
def fetchteam(teamName):
    data = getTeamAdmin(teamName)
    params = []
    params.append(data)
    params.append(teamName)
    emit('displayTeamAdmin',params)
    
@socketio.on('viewTeam', namespace='/points')
def viewTeam(teamName):
    session['teamToLoad'] = teamName
    params = [{'url':'/team'},teamName]
   # emit('teamredirect', teamName, {'url': '/team'})
    emit('teamredirect', params)
    
@socketio.on('viewStand', namespace='/points')
def viewStand(regionName):
    params = [{'url':'/stand'},regionName]
    emit('standredirect', params)
    
@socketio.on('scenClick', namespace='/points')
def scenario():
    print("Made it in here!")
    params=[{'url':'/scenario'}]
    emit('scenarioredirect', params)
    
@socketio.on('admin', namespace='/points')
def admin(un, pw):
    db = connectToDB()
    cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("select * from users where name = %s and password=crypt(%s, password)",(un,pw))
    if cur.fetchone():
        emit('adminredirect',{'url':'/admin'})
    else:
        emit('logInFail')
        
@socketio.on('commit', namespace='/points')
def commit():
    updateRecords()
    calculatePoints()
    emit('adminredirect',{'url':'/admin'})

@socketio.on('updateWeekScores', namespace='/points')
def updateWeekScores(scoresAr):
    for line in scoresAr:
        gameId = line[0]
        hscore = line[1]
        ascore = line[2]
        updateAScore(gameId, hscore, ascore)
    emit('adminredirect',{'url':'/admin'})

# start the server
if __name__ == '__main__':
        socketio.run(app, host=os.getenv('IP', '0.0.0.0'), port =int(os.getenv('PORT', 8080)), debug=True)
