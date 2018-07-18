from flask import Flask, session, render_template, request, redirect, g, url_for
import sqlite3
import os
import uuid
from datetime import datetime, timedelta


app = Flask(__name__)

def database(db_qery):
    try:
        conn = sqlite3.connect("C:\\Users\mku-center\Downloads\db.db")
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

@app.route('/mbdou', methods=['GET', 'POST'])
def mbdou():
    if request.method == 'GET':
        db_qery = 'SELECT * FROM data'
        data = database(str(db_qery))
        uuidtest = uuid.uuid4()
        return render_template('mbdou_lgot_pit.html', data=data, uuidtest=uuidtest)
    else:
        pass

@app.route('/1', methods=['GET', 'POST'])
def one():
    if request.method == 'GET':
        db_qery = 'SELECT * FROM data'
        data = database(str(db_qery))
        uuidtest = uuid.uuid4()
        return render_template('1-4.html', data=data, uuidtest=uuidtest)
    else:
        pass

@app.route('/cat', methods=['GET', 'POST'])
def cat():
    if request.method == 'GET':
        db_qery = 'SELECT * FROM data'
        data = database(str(db_qery))
        for d in data:
            v = ''
            if d[9].upper() == 'ДЕТИ СИРОТЫ':
                v = '3b28a899-5448-46c6-8e22-bc3128069322'
            elif d[9].upper() == 'ДЕТИ ОСТАВШИЕСЯ БЕЗ ПОПЕЧЕНИЯ РОДИТЕЛЕЙ' or d[9].upper() == 'ДЕТИ-СИРОТЫ И ДЕТИ, ОСТАВШИЕСЯ БЕЗ ПОПЕЧЕНИЯ РОДИТЕЛЕЙ':
                v = '9e29536a-c85b-42f1-902d-5c49d06b06a4'
            elif d[9].upper() == 'ДЕТИ С ОВЗ' or d[9].upper() == 'ДЕТИ-ИНВАЛИДЫ И ДЕТИ С ОГРАНИЧЕННЫМИ ВОЗМОЖНОСТЯМИ ЗДОРОВЬЯ, ТО ЕСТЬ ИМЕЮЩИЕ НЕДОСТАТКИ В ФИЗИЧЕСКОМ И (ИЛИ) ПСИХИЧЕСКОМ РАЗВИТИИ, ПРИ ОТСУТСТВИИ МЕДИЦИНСКИХ ПРОТИВОПОКАЗАНИЙ И СПОСОБНЫХ К САМООБСЛУЖИВАНИЮ':
                v = '7ec196dd-7f6b-492d-8082-e1219e67ab58'
            elif d[9].upper() == 'ДЕТИ ИНВАЛИДЫ':
                v = 'afd030c1-3460-4f55-8464-1dbf448c5018'
            elif d[9].upper() == 'ДЕТИ ИЗ МНОГОДЕТНЫХ ИЛИ НЕПОЛНЫХ СЕМЕЙ' or d[9].upper() == 'ДЕТИ, ПРОЖИВАЮЩИЕ В МАЛОИМУЩИХ (МАЛООБЕСПЕЧЕННЫХ) СЕМЬЯХ':
                v = '8856c07e-e4cf-453a-8a3d-c657a2caf1ab'
            else:
                print('no')
            db_qery = 'UPDATE data SET column10="%s" WHERE column1="%s"' % (str(v), str(d[0]))
            data = database(str(db_qery))
        return str('yeap')

@app.route('/cat2', methods=['GET', 'POST'])
def cat2():
    if request.method == 'GET':
        db_qery = 'SELECT * FROM data'
        data = database(str(db_qery))
        for d in data:
            v = ''
            if d[9].upper() == 'ДЕТИ ИНВАЛИДЫ':
                v = '969c2c6c-dcf3-4ad3-9484-77829da9e634'
            elif d[9].upper() == 'ДЕТИ С ОВЗ':
                v = 'bd865cd8-1db3-42c5-a86c-9ee4193a5758'
            elif d[9].upper() == 'ДЕТИ СИРОТЫ':
                v = '390f9ba1-0e45-442f-b3ef-b2f9e9ff956f'
            elif d[9].upper() == 'ДЕТИ ОСТАВШИЕСЯ БЕЗ ПОПЕЧЕНИЯ РОДИТЕЛЕЙ':
                v = 'cb386bcb-1f16-4987-8668-bd127c6afff2'
            else:
                print('no')
            db_qery = 'UPDATE data SET column10="%s" WHERE column1="%s"' % (str(v), str(d[0]))
            data = database(str(db_qery))
        return str('yeap')

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
    
@app.route('/new2', methods=['GET', 'POST'])
def new2():
    if request.method == 'GET':
        db_qery = 'SELECT * FROM data'
        data = database(str(db_qery))
        for d in data:
            v = str(uuid.uuid4())
            db_qery = 'UPDATE data SET column13="%s" WHERE column1="%s"' % (str(v), str(d[0]))
            data = database(str(db_qery))            
        return str(d[0])
    else:
        pass


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD']=True
    app.run(debug=True,use_reloader=True)

