from flask import Flask, render_template, request, redirect, url_for, session
import os
import psycopg2
import psycopg2.extras
import sys
reload(sys)
sys.setdefaultencoding("UTF8")

app = Flask(__name__)
app.secret_key = os.urandom(24).encode('hex')


def connectToDB():
  connectionString = 'dbname=session user=searcher password=search host=localhost'
  print connectionString
  try:
    return psycopg2.connect(connectionString)
  except:
    print("Can't connect to database")
    

@app.route('/')
def mainIndex():
    return render_template('index.html')
    
    

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=8080)
