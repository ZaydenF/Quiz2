import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session
import os
import time

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
                                     #The value should be set on the server. 
                                     #To run locally, set in env.bat (env.sh on Macs) and include that file in gitignore so the secret key is not made public.

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/page1')
def renderPage1():
    session["start_time"] = time.time()
    return render_template('Page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    if "answer1" not in session:
        session["answer1"]=request.form['Name']
    return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    if "answer2" not in session:
        session["answer2"]=request.form['Name2']
    return render_template('page3.html')
@app.route('/page4',methods=['GET','POST'])
def renderPage4():
    if "answer3" not in session:
        session["answer3"]=request.form['Name3']
    session["end_time"] = time.time()
    time_taken = session["end_time"] - session["start_time"]
    finalScore=get_score()
    return render_template ('page4.html', grade=finalScore, time_taken=time_taken)

def get_score():
    scoreVal=0
    if session["answer1"]=="James Monroe":
        scoreVal+=1
    if session["answer2"]=="William Henry Harrison":
        scoreVal+=1
    if session["answer3"]=="JFK":
        scoreVal+=1
    return scoreVal
if __name__=="__main__":
    app.run(debug=False)
