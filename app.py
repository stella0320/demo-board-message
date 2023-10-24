from flask import Flask
import sqlalchemy
from datetime import datetime
import logging
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

#log
today = datetime.now().strftime("%Y-%m-%d")
logging.basicConfig(filename='../../opt/log/' + os.getenv('APP_NAME')+ '/record-'+ today + '.log', level=logging.DEBUG, encoding='utf-8', format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
## for console setting
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
## 設定輸出格式
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
## handler 設定輸出格式
console.setFormatter(formatter)
## 加入 hander 到 root logger
logging.getLogger('').addHandler(console)


@app.route('/')
def index():
    return 'Hello, Docker!'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)