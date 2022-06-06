from flask import Flask
from goldrates import getGoldRates
import os

app = Flask(__name__)


@app.route('/',methods = ['GET'])
def hello_gold():
    return getGoldRates()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)
