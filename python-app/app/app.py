import os
import flask
import mysql.connector

application = flask.Flask(__name__)
application.debug = True

@application.route('/')
def hello_world():
  storage = Storage()
  storage.populate()
  score = storage.score()
  return "Hello Devops 123, %d!" % score

class Storage():
  def __init__(self):

    config = {
        'user': os.getenv('MYSQL_USERNAME'),
        'password': os.getenv('MYSQL_PASSWORD'),
        'host': os.getenv('MYSQL_PORT_3306_TCP_ADDR'),
        'port': int(os.getenv('MYSQL_PORT_3306_TCP_PORT')),
        'database': os.getenv('MYSQL_INSTANCE_NAME')
    }

    self.db = mysql.connector.connect(**config)

    cur = self.db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS scores(score INT)")

  def populate(self):
    cur = self.db.cursor()
    cur.execute("INSERT INTO scores(score) VALUES(1234)")

  def score(self):
    cur = self.db.cursor()
    cur.execute("SELECT * FROM scores")
    row = cur.fetchone()
    return row[0]

if __name__ == "__main__":
  application.run(host='0.0.0.0', port=3000)
