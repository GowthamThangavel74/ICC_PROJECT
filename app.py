
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.sql.expression import update
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()



####  CRUD   Create(insert), Read(get), Update(put), Delete(Delete)   #########
#POST: to create data.
#GET: to read data.
#PUT: to update data.
#DELETE: to delete data.

engine = create_engine('sqlite:///lamp.db', echo = True)
meta = MetaData()

####  SQLAlchemy ORM #####

class Icc2(Base):
   __tablename__ = 'ICC'
   
   Job_id = Column(Integer, primary_key=True)
   Opening_Job = Column(String)
   Job_Des = Column(String)
   Aplication_counts = Column(Integer)
   Aplication_Viewed = Column(Integer)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()




# init app
app = Flask(__name__)

#########  UPDATE THE Table  ##############

@app.route('/api/put', methods=['PUT'])
def put():
    try:
        session.query(Icc2).filter(Icc2.Job_id == 1014).update({Icc2.Opening_Job:"MIS"}, synchronize_session = False)
        session.commit()
        return jsonify({'name': 'Updated Successfully'})

    except:
        return jsonify({'name': 'except'})


######### Delete The Table ############

@app.route('/api/dele', methods=['DELETE'])
def delet():
    try:
        x = session.query(Icc2).get(1019)
        session.delete(x)
        session.commit()
        return jsonify({'name': 'Delete Successfully'})

    except:
        return jsonify({'name': 'except'})


### Insert the Table ############

@app.route('/api/post', methods=['POST'])
def post():
    try:
        c1 = Icc2(Opening_Job = 'MIS', Job_Des = 'CHENNAI', Aplication_counts = '11', Aplication_Viewed='11')
        session.add(c1)
        session.commit()
        return jsonify({'name': 'Data Inseted'})  

    except:
        return jsonify({'name': 'except'})



######  GET THE DATA  #####

@app.route('/api', methods=['GET'])
def get():
    try:
       
        sqliteConnection = sqlite3.connect('lamp.db')
        cursor = sqliteConnection.cursor()
        # multiple tabe views   #######
        #s = select([students, addresses]).where(students.c.id == addresses.c.st_id)

        sqlite_out = """SELECT * FROM ICC;"""
        cursor.execute(sqlite_out)
        record = cursor.fetchall()
        cursor.close()
        return jsonify({'name': record})
       

    except sqlite3.Error as error:
        return jsonify({'name': error})



# Run sever
if __name__ == '__main__':
    app.run(debug=True)
