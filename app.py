from flask import *
import sqlalchemy
from datetime import datetime
import logging
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

aws_cloud_front_domain_name='https://d305hij1yblnjs.cloudfront.net/'

@app.route('/')
def index():
    return render_template('index.html', time=datetime.now())

@app.route('/uploadFile')
def upload_file():
    pass


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)