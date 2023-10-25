from flask import *
import sqlalchemy
from route.upload_file import upload_file_route
from route.query_history_message import query_history_message_route
import logging
import os
import time
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
# app.json.ensure_ascii = False
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

app.register_blueprint(upload_file_route)
app.register_blueprint(query_history_message_route)



@app.route('/')
def index():
    return render_template('index.html', time=time.time())

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)