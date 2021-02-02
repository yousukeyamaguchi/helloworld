import os
import sqlalchemy

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():

  # Set the following variables depending on your specific
  # connection name and root password from the earlier steps:
  connection_name = "flaskrun:asia-northeast1:myinstance"
  db_password = "12345678"
  db_name = "guestbook"

  db_user = "root"
  driver_name = 'mysql+pymysql'
  query_string = dict({"unix_socket": "/cloudsql/{}".format(connection_name)})

  db = sqlalchemy.create_engine(
    sqlalchemy.engine.url.URL(
      drivername=driver_name,
      username=db_user,
      password=db_password,
      database=db_name,
      query=query_string,
    ),
    pool_size=5,
    max_overflow=2,
    pool_timeout=30,
    pool_recycle=1800
  )

  stmt = sqlalchemy.text("INSERT INTO entries (guestName, content) values ('another guest', 'Also this one');")
  try:
    with db.connect() as conn:
      conn.execute(stmt)
  except Exception as e:
    return 'Error: {}'.format(str(e))
  return 'Hello! You wrote something into your database!\n'

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
