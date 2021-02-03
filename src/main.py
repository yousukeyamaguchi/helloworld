import os
import sqlalchemy
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    driver_name = 'mysql+pymysql'
    db_user = os.environ.get('DB_USER')
    db_pass = os.environ.get('DB_PASS')
    db_name = os.environ.get('DB_NAME')
    db_config = {
        'pool_size': 5,
        'max_overflow': 2,
        'pool_timeout': 30,  # 30 seconds
        'pool_recycle': 1800  # 30 minutes
    }

    if os.environ.get('ENV') == 'dev':
        print('=================== running local ===================')
        db = sqlalchemy.create_engine(
            sqlalchemy.engine.url.URL(
                drivername=driver_name,
                username=db_user,
                password=db_pass,
                host='127.0.0.1',
                port=3306,
                database=db_name
            ),
            **db_config
        )
        stmt = sqlalchemy.text('INSERT INTO entries (guestName, content) values ('local guest', 'Also this one');')
    else:
        connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')
        query_string = dict({'unix_socket': '/cloudsql/{}'.format(connection_name)})
        db = sqlalchemy.create_engine(
            sqlalchemy.engine.url.URL(
                drivername=driver_name,
                username=db_user,
                password=db_pass,
                database=db_name,
                query=query_string
            ),
            **db_config
        )
        stmt = sqlalchemy.text('INSERT INTO entries (guestName, content) values ('another guest', 'Also this one');')

    try:
        with db.connect() as conn:
            conn.execute(stmt)
    except Exception as e:
        return 'Error: {}'.format(str(e))
    return 'Hello! You wrote something into your database!\n'



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
