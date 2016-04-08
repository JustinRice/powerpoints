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
         cur.execute("SELECT id, homeid, awayid, homescore, awayscore, dist from games where id=%s",(game,))
         line = cur.fetchone()
         played = "N"
         if line[3]:
             played = "Y"
         allgames[game] = {"id":line[0],"homeid":line[1],"awayid":line[2],"homescore":line[3],"awayscore":line[4],"played":played,"dist":line[5]}

def getGamesThatMatter(teamId, teamList, gameList):
    gamesThatMatter = []
    opponentsList = []
    for week in weeklist:
        if teamList[teamId][week]:
            thisGame = gameList[teamList[teamId][week]]
            home = thisGame["homeid"]
            away = thisGame["awayid"]
            if (home != teamId) and (home not in opponentsList):
                if home in teamList.keys():
                    opponentsList.append(home)
            if (away != teamId) and (away not in opponentsList):
                if away in teamList.keys():
                    opponentsList.append(away)
            if thisGame["played"] == "N":
                gamesThatMatter.append(teamList[teamId][week])
    for opponent in opponentsList:
        for week in weeklist:
            if opponent in teamList.keys():
                if teamList[opponent][week]:
                    thisGame = gameList[teamList[opponent][week]]
                    if (thisGame["played"] == "N") and (thisGame["id"] not in gamesThatMatter):
                        gamesThatMatter.append(thisGame["id"])
    return [gamesThatMatter,opponentsList]            
        


def calcTeamMax(teamList, gameList, teamId):
    curPoints = float(teamList[teamId]["points"]) * (int(teamList[teamId]["wins"]) * int(teamList[teamId]["losses"]))
    gaopp = getGamesThatMatter(teamId, teamList, gameList)
    gtm = gaopp[0]
    opps = gaopp[1]
    teamCp = {}
    gameCp = {}
    
    for key in teamList.keys():
        teamCp[key] = teamList[key]
    for key in gameList.keys():
        gameCp[key] = gameList[key]
    thisClass = teamCp[teamId]["class"]    
    for game in gtm:
        home = gameCp[game]["homeid"]
        away = gameCp[game]["awayid"]
        if home==teamId:
            gameCp[game]["homescore"] = 1
            gameCp[game]["awayscore"] = 0
            gameCp[game]["played"] = 'Y'
            if gameCp[game]["awayid"] in teamCp.keys():
                teamCp[gameCp[game]["awayid"]]["losses"] += 1
            teamCp[teamId]["wins"] += 1
        elif away==teamId:
            gameCp[game]["homescore"] = 0
            gameCp[game]["awayscore"] = 1
            gameCp[game]["played"] = 'Y'
            if "homeid" in gameCp[game].keys():
                if gameCp[game]["homeid"] in teamCp.keys():
                    teamCp[gameCp[game]["homeid"]]["losses"] += 1
            teamCp[teamId]["wins"] += 1
        else:
            playedHome = False
            playedRoad = False
            if gameCp[game]["awayid"] in opps:
                playedRoad = True
            if gameCp[game]["homeid"] in opps:
                playedHome = True    
            if playedHome and not playedRoad:
                gameCp[game]["homescore"] = 1
                gameCp[game]["awayscore"] = 0
                gameCp[game]["played"] = 'Y'
                teamCp[gameCp[game]["homeid"]]["wins"] += 1
            if playedRoad and not playedHome:
                gameCp[game]["homescore"] = 0
                gameCp[game]["awayscore"] = 1
                gameCp[game]["played"] = 'Y'
                teamCp[gameCp[game]["awayid"]]["wins"] += 1  
    for game in gtm:
        if gameCp[game]["played"] == 'N':
            gameToFix = gameCp[game]
            oppH = gameCp[game]["homeid"]
            oppR = gameCp[game]["awayid"]
            beatHome = False
            beatRoad = False
            homeId = gameCp[game]["homeid"]
            awayId = gameCp[game]["awayid"]
            for week in weeklist:
                if teamCp[teamId][week]:
                    thisGame = gameCp[teamCp[teamId][week]]
                    if (thisGame["homeid"] == oppH and thisGame["awayid"] == teamId) or (thisGame["awayid"] == oppH and thisGame["homeid"] == teamId):
                        wasHome = False
                        if thisGame["homeid"] == teamId:
                            wasHome = True
                        homeWon = False
                        if thisGame["homescore"] > thisGame["awayscore"]:
                            homeWon = True
                        if wasHome and homeWon:
                            beatHome = True
                        elif (not wasHome and not homeWon):
                            beatHome = True
                    if (thisGame["homeid"] == oppR and thisGame["awayid"] == teamId) or (thisGame["awayid"] == oppR and thisGame["homeid"] == teamId):
                        wasHome = False
                        if thisGame["homeid"] == teamId:
                            wasHome = True
                        homeWon = False
                        if thisGame["homescore"] > thisGame["awayscore"]:
                            homeWon = True
                        if wasHome and homeWon:
                            beatRoad = True
                        elif (not wasHome and not homeWon):
                            beatRoad = True
            if (beatHome and beatRoad) or (beatHome and not beatRoad) or (not beatHome and not beatRoad):
                gameToFix["homescore"] = 1
                gameToFix["awayscore"] = 0
                gameToFix["played"] = 'Y'
                teamCp[homeId]["wins"] += 1
                teamCp[awayId]["losses"] += 1
            else:
                gameToFix["homescore"] = 0
                gameToFix["awayscore"] = 1
                gameToFix["played"] = 'Y'
                teamCp[awayId]["wins"] += 1
                teamCp[homeId]["losses"] += 1
    maxPoints = 0
    for week in weeklist:
        if teamCp[teamId][week]:
            thisGame = gameCp[teamCp[teamId][week]]
            isHome = False
            if thisGame["homeid"] == teamId:
                isHome = True
            homeWon = False
            if thisGame["homescore"] > thisGame["awayscore"]:
                homeWon = True
            oppClass = ""
            oppWins = ""
            if isHome:
                if thisGame["awayid"] in teamCp.keys():
                    oppClass = teamCp[thisGame["awayid"]]["class"]
                    oppWins = teamCp[thisGame["awayid"]]["wins"]
                else:
                    oppClass = 3
                    oppWins = 0
                if homeWon:
                    maxPoints += (2*oppClass) + 14 + (oppWins * 2)
                else:
                    maxPoints += (2*oppClass) + 2 + oppWins
            else:
                if thisGame["homeid"] in teamCp.keys():
                    oppClass = teamCp[thisGame["homeid"]]["class"]
                    oppWins = teamCp[thisGame["homeid"]]["wins"]
                else:
                    oppClass = 3
                    oppWins = 0
                if homeWon:
                    maxPoints += (2*oppClass) + 2 + oppWins
                else:
                    maxPoints += (2*oppClass) + 14 + (oppWins * 2)
            if thisClass > oppClass:
                if thisGame["dist"] == 'Y':
                    maxPoints += 2*(thisClass - oppClass)
                else:
                    maxPoints += (thisClass - oppClass)
    
    totalGames = teamCp[teamId]["wins"] + teamCp[teamId]["losses"]
    if not (totalGames > 0):
        totalGames = 10
    maxPoints = (maxPoints * 1.0)/ totalGames  
    maxPoints = maxPoints * 100
    finPoints = int(maxPoints)
    finPoints = (finPoints * 1.0) / 100
    print finPoints
    return finPoints
    
    
def calcTeamMin(teamList, gameList, teamId):
    curPoints = float(teamList[teamId]["points"]) * (int(teamList[teamId]["wins"]) * int(teamList[teamId]["losses"]))
    gaopp = getGamesThatMatter(teamId, teamList, gameList)
    gtm = gaopp[0]
    opps = gaopp[1]
    teamCp = {}
    gameCp = {}
    
    for key in teamList.keys():
        teamCp[key] = teamList[key]
    for key in gameList.keys():
        gameCp[key] = gameList[key]
    thisClass = teamCp[teamId]["class"]    
    for game in gtm:
        home = gameCp[game]["homeid"]
        away = gameCp[game]["awayid"]
        if home==teamId:
            gameCp[game]["homescore"] = 0
            gameCp[game]["awayscore"] = 1
            gameCp[game]["played"] = 'Y'
            if gameCp[game]["awayid"] in teamCp.keys():
                teamCp[gameCp[game]["awayid"]]["wins"] += 1
            teamCp[teamId]["losses"] += 1
        elif away==teamId:
            gameCp[game]["homescore"] = 1
            gameCp[game]["awayscore"] = 0
            gameCp[game]["played"] = 'Y'
            if "homeid" in gameCp[game].keys():
                if gameCp[game]["homeid"] in teamCp.keys():
                    teamCp[gameCp[game]["homeid"]]["wins"] += 1
            teamCp[teamId]["losses"] += 1
        else:
            playedHome = False
            playedRoad = False
            if gameCp[game]["awayid"] in opps:
                playedRoad = True
            if gameCp[game]["homeid"] in opps:
                playedHome = True    
            if playedHome and not playedRoad:
                gameCp[game]["homescore"] = 0
                gameCp[game]["awayscore"] = 1
                gameCp[game]["played"] = 'Y'
                teamCp[gameCp[game]["homeid"]]["losses"] += 1
            if playedRoad and not playedHome:
                gameCp[game]["homescore"] = 1
                gameCp[game]["awayscore"] = 0
                gameCp[game]["played"] = 'Y'
                teamCp[gameCp[game]["awayid"]]["losses"] += 1  
    for game in gtm:
        if gameCp[game]["played"] == 'N':
            gameToFix = gameCp[game]
            oppH = gameCp[game]["homeid"]
            oppR = gameCp[game]["awayid"]
            beatHome = False
            beatRoad = False
            homeId = gameCp[game]["homeid"]
            awayId = gameCp[game]["awayid"]
            for week in weeklist:
                if teamCp[teamId][week]:
                    thisGame = gameCp[teamCp[teamId][week]]
                    if (thisGame["homeid"] == oppH and thisGame["awayid"] == teamId) or (thisGame["awayid"] == oppH and thisGame["homeid"] == teamId):
                        wasHome = False
                        if thisGame["homeid"] == teamId:
                            wasHome = True
                        homeWon = False
                        if thisGame["homescore"] > thisGame["awayscore"]:
                            homeWon = True
                        if wasHome and homeWon:
                            beatHome = True
                        elif (not wasHome and not homeWon):
                            beatHome = True
                    if (thisGame["homeid"] == oppR and thisGame["awayid"] == teamId) or (thisGame["awayid"] == oppR and thisGame["homeid"] == teamId):
                        wasHome = False
                        if thisGame["homeid"] == teamId:
                            wasHome = True
                        homeWon = False
                        if thisGame["homescore"] > thisGame["awayscore"]:
                            homeWon = True
                        if wasHome and homeWon:
                            beatRoad = True
                        elif (not wasHome and not homeWon):
                            beatRoad = True
            if (beatHome and beatRoad) or (beatHome and not beatRoad) or (not beatHome and not beatRoad):
                gameToFix["homescore"] = 0
                gameToFix["awayscore"] = 1
                gameToFix["played"] = 'Y'
                teamCp[homeId]["losses"] += 1
                teamCp[awayId]["wins"] += 1
            else:
                gameToFix["homescore"] = 1
                gameToFix["awayscore"] = 0
                gameToFix["played"] = 'Y'
                teamCp[awayId]["losses"] += 1
                teamCp[homeId]["wins"] += 1
    maxPoints = 0
    for week in weeklist:
        if teamCp[teamId][week]:
            thisGame = gameCp[teamCp[teamId][week]]
            isHome = False
            if thisGame["homeid"] == teamId:
                isHome = True
            homeWon = False
            if thisGame["homescore"] > thisGame["awayscore"]:
                homeWon = True
            oppClass = ""
            oppWins = ""
            if isHome:
                if thisGame["awayid"] in teamCp.keys():
                    oppClass = teamCp[thisGame["awayid"]]["class"]
                    oppWins = teamCp[thisGame["awayid"]]["wins"]
                else:
                    oppClass = 3
                    oppWins = 0
                if homeWon:
                    maxPoints += (2*oppClass) + 14 + (oppWins * 2)
                else:
                    maxPoints += (2*oppClass) + 2 + oppWins
            else:
                if thisGame["homeid"] in teamCp.keys():
                    oppClass = teamCp[thisGame["homeid"]]["class"]
                    oppWins = teamCp[thisGame["homeid"]]["wins"]
                else:
                    oppClass = 3
                    oppWins = 0
                if homeWon:
                    maxPoints += (2*oppClass) + 2 + oppWins
                else:
                    maxPoints += (2*oppClass) + 14 + (oppWins * 2)
            if thisClass > oppClass:
                if thisGame["dist"] == 'Y':
                    maxPoints += 2*(thisClass - oppClass)
                else:
                    maxPoints += (thisClass - oppClass)
    
    totalGames = teamCp[teamId]["wins"] + teamCp[teamId]["losses"]
    if not (totalGames > 0):
        totalGames = 10
    maxPoints = (maxPoints * 1.0)/ totalGames  
    maxPoints = maxPoints * 100
    finPoints = int(maxPoints)
    finPoints = (finPoints * 1.0) / 100
    return finPoints
             
       
        
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
    
@socketio.on('updatepmax', namespace='/points')
def updatepmax():
    getAllTeams()
    getAllGames()
    for teamid in allteams.keys():
        maxP = calcTeamMax(allteams, allgames, teamid)
        if maxP > 40:
            maxP = 34.3
        db = adminConnect()
        cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "update teams set pmax=" + str(maxP) + " where id=" + str(teamid) + ";"
        cur.execute(query)
        db.commit()
        
@socketio.on('updatepmin', namespace='/points')
def updatepmin():
    getAllTeams()
    getAllGames()
    for teamid in allteams.keys():
        minP = calcTeamMin(allteams, allgames, teamid)
        db = adminConnect()
        cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "select pmax from teams where id=" + str(teamid) + ";"
        cur.execute(query)
        result = cur.fetchone()
        mintest = result[0]
        if minP > mintest:
            minP = mintest / 4
        query = "update teams set pmin=" + str(minP) + " where id=" + str(teamid) + ";"
        cur.execute(query)
        db.commit()
    

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
