import json
import pymysql
from flask import Flask
from datetime import date, datetime

app = Flask(__name__)

def getConnection():
    return pymysql.connect(
        host='localhost',
        user='app',
        password='app',
        database='app',
        cursorclass=pymysql.cursors.DictCursor)

# date, datetimeの変換関数
def json_serial(obj):
    # 日付型の場合には、文字列に変換します
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    # 上記以外はサポート対象外.
    raise TypeError ("Type %s not serializable" % type(obj))

@app.route('/')
def hello():
    return "<h1>Hello Flask</h1>\n"

@ app.route('/users')
def users():
    connection = getConnection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `user`"
            cursor.execute(sql)
            result = cursor.fetchall()
            return json.dumps(result)

@ app.route('/items')
def items():
    connection = getConnection()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `item`"
            cursor.execute(sql)
            result = cursor.fetchall()
            return json.dumps(result, default=json_serial)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

