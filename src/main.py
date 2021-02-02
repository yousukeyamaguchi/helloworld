import os
import sqlalchemy

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  driver_name = 'mysql+pymysql'
  db_user = "root"
  db_password = "12345678"
  db_name = "guestbook"
  db_config = {
    "pool_size": 5,
    "max_overflow": 2,
    "pool_timeout": 30,  # 30 seconds
    "pool_recycle": 1800  # 30 minutes
  }

  if(os.environ.get('PORT')):
    connection_name = "flaskrun:asia-northeast1:myinstance"
    query_string = dict({"unix_socket": "/cloudsql/{}".format(connection_name)})
    db = sqlalchemy.create_engine(
      sqlalchemy.engine.url.URL(
        drivername=driver_name,
        username=db_user,
        password=db_password,
        database=db_name,
        query=query_string,
      ),
      **db_config
    )
  else:
    print('=================== running local ===================')
    db = sqlalchemy.create_engine(
          # Equivalent URL:
          # mysql+pymysql://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
          sqlalchemy.engine.url.URL(
              drivername=driver_name,
              username=db_user,  # e.g. "my-database-user"
              password=db_password,  # e.g. "my-database-password"
              host="127.0.0.1",  # e.g. "127.0.0.1"
              port=3306,  # e.g. 3306
              database=db_name,  # e.g. "my-database-name"
          ),
          **db_config
    )

  stmt = sqlalchemy.text("INSERT INTO entries (guestName, content) values ('another guest', 'Also this one');")
  try:
    with db.connect() as conn:
      conn.execute(stmt)
  except Exception as e:
    # return 'fugafuga'
    return 'Error: {}'.format(str(e))
  return 'Hello! You wrote something into your database!\n'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
