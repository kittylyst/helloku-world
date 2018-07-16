import os
import datetime
import json
import psycopg2
import urllib.parse as urlparse
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/users')
def get_users():
    conn = ""
    out = []
    try:
        url = urlparse.urlparse(os.environ['DATABASE_URL'])
        dbname = url.path[1:]
        user = url.username
        password = url.password
        host = url.hostname
        port = url.port
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    except:
        out = {"err": "Unable to connect to the database"}
    try:
        # conn = psycopg2.connect(os.environ.get("DATABASE_URL"))
        cur = conn.cursor()
        cur.execute("""SELECT user_id, user_name from users""")
        rows = cur.fetchall()
        out = []
        for row in rows:
            out.append({"id": row[0], "name": row[1]})
    except:
        out = {"err": "General SQL Error"}
    return json.dumps(out)


# Returns JSON formatted date for AJAX-y goodness
@app.route('/date')
def current_date():
	return json.dumps({"date": str(datetime.datetime.now())})
	
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
