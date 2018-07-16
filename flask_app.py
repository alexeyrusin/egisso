from flask import Flask, session, render_template, request, redirect, g, url_for
import sqlite3
import os
import uuid
from datetime import datetime, timedelta


app = Flask(__name__)

def database(db_qery):
    try:
        conn = sqlite3.connect('db.db')
        c = conn.cursor()
        c.execute(db_qery)
        data = c.fetchall()
        conn.commit()
        return data
    except Exception as error:
        return str(error)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        db_qery = 'SELECT * FROM data'
        data = database(str(db_qery))
        uuidtest = uuid.uuid4()
        return render_template('zero.html', data=data, uuidtest=uuidtest)
    else:
        pass

@app.route('/time', methods=['GET', 'POST'])
def time():
    if request.method == 'GET':
        db_qery = 'SELECT * FROM data'
        data = database(str(db_qery))
        for d in data:
            v = datetime.now()
            db_qery = 'UPDATE data SET column12="%s" WHERE column1="%s"' % (str(v), str(d[0]))
            data = database(str(db_qery))            
        return str(v)
    else:
        pass

@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'GET':
        db_qery = 'SELECT * FROM data'
        data = database(str(db_qery))
        vata = {}
        for d in data:
            v = str(uuid.uuid4())
            #db_qery = 'INSERT INTO data(column11) VALUES("%s") WHERE column1="%s"' % (str(v), str(d[0]))
            db_qery = 'UPDATE data SET column11="%s" WHERE column1="%s"' % (str(v), str(d[0]))
            data = database(str(db_qery))            
        return str(d[0])
    else:
        pass

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD']=True
    app.run(debug=True,use_reloader=True)

