from flask import Flask
from goldrates import getGoldRates
from usdrates import getUsdRates
import os

app = Flask(__name__)


@app.route('/',methods = ['GET'])
def hello_gold():
    return getGoldRates()

@app.route('/usd', methods=['GET'])
def hello_usd():
    return getUsdRates()


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)
