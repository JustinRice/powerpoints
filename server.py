import os, uuid
from flask.ext.socketio import SocketIO, emit
from flask_socketio import join_room, leave_room
from flask import Flask, session
import psycopg2
import psycopg2.extras

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)

messages = []
            
rooms = ['Lobby','Awesome People','Losers','Admins']
roomsList = [{'name':'Lobby', 'Link':'changeRoom()'}]
            
testVar = "Hi!"

users = {}
testUsers = []

def connectToDB():
  connectionString = 'dbname=sock2 user=sockuser password=sockuser host=localhost'
  #print connectionString
  try:
    return psycopg2.connect(connectionString)
  except:
    print("Can't connect to database")

@socketio.on('connect', namespace='/awesome')
def makeConnection():
    session['uuid']=uuid.uuid1()
    session['username']='new user'
   # print('connected')
    users[session['uuid']] = {'username':'New User'}
    db = connectToDB()
    cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    query = "select poster, post from posts where room = 'lobby'"
    cur.execute(query)
    results = cur.fetchall()
    for row in results:
        tmp = {'text':row[1], 'name':row[0]}
        emit('message',tmp)
    for user in testUsers:
        emit('users',user)
        
@socketio.on('login', namespace='/awesome')
def login():
    emit('login')
    
@socketio.on('logout', namespace='/awesome')
def logout():
    userName=users[session['uuid']]['username']
    userMsg = userName + " has logged out."
    tmp = {'text':userMsg, 'name': '***System***'}
    emit('message',tmp, broadcast=True)
    emit('removeuser',users[session['uuid']]['username'], broadcast=True)
    emit('loggedOut', broadcast=False)
    testUsers.remove(users[session['uuid']]['username'])
    
    
@socketio.on('logUser', namespace='/awesome')
def on_identify(name, password):
   # print('Made it here!')
   # print('identify ' + name)
    db = connectToDB()
    cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    query = "select * from users where name = '%s' and password=crypt('%s',password)" % (name, password)
    cur.execute(query)
    if cur.fetchone():
        if name not in testUsers:
            users[session['uuid']] = {'username':name}
            session['room']='lobby'
            join_room('lobby')
            
            logString = "%s has entered the room." %(name)
            logAppend = {'text': logString, 'name': '***System***'}
     #   print(logString)
            messages.append(logAppend)
     #   print(messages)
            testUsers.append(users[session['uuid']]['username'])
            emit('addUser', users[session['uuid']]['username'], broadcast=True)
            emit('loggedIn')
            emit('message', logAppend, broadcast=True, room='lobby')
        else:
            emit('logInFail')
    else:
        emit('logInFail')
        
@socketio.on('message', namespace='/awesome')
def new_message(message):
    tmp = {'text': message, 'name': users[session['uuid']]['username']}
    messages.append(tmp)
    emit('message', tmp, broadcast=True, room=session['room'])
    roomName = session['room']
    userName = users[session['uuid']]['username']
    query = "insert into posts (room, poster, post) values (%s,%s,%s)"
    db = connectToDB()
    cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(query, (roomName, userName, message))
    db.commit()
    
@socketio.on('changeRoom', namespace='/awesome')
def changeRoom(roomName):
    db = connectToDB()
    cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    name=users[session['uuid']]['username']
    query = "select %s from users where name = '%s'" % (roomName, name)
    cur.execute(query)
    answer = cur.fetchone()
    if answer[0] == 'N':
        logString = "You're not a member of the room %s" %(roomName)
        logAppend = {'text': logString, 'name': '***System***'}
        emit('message', logAppend, broadcast=False)
    else:
        leave_room(session['room'])
        join_room(roomName)
        session['room']=roomName
        logString = "Entering the room %s" %(roomName)
        logAppend = {'text': logString, 'name': '***System***'}
        emit('message', logAppend, broadcast=False)
        logString = "%s has entered the room." %(name)
        logAppend = {'text': logString, 'name': '***System***'}
        emit('message', logAppend, broadcast=True, room=session['room'])
        query = "select poster, post from posts where room ='%s'" %roomName
        cur.execute(query)
        results = cur.fetchall()
        if len(results) > 0:
            for row in results:
                tmp = {'text':row[1], 'name':row[0]}
                emit('message',tmp)

    
@socketio.on('search', namespace='/awesome')
def search(searchQ):      
    roomName = session['room']
    query = "select poster, post from posts where (post like '%" + searchQ + "%') and (room='" + roomName + "')"
    answers = []
    db = connectToDB()
    cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(query)
    rows = cur.fetchall()
    if len(rows) > 0:
        for row in rows:
            ans = {'text':row[1],'name':row[0]}
            answers.append(ans)
            
    query = "select poster, post from posts where (poster like '%" + searchQ + "%') and (room='" + roomName + "')"
    cur.execute(query)
    rows = cur.fetchall()
    if len(rows) > 0:
        for row in rows:
            ans = {'text':row[1],'name':row[0]}
            answers.append(ans)
    
    if len(answers) == 0:
        ans = {'text':'No results returned','name':'***System***'}
        emit('searchRes',ans)
    else:
        for row in answers:
            emit('searchRes',row)
    
    
@socketio.on('newUser', namespace='/awesome')
def search(newName, pw1, theseRooms):    
    query = "select name from users where name='%s'" % (newName)
    db = connectToDB()
    cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(query)
    checkName = cur.fetchall()
    if len(checkName) > 0:
        emit('newUserFail',"Invalid User Name")
    else:
        awesome="N"
        cool="N"
        regular="N"
        if "awesomepeople" in theseRooms:
            awesome="Y"
        if "coolpeople" in theseRooms:
            cool="Y"
        if "regularpeople" in theseRooms:
            regular="Y"
        query = "insert into users (name, password, awesomepeople, coolpeople, regularpeople) values ('%s', crypt('%s', gen_salt('bf')),'%s','%s','%s')" %(newName, pw1, awesome, cool, regular)
        cur.execute(query)
        db.commit()
        emit('madeNewUser')
    
@app.route('/')
def mainIndex():
  #  print 'in hello world'
    return app.send_static_file('index.html')
    

    


# start the server
if __name__ == '__main__':
        socketio.run(app, host=os.getenv('IP', '0.0.0.0'), port =int(os.getenv('PORT', 8080)), debug=True)
