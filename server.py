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




def connectToDB():
  connectionString = 'dbname=session user=searcher password=search host=localhost'
  print connectionString
  try:
    return psycopg2.connect(connectionString)
  except:
    print("Can't connect to database")
  
@app.route('/')
def mainIndex():
#    return render_template('index.html')
    print('Im here.');
    return render_template('index.html')
    
@app.route('/team')
def new_view():
    return render_template('team.html')
        
@socketio.on('connect', namespace='/points')
def makeConnection(): 
    print('connected')   
    
@socketio.on('viewTeam', namespace='/points')
def viewTeam(teamName):
    emit('redirect', {'url': '/team'})
 

# start the server
if __name__ == '__main__':
        socketio.run(app, host=os.getenv('IP', '0.0.0.0'), port =int(os.getenv('PORT', 8080)), debug=True)
