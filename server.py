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


def connectToDB():
  connectionString = 'dbname=powerpoints user=pp password=pp host=localhost'
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
    
def getGameInfo(team, gameNumber):
    data = {}
    db = connectToDB()
    cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT homeid, awayid, homescore, awayscore, day, dist from games where id=%s",(gameNumber,))
    results = cur.fetchone()
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
    return data
    
def makeBye():
    data = {}
    data["loc"] = ""
    data["opp"] = "Bye"
    data["score"] = ""
    data["winloss"] = ""
    return data
        
  
@app.route('/')
def mainIndex():
    getGameInfo("Highland Springs", 1)
    session['teamToLoad'] = ''
    if len(teamNames) == 0:
        getTeamNames()
    return render_template('index.html', teamnames=teamNames)
    
@app.route('/team', methods=['GET'])
def new_view():
    if len(teamNames) == 0:
        getTeamNames()
    teamName = request.args.get('tn')
    teamData = getTeamData(teamName)
    return render_template('team.html', teamnames=teamNames, teamData=teamData)
       
@socketio.on('connect', namespace='/points')
def makeConnection(): 
    print('connected')   
    
@socketio.on('viewTeam', namespace='/points')
def viewTeam(teamName):
    session['teamToLoad'] = teamName
    params = [{'url':'/team'},teamName]
   # emit('teamredirect', teamName, {'url': '/team'})
    emit('teamredirect', params)
 

# start the server
if __name__ == '__main__':
        socketio.run(app, host=os.getenv('IP', '0.0.0.0'), port =int(os.getenv('PORT', 8080)), debug=True)
